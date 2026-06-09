# Missing Posts Recovery Plan

当前缺口来自 `missing_posts.csv`，本轮已从 Reddit 公共 HTML、搜索索引/镜像补回 8 篇正文，剩余 37 条。

## 缺口分类

- `link_only_local_reddit_blocked`：0 条。此前的 3 条已补回。
- `no_body`：12 条。PullPush 记录里正文为空，很多可能本来就是链接帖/截图帖/短标题帖，不一定有长正文。
- `removed:reddit`：16 条。Reddit 层面删除，PullPush 只留下 `[removed]`。需要靠旧缓存、搜索片段、作者转帖或截图。
- `removed:moderator`：7 条。版主删除。若删除前被 PullPush 抓到正文则已保存；没抓到的只能靠缓存/作者转贴。
- `removed:automod_filtered`：1 条。自动过滤，通常正文可能没公开过。
- `removed:content_takedown`：1 条。内容下架，不建议强行恢复全文；只保留标题和元数据。

## 推荐补救顺序

1. 用已登录的 Reddit 页面打开 `missing_posts.csv` 里的 `link_only_local_reddit_blocked` 8 条，手动或自动复制正文。
2. 查作者 X：`https://x.com/aleabitoreddit`，按标题或 ticker 搜索，很多 Reddit DD 会同步成 X 长帖。
3. 查第三方聚合：Buzzberg、Yellowbrick、Buyside Digest、semiconstocks。它们常保留摘要或 ticker 观点，但不一定有 Reddit 原文。
4. 查缓存：Wayback、archive.today、Google/Bing cache/snippets。当前本机访问 Wayback API 多次超时，未能批量确认。
5. 对 `no_body` 做二次判断：如果原帖是链接帖或新闻转发，正文为空就是原始状态，不算遗漏。

## 本轮已补回的 8 条

- 2025-10-10 `1o2op9m` FLY - Reusable Rocket Chairman Kim TA
- 2025-10-06 `1nzp9nl` SNAP - Ghost Bull Formation
- 2025-09-25 `1nqjmwv` NBIS - Nezuko Body Pillow Formation
- 2025-09-10 `1nd9fpz` HIMS - Gym Bro Formation
- 2025-09-08 `1nbtn61` Sweetgreen - Sydney Sweeney Jeans Formation
- 2025-07-02 `1lpsbxa` Upwork - Nine Tailed Fox/Naruto Pattern
- 2025-06-08 `1l6dm8d` Bitcoin/IBIT - Godzilla Formation
- 2025-06-06 `1ky326s` Oscar Health - Crab Pattern

## 最值得继续补的公开页

暂无。剩余缺口主要是空正文帖、重复交叉发帖、已删除帖和 content takedown。

## 如果要继续自动化

最可行的自动化方式是通过一个已经登录 Reddit 的浏览器会话读取这 8 条公开页正文，再回填到：

- `raw/merged_submissions.json`
- `posts/*.md`
- `AleaBito_DD合集.md`

这一步需要显式允许使用你的登录浏览器页面或提供可访问的 Reddit JSON/HTML 内容。
