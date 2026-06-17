"""Local audio → transcript toolbox for conference talks / lectures.

Two halves:

- **Pure helpers** (no third-party deps): VTT parsing, transcript cleaning,
  timestamp formatting, splitting a timestamped transcript into per-talk chunks.
  These are unit-tested and run anywhere.

- **Heavy I/O** (``download_audio`` / ``fetch_subtitles`` / ``transcribe_audio``):
  need ``yt-dlp`` + ``faster-whisper`` + ffmpeg and network access to the video
  host. They lazy-import the optional deps so importing this module (and the rest
  of research_news) never requires them. Install with ``pip install -e ".[asr]"``.

Transcription is meant to run **locally** (it needs a GPU to be fast and access
to YouTube), not in CI / the daily cron — same spirit as the highlight PDFs that
live only on disk.
"""
from __future__ import annotations

import importlib
import logging
import os
import re
from pathlib import Path

log = logging.getLogger(__name__)


# ── pure helpers ──────────────────────────────────────────────────────────────

def parse_timestamp(value) -> float:
    """Parse a timestamp into seconds. Accepts numbers, "SS", "MM:SS",
    "HH:MM:SS", with optional ".mmm" / ",mmm" fractions."""
    if isinstance(value, (int, float)):
        return float(value)
    s = str(value or "").strip().replace(",", ".")
    if not s:
        return 0.0
    if ":" in s:
        sec = 0.0
        for part in s.split(":"):
            sec = sec * 60 + float(part or 0)
        return sec
    try:
        return float(s)
    except ValueError:
        return 0.0


def format_ts(seconds: float) -> str:
    """Seconds → 'H:MM:SS'."""
    total = int(round(seconds))
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}"


def strip_inline_tags(text: str) -> str:
    """Drop WebVTT inline timing tags (<00:00:00.480>, <c>...</c>) and any other
    angle-bracket markup, then collapse whitespace."""
    text = re.sub(r"<\d{1,2}:\d{2}:\d{2}[.,]\d{3}>", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"[ \t]+", " ", text).strip()


_VTT_CUE = re.compile(
    r"^(\d{1,2}:\d{2}:\d{2}[.,]\d{3}|\d{1,2}:\d{2}[.,]\d{3})\s*-->"
)


def parse_vtt(vtt_text: str) -> list[dict]:
    """Parse a WebVTT / SRT-ish subtitle blob into [{'start': sec, 'text': str}].

    Tolerant of YouTube auto-caption quirks (inline timing tags, header lines,
    cue indices). Does not de-duplicate rolling captions — that's clean_transcript's
    job, applied uniformly to both the subtitle and the ASR paths.
    """
    segments: list[dict] = []
    cur_start: float | None = None
    buf: list[str] = []

    def flush() -> None:
        nonlocal cur_start, buf
        if cur_start is not None:
            text = strip_inline_tags(" ".join(buf))
            if text:
                segments.append({"start": cur_start, "text": text})
        cur_start = None
        buf = []

    for raw in vtt_text.splitlines():
        line = raw.strip()
        m = _VTT_CUE.match(line)
        if m:
            flush()
            cur_start = parse_timestamp(m.group(1))
            continue
        if not line:
            continue
        if line in ("WEBVTT",) or line.startswith(("NOTE", "Kind:", "Language:", "STYLE")):
            continue
        if line.isdigit():  # SRT cue index
            continue
        if cur_start is not None:
            buf.append(line)
    flush()
    return segments


def segments_to_text(segments: list[dict], *, with_timestamps: bool = True) -> str:
    """Render parsed segments to a line-per-cue transcript ('[H:MM:SS] text')."""
    lines: list[str] = []
    for seg in segments:
        txt = strip_inline_tags(str(seg.get("text") or ""))
        if not txt:
            continue
        if with_timestamps:
            lines.append(f"[{format_ts(parse_timestamp(seg.get('start', 0)))}] {txt}")
        else:
            lines.append(txt)
    return "\n".join(lines)


