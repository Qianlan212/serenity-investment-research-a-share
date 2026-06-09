# Monopoly and China Position Framework — A 股定制版

Use when judging whether China, a country, or a company has monopoly power in a supply chain.

## Three-Layer Monopoly Test

| Layer | Question | Valid conclusion |
|---|---|---|
| 全球份额垄断 | Does the entity control mainstream global high-end capacity, pricing, delivery, and customer access? | Global monopoly / no global monopoly |
| 技术瓶颈垄断 | Does it control an unavoidable material, process, equipment, patent, yield window, or qualification database? | Chokepoint control / partial control / no control |
| 本土替代强势 | Inside China or another local ecosystem, does it have customer, cost, delivery, policy, and engineering advantages? | Local substitution strength / chasing / weak |

Do not collapse these layers into one answer. A country can be locally strong without being globally monopolistic.

## Rating Labels

Use these labels by chain node:

- **全球领先**：sets high-end specs, has top customers, and ships at scale.
- **本土强势**：strong in domestic ecosystem or commodity/mid-high-end supply, but not global high-end control.
- **追赶验证**：credible samples, pilot, or partial shipments, but high-end customers/yield still being proven.
- **概念参与**：related business exists, but exposure or high-end relevance is unclear.
- **证据不足**：no reliable evidence for the claim.

## 国产替代进度标注

For each chain node, also label:

- **已替代**：国产产品已在大客户中量产使用，有收入和份额数据支撑 [A|一手]。
- **部分替代**：国产产品在中低端已使用，高端仍在追赶或认证中。
- **追赶中**：有样品/小批量，但尚未通过大客户认证或量产。
- **未起步**：无可靠证据表明国产替代有实质进展。

## Required Anti-Hype Checks

Before saying "monopoly" or "国产替代已完成", test:

- Are there overseas suppliers with qualified high-end products?
- Is the claim based on capacity, or on customer-qualified high-end capacity?
- Does "mass production" mean HVM, LVM, pilot, or sample?
- Is the node technically unavoidable, or can architecture/design route around it?
- Are price increases from structural scarcity, or restocking/commodity cycles?
- Do customer names, AVL status, revenue share, and yield have primary evidence?
- 国产替代的"认证"是客户官方公告确认，还是仅来自供应链传闻或互动易模糊回复？
- "份额提升"是否有具体数据和一手来源？

## Output Conclusion Format

Use a direct split:

```text
全球垄断：否/是，原因... [证据等级|一手/二手]
技术瓶颈控制：否/部分/是，原因... [证据等级|一手/二手]
本土替代强势：否/部分/是，原因... [证据等级|一手/二手]
国产替代进度：已替代/部分替代/追赶中/未起步，原因... [证据等级|一手/二手]
最终判断：...
A 股受益标的：...
```
