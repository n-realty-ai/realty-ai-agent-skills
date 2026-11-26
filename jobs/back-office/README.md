# Run the back office

Check commissions, close the month and catch expiries.

## Skills in this folder

- [brokerage-admin-checks](skills/brokerage-admin-checks/SKILL.md): Check brokerage administration, including agent offboarding handovers and access lists, licence, insurance and training expiry, and software subscription and seat audits.
- [brokerage-money-checks](skills/brokerage-money-checks/SKILL.md): Check brokerage money work, including commission breakdowns, deposit exceptions, receipt categories, agent fee billing previews, receivables, referral fees, month-end packs, owner briefs, tax slip data and expense logs.

## Skills used from other jobs

- [realty-event-automations](../leads/skills/realty-event-automations/SKILL.md)

## Workflows

Full instructions are in [workflows.md](workflows.md). Core workflows are the ones to start with.

| ID | Workflow | Priority | Use if | Our skill | Existing skill |
|---|---|---|---|---|---|
| BO3 | [Commission statement pre-check](workflows.md#bo3) | Core | a deal is closing and commission is due | [brokerage-money-checks](skills/brokerage-money-checks/SKILL.md) | - |
| BO7 | [Month-end close pack](workflows.md#bo7) | Core | the month has ended | [brokerage-money-checks](skills/brokerage-money-checks/SKILL.md) | [close-month](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/small-business/skills/close-month), [month-end-prep](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/small-business/skills/month-end-prep), [variance-analysis](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/finance/skills/variance-analysis) |
| BO11 | [Expiry tracker](workflows.md#bo11) | Core | you track licences and training | [brokerage-admin-checks](skills/brokerage-admin-checks/SKILL.md) | - |
| BO4 | [Deposit exception list](workflows.md#bo4) | Add when needed | you are checking deposits | [brokerage-money-checks](skills/brokerage-money-checks/SKILL.md) | [reconciliation](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/finance/skills/reconciliation) |
| BO5 | [Receipt capture and categorising](workflows.md#bo5) | Add when needed | receipts are piling up | [brokerage-money-checks](skills/brokerage-money-checks/SKILL.md) | [ap-processor](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/small-business/skills/ap-processor), [month-end-prep](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/small-business/skills/month-end-prep) |
| BO6 | [Agent fee billing run](workflows.md#bo6) | Add when needed | it is time to bill agent fees | [brokerage-money-checks](skills/brokerage-money-checks/SKILL.md) | - |
| B2 | [Receivables and renewal reminders](workflows.md#b2) | Add when needed | invoices or renewals are overdue | [brokerage-money-checks](skills/brokerage-money-checks/SKILL.md) | [invoice-chase](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/small-business/skills/invoice-chase) |
| BO17 | [Referral agreement tracker](workflows.md#bo17) | Add when needed | a referral is involved | [brokerage-money-checks](skills/brokerage-money-checks/SKILL.md) | - |
| BO8 | [Tax slip data checker](workflows.md#bo8) | Add when needed | tax slips are coming up | [brokerage-money-checks](skills/brokerage-money-checks/SKILL.md) | [tax-season-organizer](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/small-business/skills/tax-season-organizer) |
| BO19 | [Expense and mileage log](workflows.md#bo19) | Add when needed | you need to log expenses | [brokerage-money-checks](skills/brokerage-money-checks/SKILL.md) | - |
| BO9 | [Agent onboarding orchestrator](workflows.md#bo9) | Add when needed | a new agent signed | [realty-event-automations](../leads/skills/realty-event-automations/SKILL.md) | [onboarding](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/human-resources/skills/onboarding) |
| BO10 | [Offboarding checklist and access review](workflows.md#bo10) | Add when needed | an agent is leaving | [brokerage-admin-checks](skills/brokerage-admin-checks/SKILL.md) | - |
| BO15 | [Office request triage](workflows.md#bo15) | Add when needed | office requests are getting lost | [realty-event-automations](../leads/skills/realty-event-automations/SKILL.md) | [ticket-triage](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/customer-support/skills/ticket-triage) |
| BO16 | [Subscription and seat audit](workflows.md#bo16) | Add when needed | software costs are creeping up | [brokerage-admin-checks](skills/brokerage-admin-checks/SKILL.md) | [vendor-review](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/operations/skills/vendor-review) |
| F3 | [Weekly duplicate and data cleanup report](workflows.md#f3) | Add when needed | your CRM is full of duplicates and gaps | - | [crm-hygiene-check](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/sales/skills/crm-hygiene-check) |

## Notes on existing skills

- BO8: US federal focus.
- BO15: Existing one is for customer support tickets.
- F3: Checks opportunities; ask it to cover contacts and duplicates.

## Install

```bash
/plugin marketplace add n-realty-ai/realty-ai-agent-skills
```

```bash
/plugin install realty-back-office@realty-ai-agent-skills
```

Run those two inside Claude Code. Also install `realty-writing`, which the other skills use for client-facing text.