_LINE_TS = re.compile(r"^\[(\d{1,2}:\d{2}:\d{2})\]\s*(.*)$")


def _split_line(line: str) -> tuple[str | None, str]:
    m = _LINE_TS.match(line)
    if m:
        return m.group(1), m.group(2)
    return None, line


def clean_transcript(text: str) -> str:
    """Collapse the duplication ASR / auto-captions produce.

    - drops blank lines and inline timing tags;
    - drops a line identical to the one before it (Whisper repetition loops);
    - collapses rolling captions where each line extends the previous one
      (keeps the longest), the classic YouTube auto-sub pattern.
    Timestamps (if present) are preserved on the kept line.
    """
    out: list[str] = []
    prev = ""
    for raw in text.splitlines():
        ts, body = _split_line(raw.rstrip())
        body = strip_inline_tags(body)
        if not body:
            continue
        rendered = f"[{ts}] {body}" if ts else body
        if body == prev:
            continue
        # rolling growth: previous kept line is a prefix of this one → replace it
        if prev and out and body.startswith(prev) and len(body) > len(prev):
            out[-1] = rendered
            prev = body
            continue
        out.append(rendered)
        prev = body
    return "\n".join(out)


def split_by_segments(text: str, segments: list[dict]) -> list[dict]:
    """Split a timestamped transcript into per-talk chunks at segment starts.

    Returns [{'speaker', 'title', 'start', 'text'}], one per segment, sorted by
    start time. Empty ``segments`` → a single chunk holding the whole text.
    Lines without a parseable timestamp fall into the first chunk.
    """
    if not segments:
        return [{"speaker": None, "title": None, "start": 0.0, "text": text}]

    parsed: list[tuple[float | None, str]] = []
    for raw in text.splitlines():
        ts, _ = _split_line(raw)
        parsed.append((parse_timestamp(ts) if ts else None, raw))

    bounds = sorted(
        ((parse_timestamp(s.get("start", 0)), s) for s in segments),
        key=lambda b: b[0],
    )
    chunks: list[dict] = []
    for i, (start_sec, seg) in enumerate(bounds):
        end_sec = bounds[i + 1][0] if i + 1 < len(bounds) else float("inf")
        lo = start_sec if i > 0 else float("-inf")  # first chunk also keeps untimed lead-in
        body = [ln for (s, ln) in parsed if s is not None and lo <= s < end_sec]
        if i == 0:
            untimed = [ln for (s, ln) in parsed if s is None]
            body = untimed + body
        chunks.append({
            "speaker": seg.get("speaker"),
            "title": seg.get("title"),
            "start": start_sec,
            "text": "\n".join(body),
        })
    return chunks


# ── heavy I/O (lazy optional deps) ────────────────────────────────────────────

def _lazy_import(name: str):
    try:
        return importlib.import_module(name)
    except ImportError as e:  # pragma: no cover - exercised only without the extra
        raise RuntimeError(
            f"'{name}' is required for talk transcription. Install the ASR extra:\n"
            f"    pip install -e \".[asr]\"\n"
            f"and make sure ffmpeg is on PATH."
        ) from e


_AUDIO_EXTS = (".m4a", ".mp3", ".wav", ".webm", ".opus", ".ogg", ".aac")

# Heartbeat cadence for transcription progress, in seconds of *audio* processed.
PROGRESS_EVERY_SECS = float(os.environ.get("WHISPER_PROGRESS_SECS", "120"))


