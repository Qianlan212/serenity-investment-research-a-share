# Subagent Research Playbook — A 股定制版

Use only when the user explicitly asks for subagents, parallel agents, or "每部分一个 subagent".

## Recommended Split

For deep industry-chain work, assign 5-7 independent modules:

1. **需求与产业革命**：why demand/architecture makes the chain important now. 含中国政策催化分析。
2. **技术路线与瓶颈**：materials, components, process, equipment, reliability. 每个节点标注中国位置。
3. **全球玩家路线图**：high-end spec setters, scale suppliers, pilot/HVM status. 标注 A 股对标。
4. **中国位置地图**：Chinese companies by chain node, strengths, weaknesses, evidence grade, 国产替代进度.
5. **上游材料/设备**：unavoidable materials, tools, chemicals, yield windows. 标注国产替代现状。
6. **垄断判断与反证**：three-layer monopoly test, 国产替代进度, strongest bear case, downgrade triggers.
7. **A 股个股映射与评分**：按投资者画像筛选和排序，包含持仓建议。

## Integration Rules

- Each subreport must have one-line conclusion, evidence table (with grades and source types), key sources, and counter-evidence.
- The main report must not merely concatenate subreports. It must answer:
  - 替代了什么？
  - 解决了什么瓶颈？
  - 中国强在哪？
  - 中国不强在哪？
  - 是否控制不可绕开的节点？
  - 国产替代进度如何？
  - 哪些事实会推翻 thesis？
  - A 股投资者如何参与？
- Preserve evidence grades and source type annotations. Do not upgrade a C-level lead into an A-level fact during synthesis.
- If writing files, include an index/README and verify no unfinished placeholder markers remain.
