# Evidence and Maturity Rules — A 股增强版

Use for all sector, company, monopoly, and recommendation claims.

## Evidence Grades

| Grade | Sources | Can support |
|---|---|---|
| **A** | Company filings, annual/interim reports, exchange filings (上交所/深交所/港交所/SEC), official IR, official customer or regulator announcements, official product datasheets | Core facts, revenue, capacity, product existence, management statements |
| **B** | Peer-reviewed papers, conference materials, industry bodies, credible market research, standards organizations, official university/lab pages, 中国半导体行业协会/中国光伏行业协会等官方行业组织 | Technical feasibility, market structure, industry sizing, standards |
| **C** | Broker reports, media, expert calls, social posts, supply-chain rumors, community trackers, 东方财富/同花顺数据汇总 | Leads, hypotheses, watch items |

C-level evidence cannot alone support:

- "global monopoly" / "全球垄断"
- "mass production" / "量产" / "核心客户导入"
- "top customer adoption" / "国产替代已完成"
- "unavoidable chokepoint" / "不可绕开瓶颈"
- "High conviction" / "高确信推荐"
- "core bottleneck solved" / "核心瓶颈已突破"

## Source Type Distinction (强制)

| Type | Definition | Examples |
|---|---|---|
| **一手来源 (Primary)** | Original publisher of the event/data | Company announcements (巨潮资讯网), exchange filings, regulatory filings, official IR, customer official press releases, official product specs |
| **二手来源 (Secondary)** | Reinterpretation, summary, or commentary on primary sources | Media reports, broker research, community posts, trackers, third-party databases, blog interpretations |

### Annotation Format

Every key claim must be annotated:

```text
[Grade|Primary/Secondary] 例如：
"中际旭创 800G 光模块已向核心客户批量交付 [A|一手 — 公司 2024 年年报]"
"据券商研报，国内光通信需求 2025 年将增长 40% [C|二手 — 中信证券研报 2025.03]"
"国产 EDA 工具在 28nm 以上制程已实现替代 [B|一手 — 中国半导体行业协会 2024 年度报告]"
```

If unable to annotate, mark as `[待验证]` and explain what evidence is missing.

### Source Hierarchy

1. **一手来源**（highest credibility）: Company filings, exchange/regulatory filings, official IR, customer official press releases
2. **一手衍生** (Primary-derived): Calculations/inferences based on primary data (e.g., revenue growth rate calculated from announced figures)
3. **二手来源** (Secondary): Media, brokers, community, trackers, third-party databases
4. **待验证** (Unverified): Cannot confirm source or source credibility is doubtful

## Maturity Definitions

Use precise maturity language:

| Term | Meaning |
|---|---|
| R&D | Lab or internal development; no customer validation proven |
| Prototype | Demonstrated sample or product concept |
| Sample / 送样 | Customer has samples; no production proof |
| Pilot | Trial line or limited engineering production |
| LVM | Low-volume manufacturing with limited customers or SKUs |
| HVM | High-volume manufacturing with stable yield and commercial delivery |
| AVL / qualified | Approved by customer or platform, but may not imply large revenue |
| Mass shipment | Repeated commercial shipments with meaningful revenue or disclosed volumes |

## Required Source Language

When evidence is not A-grade, qualify the claim:

- "据媒体/券商/专家访谈线索"
- "公开资料尚不能证明"
- "更适合作为待验证假设"
- "不能单独支撑垄断结论"
- "据二手来源转述，一手来源尚未核验"

## A 股特有证据注意事项

| 场景 | 注意事项 |
|---|---|
| 互动易 / e 互动 | 属于公司官方回复，可视为 A 级一手，但注意措辞可能模糊 |
| 券商研报 | C 级二手来源，盈利预测和目标价仅供参考 |
| 公募/私募持仓 | 季报披露的持仓数据有时滞，属 A 级但有滞后性 |
| 龙虎榜 | 交易所官方数据，A 级一手，但仅反映短期交易行为 |
| 北向资金 | A 级一手数据，但需注意短期波动不代表长期趋势 |
| 行业协会数据 | B 级一手，注意统计口径和会员覆盖面 |
| 供应链调研/专家访谈 | C 级二手，不能单独支撑核心结论 |
