# Lead your team

Check lead handling, see the weekly numbers and answer agent questions.

## Skills in this folder

- [team-performance-review](skills/team-performance-review/SKILL.md): Review real estate team performance, including lead routing checks, speed-to-lead scorecards, coaching signals, retention check-ins, pipeline and source reviews, lead quality and recruiting follow-up.

## Skills used from other jobs

- [brokerage-money-checks](../back-office/skills/brokerage-money-checks/SKILL.md)

## Workflows

Full instructions are in [workflows.md](workflows.md). Core workflows are the ones to start with.

| ID | Workflow | Priority | Use if | Our skill | Existing skill |
|---|---|---|---|---|---|
| O1 | [Lead routing watchdog](workflows.md#o1) | Core | you manage lead routing | [team-performance-review](skills/team-performance-review/SKILL.md) | [route-lead](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/sales/skills/route-lead) |
| O2 | [Speed-to-lead scorecard](workflows.md#o2) | Core | you need to know how fast agents respond | [team-performance-review](skills/team-performance-review/SKILL.md) | - |
| B1 | [Monday owner brief](workflows.md#b1) | Core | you need the weekly owner numbers | [brokerage-money-checks](../back-office/skills/brokerage-money-checks/SKILL.md) | [monday-brief](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/small-business/skills/monday-brief), [business-pulse](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/small-business/skills/business-pulse) |
| P2 | [Policy and onboarding assistant](workflows.md#p2) | Core | agents keep asking the same questions | - | [policy-lookup](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/human-resources/skills/policy-lookup) |
| P1 | [Weekly coaching radar](workflows.md#p1) | Add when needed | you coach agents | [team-performance-review](skills/team-performance-review/SKILL.md) | [performance-review](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/human-resources/skills/performance-review) |
| R1 | [Recruiting pipeline assistant](workflows.md#r1) | Add when needed | you are recruiting agents | [team-performance-review](skills/team-performance-review/SKILL.md) | [recruiting-pipeline](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/human-resources/skills/recruiting-pipeline) |
| R2 | [Retention check-in prompts](workflows.md#r2) | Add when needed | you want to keep good agents | [team-performance-review](skills/team-performance-review/SKILL.md) | - |
| E2 | [Weekly pipeline and source review](workflows.md#e2) | Add when needed | it is time to review the week | [team-performance-review](skills/team-performance-review/SKILL.md) | [pipeline-review](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/sales/skills/pipeline-review), [weekly-wrap](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/sales/skills/weekly-wrap) |

## Notes on existing skills

- P1: The existing one is for formal reviews, not weekly coaching.

## Install

```bash
/plugin marketplace add n-realty-ai/realty-ai-agent-skills
```

```bash
/plugin install realty-team-leadership@realty-ai-agent-skills
```

Run those two inside Claude Code. Also install `realty-writing`, which the other skills use for client-facing text.
