# Win and follow up leads

Answer new inquiries fast and keep every lead moving.

## Skills in this folder

One skill per job. Pick the job you need done.

| Job to be done | Skill |
|---|---|
| Alert an agent to a new lead with a reply draft | [new-lead-alert](skills/new-lead-alert/SKILL.md) |
| Acknowledge leads that arrive after hours | [after-hours-lead-reply](skills/after-hours-lead-reply/SKILL.md) |
| Follow up open house visitors who agreed to contact | [open-house-follow-up](skills/open-house-follow-up/SKILL.md) |
| Pull this week's call list from a CRM with no connector | [crm-call-list](skills/crm-call-list/SKILL.md) |
| Research expired and withdrawn listings | [expired-listing-research](skills/expired-listing-research/SKILL.md) |

## Workflows

Full instructions are in [workflows.md](workflows.md). Core workflows are the ones to start with.

| ID | Workflow | Priority | Use if | Our skill | Existing skill |
|---|---|---|---|---|---|
| L1 | [Instant lead alert with reply draft](workflows.md#l1) | Core | a new lead just came in | [new-lead-alert](skills/new-lead-alert/SKILL.md) | [speed-to-lead](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/small-business/skills/speed-to-lead), [lead-follow-up](https://github.com/polytheseus/real-estate-skills/tree/91df95c7e9c57c2b65456ffbc0b050873af09310/skills/lead-follow-up) |
| L2 | [After-hours capture and handoff](workflows.md#l2) | Core | leads arrive while you are busy or after hours | [after-hours-lead-reply](skills/after-hours-lead-reply/SKILL.md) | [speed-to-lead](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/small-business/skills/speed-to-lead) |
| N2 | [Open house sign-in to follow-up](workflows.md#n2) | Core | you are hosting an open house | [open-house-follow-up](skills/open-house-follow-up/SKILL.md) | [open-house-follow-up](https://github.com/SkillMedev/real-estate-agent-stack/tree/d0216171dd74239720abe8bc24854bd9884b7024/skills/open-house-follow-up), [lead-follow-up](https://github.com/polytheseus/real-estate-skills/tree/91df95c7e9c57c2b65456ffbc0b050873af09310/skills/lead-follow-up) |
| F1 | [Dormant lead reactivation list](workflows.md#f1) | Core | your database has old leads sitting untouched | - | [reactivate](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/small-business/skills/reactivate) |
| F2 | [Next-step enforcer](workflows.md#f2) | Core | you are not sure what happens next with a lead | - | [crm-autopilot](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/small-business/skills/crm-autopilot), [crm-hygiene-check](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/sales/skills/crm-hygiene-check) |
| F5 | [Closed-CRM call list](workflows.md#f5) | Add when needed | your CRM has no connector | [crm-call-list](skills/crm-call-list/SKILL.md) | - |
| N7 | [Expired and withdrawn listing research list](workflows.md#n7) | Add when needed | you prospect expired or withdrawn listings | [expired-listing-research](skills/expired-listing-research/SKILL.md) | [prospecting](https://github.com/coreyhaines31/marketingskills/tree/2bf95edb4ebd37198ab7fd18b99ba95c2145ec64/skills/prospecting) |

## Notes on existing skills

- F1: Add the consent rule from the sheet.
- F2: crm-autopilot writes to the CRM: keep approval on.
- N7: The existing one covers business prospecting, not MLS lists.

## Install

```bash
/plugin marketplace add n-realty-ai/realty-ai-agent-skills
```

```bash
/plugin install realty-leads@realty-ai-agent-skills
```

Run those two inside Claude Code. Also install `realty-writing`, which the other skills use for client-facing text.
