# research-news

陈星宇个人定制的每日研究资讯系统。每天抓 arXiv 新论文 + 关注的会议/seminar 页面 + 关注的作者，调用 SJTU LLM API 按个人兴趣排序、生成中文摘要，渲染成 MkDocs Material 站点。

## 当前覆盖

- **arXiv 每日新提交**: stat.ME, stat.TH, math.ST, econ.EM, astro-ph.IM
- **会议/Seminar 页面**: SCI, ACIC, EuroCIM, PCIC, ETH SfS（LLM 解析事件）
- **作者追踪**: Semantic Scholar API（先填 `config/authors.yaml` 再启用）

## 本地起步

```bash
# 1. 装依赖（建议 venv）
python -m venv .venv && source .venv/bin/activate
pip install -e ".[docs]"

# 2. 配 API key
cp .env.example .env
# 编辑 .env，填入 SJTU_API_KEY

# 3. 编辑兴趣 & 作者列表（可选）
vim config/interests.yaml
vim config/authors.yaml

# 4. 干跑一次（不调 LLM，只看抓到啥）
python -m research_news.daily --dry-run

# 5. 完整跑一次
python -m research_news.daily

# 6. 本地预览站点
mkdocs serve
```

## 定时（macOS / Linux cron）

```cron
30 7 * * 1-5 /absolute/path/to/research-news/run_daily.sh >> /tmp/research-news.log 2>&1
```

## 部署到 GitHub Pages

仓库 Settings → Pages → Source 选 `Deploy from a branch` → `main` / `docs` 文件夹，
或者用 `mkdocs gh-deploy` 部署到 `gh-pages`。

## 安全

- API key 走 `.env`，已 `.gitignore`。**不要 commit `.env`。**
- 本仓库公开，但里面没有任何凭证。

## 目录

```
research_news/        # 主代码包
  scrapers/           # arxiv / conferences / authors
  llm/                # SJTU client + scoring/summarization pipeline
  render/             # markdown 渲染
config/               # 兴趣、信源、作者列表
docs/                 # MkDocs 源（每日报告生成在 docs/daily/）
data/                 # 运行时缓存（已 gitignore 部分）
```

## TODO

- [ ] 添加期刊 RSS（JASA, AoS, Biometrika, JRSS-B）
- [ ] 添加 NBER working papers
- [ ] 添加邮件推送（可选）
- [ ] 跑通后调优会议页面 LLM 解析 prompt
