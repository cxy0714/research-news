"""Throwaway smoke test: run publish-favorites' "Verify GIST_TOKEN" step with
stubbed curl/gh, so the shell logic (expiry math, warning branch, issue body) is
exercised without touching GitHub. Deleted after use."""
import os
import subprocess
import tempfile

import yaml

WF = ".github/workflows/publish-favorites.yml"
CURL_STUB = """#!/bin/bash
if [[ "$*" == *-sSI* ]]; then
  printf 'HTTP/2 200\\r\\ngithub-authentication-token-expiration: %s 12:00:00 UTC\\r\\n' "$STUB_EXP"
else
  next=
  for a in "$@"; do
    if [ "$a" = "-o" ]; then next=1
    elif [ -n "$next" ]; then echo '{"login":"cxy0714"}' > "$a"; next=; fi
  done
  printf '%s' "$STUB_CODE"
fi
"""
GH_STUB = """#!/bin/bash
echo "[stub gh] $1 $2 ${@:3}" >&2
if [ "$1 $2" = "issue list" ]; then echo "$STUB_EXISTING"; fi
"""


def run_step(*, code="200", exp="2026-09-08", existing="", warn_days="14"):
    step = yaml.safe_load(open(WF, encoding="utf-8"))["jobs"]["publish"]["steps"][0]
    stub = tempfile.mkdtemp()
    for name, body in (("curl", CURL_STUB), ("gh", GH_STUB)):
        p = os.path.join(stub, name)
        with open(p, "w", newline="\n", encoding="utf-8") as f:
            f.write(body)
        os.chmod(p, 0o755)
    sh = os.path.join(stub, "step.sh")
    with open(sh, "w", newline="\n", encoding="utf-8") as f:
        f.write(step["run"])
    out = os.path.join(stub, "out.txt")
    body_file = "/tmp/gist_token_body.md"
    if os.path.exists(body_file):
        os.remove(body_file)
    env = {
        **os.environ,
        "PATH": stub + os.pathsep + os.environ["PATH"],
        "GIST_TOKEN": "stub-token", "GH_TOKEN": "stub", "REPO": "cxy0714/research-news",
        "WARN_WITHIN_DAYS": warn_days,
        "STUB_CODE": code, "STUB_EXP": exp, "STUB_EXISTING": existing,
    }
    cmd = 'bash "%s" > "%s" 2>&1' % (sh.replace(os.sep, "/"), out.replace(os.sep, "/"))
    rc = subprocess.run(["bash", "-c", cmd], env=env).returncode
    text = open(out, encoding="utf-8").read()
    body = open(body_file, encoding="utf-8").read() if os.path.exists(body_file) else None
    return rc, text, body


def case(label, **kw):
    rc, text, body = run_step(**kw)
    print(f"===== {label} → exit {rc} =====")
    print(text.rstrip())
    if body:
        print("--- issue body ---")
        print(body.rstrip())
    print()


case("expiring in ~8 days, no open issue", exp="2026-09-08")
case("expiring, open issue #7 exists", exp="2026-09-08", existing="7")
case("healthy, far from expiry", exp="2027-06-01")
case("expired token (401)", code="401")
case("no expiry header (No expiration)", exp="")
