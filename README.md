# Serenity Investment Research Skill — A-Share Customized Edition

基于 [Serenity/AleaBito 瓶颈迁移框架](https://github.com/dantewoo/serenity-investment-research-skill) 定制，适配 A 股投资者。

核心框架不变：

```text
超级周期 -> 架构变化 -> 瓶颈 / chokepoint
-> 被忽视的供应商、材料节点、产能节点
-> 证据链（强制标注等级 + 区分一手/二手）-> 收入/估值弹性
-> 市场反馈 -> 推荐/观察/否决 -> 反证清单
-> 适配持仓规则与交易风格
```

## 与原版的主要差异

| 维度 | 原版 | A 股定制版 |
|---|---|---|
| 市场定位 | 以美股为主 | A 股为主，海外通过 ETF/港股通 |
| 投资风格 | 未限定 | 波段交易 + 趋势交易，1-18 个月 |
| 市值偏好 | 未限定 | 中盘、大盘优先 |
| 行业聚焦 | 广泛 | AI 基建/光通信/半导体/机器人/航天/电网/有色金属 |
| 中国优势 | 分析维度之一 | 偏重国产替代和本土强势 |
| 持仓规则 | 未限定 | 单笔 5%-20%，止损/止盈，不对冲 |
| 衍生品 | 包含 warrant 等策略 | 不使用期权/warrant/可转债等衍生品 |
| 证据标注 | 标注等级 | 强制标注等级 + 区分一手/二手来源 |
| 输出风格 | 固定模板 | 深度为主，根据场景自动选择格式 |

## 适用场景

- **产业链研究**：AI 基建、光通信、半导体、机器人、航天、电网、有色金属等产业链的瓶颈分析。
- **中国位置判断**：分析中国在某个上游环节是否具备全球垄断、本土替代或追赶验证地位。
- **国产替代研究**：跟踪各环节国产替代进度和认证状态。
- **投资候选筛选**：把产业链节点映射到 A 股公司，并用六维评分判断候选优先级。
- **股票研究推荐**：在用户明确要求时，给出 Recommend / Watchlist / Avoid 和 conviction，并附持仓建议。

## 目录结构

```text
serenity-investment-research-a-share/
├── SKILL.md                              # 主技能入口文件
├── README.md                             # 本文件
├── agents/openai.yaml                    # Agent 配置
├── scripts/search_serenity_corpus.py     # 语料检索脚本
└── references/
    ├── serenity-framework.md             # 核心投资框架
    ├── recommendation-scoring.md         # 六维推荐评分（含 A 股适配）
    ├── industry-chain-research.md        # 产业链研究模板（含国产替代）
    ├── monopoly-framework.md             # 中国位置和垄断判断模板
    ├── evidence-and-maturity.md          # 证据等级和成熟度定义（含 A 股来源）
    ├── investor-profile.md              # 投资者画像与约束规则
    ├── report-template.md               # 股票推荐模板（含持仓建议）
    ├── external-sources.md              # 外部资料入口（含 A 股资料）
    ├── serenity-casebook.md             # 案例类比（含 A 股案例）
    ├── subagent-research-playbook.md    # 多 Agent 研究手册
    └── corpus/                           # Serenity 语料库
```

## 关键原则

1. 先研究产业链，再决定是否推荐股票。
2. 区分周期品和结构性瓶颈，避免把补库、涨价、库存周期误判成产业革命。
3. 所有"垄断、量产、客户导入、高确信推荐、国产替代完成"都必须有足够证据等级支撑。
4. C 级证据只能作为线索，不能单独支撑核心结论。
5. 强推荐必须配强反证，明确什么事实会推翻 thesis。
6. 所有输出强制标注证据等级（A/B/C）和来源类型（一手/二手）。
7. A 股优先，海外标的必须提供 ETF 或港股通参与路径。
8. 推荐必须包含持仓建议（仓位、止损、止盈、周期）。
9. 不使用衍生品策略，不对冲。

## 证据等级

- **A 级**：公司公告、年报、监管文件、交易所文件、官方 IR、客户公告、官方产品资料。
- **B 级**：论文、会议、行业协会、可信机构资料、标准组织资料。
- **C 级**：券商研报、媒体、专家访谈、社媒线索、供应链传闻。

## 使用方式

在支持 Codex 技能的环境中触发：

```text
[$serenity-investment-research-a-share] 按 Serenity 思路分析这个产业链
```

或者：

```text
用 serenity-investment-research-a-share 分析某 A 股公司是否是下一层瓶颈受益者
```

内置语料检索脚本：

```bash
python scripts/search_serenity_corpus.py --query "AI infrastructure" --top-k 8
```

## 致谢

本技能基于 [dantewoo/serenity-investment-research-skill](https://github.com/dantewoo/serenity-investment-research-skill) 原版定制，感谢原作者和 Serenity/AleaBito 的研究贡献。

## 免责声明

本技能用于研究和思考辅助，不构成个性化投资建议。任何结论都依赖公开资料和当前价格环境，需要随新公告、财报、客户验证、产能变化和市场反馈持续更新。持仓规则和止损/止盈建议仅供参考，请根据自身风险承受能力调整。
