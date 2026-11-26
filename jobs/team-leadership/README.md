# Lead your team

Check lead handling, see the weekly numbers and answer agent questions.

## Skills in this folder

One skill per job. Pick the job you need done.

| Job to be done | Skill |
|---|---|
| Catch unassigned or uncontacted leads | [lead-routing-watchdog](skills/lead-routing-watchdog/SKILL.md) |
| Measure how fast agents answer leads | [speed-to-lead-scorecard](skills/speed-to-lead-scorecard/SKILL.md) |
| Spot where an agent may need coaching | [agent-coaching-radar](skills/agent-coaching-radar/SKILL.md) |
| List which agents to check in with | [agent-retention-check-ins](skills/agent-retention-check-ins/SKILL.md) |
| Follow up with recruiting candidates | [agent-recruiting-follow-up](skills/agent-recruiting-follow-up/SKILL.md) |
| Review the week's pipeline by source | [weekly-pipeline-review](skills/weekly-pipeline-review/SKILL.md) |
| Write the Monday brief for the owner | [monday-owner-brief](skills/monday-owner-brief/SKILL.md) |

## Workflows

Full instructions are in [workflows.md](workflows.md). Core workflows are the ones to start with.

| ID | Workflow | Priority | Use if | Our skill | Existing skill |
|---|---|---|---|---|---|
| O1 | [Lead routing watchdog](workflows.md#o1) | Core | you manage lead routing | [lead-routing-watchdog](skills/lead-routing-watchdog/SKILL.md) | [route-lead](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/sales/skills/route-lead) |
| O2 | [Speed-to-lead scorecard](workflows.md#o2) | Core | you need to know how fast agents respond | [speed-to-lead-scorecard](skills/speed-to-lead-scorecard/SKILL.md) | - |
| B1 | [Monday owner brief](workflows.md#b1) | Core | you need the weekly owner numbers | [monday-owner-brief](skills/monday-owner-brief/SKILL.md) | [monday-brief](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/small-business/skills/monday-brief), [business-pulse](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/small-business/skills/business-pulse) |
| P2 | [Policy and onboarding assistant](workflows.md#p2) | Core | agents keep asking the same questions | - | [policy-lookup](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/human-resources/skills/policy-lookup) |
| P1 | [Weekly coaching radar](workflows.md#p1) | Add when needed | you coach agents | [agent-coaching-radar](skills/agent-coaching-radar/SKILL.md) | [performance-review](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/human-resources/skills/performance-review) |
| R1 | [Recruiting pipeline assistant](workflows.md#r1) | Add when needed | you are recruiting agents | [agent-recruiting-follow-up](skills/agent-recruiting-follow-up/SKILL.md) | [recruiting-pipeline](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/human-resources/skills/recruiting-pipeline) |
| R2 | [Retention check-in prompts](workflows.md#r2) | Add when needed | you want to keep good agents | [agent-retention-check-ins](skills/agent-retention-check-ins/SKILL.md) | - |
| E2 | [Weekly pipeline and source review](workflows.md#e2) | Add when needed | it is time to review the week | [weekly-pipeline-review](skills/weekly-pipeline-review/SKILL.md) | [pipeline-review](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/sales/skills/pipeline-review), [weekly-wrap](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/sales/skills/weekly-wrap) |

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