def download_audio(url: str, dest_dir: Path | str, talk_id: str) -> Path:
    """Download the best audio track of `url` to dest_dir/<talk_id>.<ext> (yt-dlp).
    Reuses an already-downloaded file if present (no re-download)."""
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    existing = [c for c in sorted(dest_dir.glob(f"{talk_id}.*"))
                if c.suffix.lower() in _AUDIO_EXTS]
    if existing:
        log.info("audio already present, skipping download: %s", existing[0].name)
        return existing[0]
    yt_dlp = _lazy_import("yt_dlp")
    opts = {
        "format": "bestaudio/best",
        "outtmpl": str(dest_dir / f"{talk_id}.%(ext)s"),
        "quiet": True,
        "no_warnings": True,
        "postprocessors": [
            {"key": "FFmpegExtractAudio", "preferredcodec": "m4a", "preferredquality": "0"}
        ],
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])
    cands = [c for c in sorted(dest_dir.glob(f"{talk_id}.*"))
             if c.suffix.lower() in _AUDIO_EXTS]
    if not cands:
        raise RuntimeError(f"audio download produced no file for {talk_id} in {dest_dir}")
    return cands[0]


def fetch_subtitles(url: str, dest_dir: Path | str, talk_id: str,
                    *, lang: str = "en") -> str | None:
    """Try to grab existing (human or auto) subtitles as VTT text, no ASR.

    Returns the VTT blob, or None when the video has no subtitles in `lang`.
    """
    yt_dlp = _lazy_import("yt_dlp")
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    opts = {
        "skip_download": True,
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": [lang, f"{lang}.*", f"{lang}-orig"],
        "subtitlesformat": "vtt",
        "outtmpl": str(dest_dir / f"{talk_id}.%(ext)s"),
        "quiet": True,
        "no_warnings": True,
        # Be gentle with YouTube on bulk runs — back off on the 429s it throws
        # after a burst of caption requests.
        "retries": 5,
        "extractor_retries": 5,
        "sleep_interval_requests": 1,
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])
    vtts = sorted(dest_dir.glob(f"{talk_id}*.vtt"))
    if not vtts:
        return None
    return vtts[0].read_text(encoding="utf-8", errors="ignore")


def transcribe_audio(
    audio_path: Path | str,
    *,
    model_size: str = "large-v3",
    initial_prompt: str | None = None,
    language: str | None = None,
    device: str | None = None,
    compute_type: str | None = None,
) -> list[dict]:
    """Transcribe an audio file with faster-whisper → [{'start','end','text'}].

    `initial_prompt` biases recognition toward domain terms / names. Device and
    compute type default to env (WHISPER_DEVICE / WHISPER_COMPUTE_TYPE) then
    auto, so a GPU box and a CPU box both work without code changes.
    """
    fw = _lazy_import("faster_whisper")
    device = device or os.environ.get("WHISPER_DEVICE", "auto")
    compute_type = compute_type or os.environ.get("WHISPER_COMPUTE_TYPE", "default")
    log.info("loading whisper model=%s device=%s compute=%s", model_size, device, compute_type)
    model = fw.WhisperModel(model_size, device=device, compute_type=compute_type)
    segments, info = model.transcribe(
        str(audio_path),
        initial_prompt=initial_prompt,
        language=language,
        vad_filter=True,
        beam_size=5,
    )
    total = float(getattr(info, "duration", 0.0) or 0.0)
    log.info("transcribing %s of audio (language=%s) — heartbeat every %ds of audio",
             format_ts(total) if total else "?", getattr(info, "language", "?"),
             int(PROGRESS_EVERY_SECS))
    out: list[dict] = []
    next_mark = PROGRESS_EVERY_SECS
    for seg in segments:
        txt = (seg.text or "").strip()
        if txt:
            out.append({"start": float(seg.start), "end": float(seg.end), "text": txt})
        # Heartbeat keyed on audio time processed, so a long (or stuck) run is
        # visible instead of a silent console.
        if seg.end >= next_mark:
            pct = f" ({min(100.0, seg.end / total * 100):.0f}%)" if total else ""
            log.info("  … %s / %s%s — %d segments so far",
                     format_ts(seg.end), format_ts(total) if total else "?", pct, len(out))
            while next_mark <= seg.end:
                next_mark += PROGRESS_EVERY_SECS
    log.info("transcribed %d segments (%s of audio, language=%s)",
             len(out), format_ts(total) if total else "?", getattr(info, "language", "?"))
    return out
