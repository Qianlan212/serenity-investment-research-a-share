# AleaBito / Serenity DD Collection

生成时间：2026-05-30 08:28:16 UTC

本资料夹整理 Reddit 用户 `u/AleaBito`（Serenity / `@aleabitoreddit`）公开可检索的 submissions。核心来源是 PullPush Reddit 历史索引，外加 Reddit 个人页当前可见的新帖链接手工补齐。

## 统计

- 去重 submissions：82
- 已保存正文：45
- 已删除/被移除：25
- 仅链接/本机未抓到正文：0

## 文件

- `submissions_dedup.csv`：去重总表，适合表格软件打开。
- `submissions_dedup.json`：去重总表 JSON 版。
- `timeline.md`：按时间倒序排列。
- `by_ticker.md`：按识别出的 ticker 分组。
- `AleaBito_DD合集.md`：已抓到正文的帖子全文合集。
- `posts/`：逐篇 markdown 文件，能抓到正文的已放入正文。
- `raw/pullpush_author_AleaBito.json`：PullPush 原始返回。
- `raw/merged_submissions.json`：合并后的完整 JSON，包含正文。
- `third_party_tracker_snapshot.md`：第三方 Serenity Tracker 资料摘录。

## 来源分布

- pullpush: 70
- recovered_bitbbq_reddit_mirror: 1
- recovered_reddit_public_html: 3
- recovered_search_index_reddit: 4
- reddit_profile_json_manual: 3
- search_result_deleted_manual: 1

## 抓取限制

本机无登录请求 Reddit 官方 API 时多次出现 `403 Blocked`、连接重置或超时。因此：

- PullPush 里有正文的帖子，已完整保存。
- Reddit 个人页最新可见但 PullPush 未收录的帖子，已补入标题和链接；其中 AXTI、META、T1 Energy 三篇已根据 Reddit JSON 可读输出补入正文。
- GRRR 一帖仅能确认标题和原链接，页面显示已被版主删除。

## 参考入口

- Reddit profile: https://www.reddit.com/user/AleaBito/submitted/
- PullPush API: https://api.pullpush.io/reddit/search/submission/?author=AleaBito&size=100&sort=desc
- Serenity Tracker: https://semiconstocks.com/
