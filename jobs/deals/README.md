# Move deals to closing

Track dates, chase documents and compare offers.

## Skills in this folder

One skill per job. Pick the job you need done.

| Job to be done | Skill |
|---|---|
| Confirm that an emailed offer arrived | [offer-receipt-confirmation](skills/offer-receipt-confirmation/SKILL.md) |
| Set up the checklist for a newly accepted deal | [deal-intake-checklist](skills/deal-intake-checklist/SKILL.md) |
| Alert the team when a signature request changes status | [signature-status-alert](skills/signature-status-alert/SKILL.md) |
| Chase missing documents on open deals | [missing-document-chaser](skills/missing-document-chaser/SKILL.md) |
| Draft a status update for a client in a deal | [client-status-update](skills/client-status-update/SKILL.md) |
| Check one file before broker review | [broker-review-precheck](skills/broker-review-precheck/SKILL.md) |
| Check identity records are complete | [id-record-check](skills/id-record-check/SKILL.md) |
| Sample closed files for audit readiness | [file-audit-sample](skills/file-audit-sample/SKILL.md) |
| Index a disclosure and HOA package | [disclosure-index](skills/disclosure-index/SKILL.md) |
| Turn an inspection report into a repair list | [inspection-repair-list](skills/inspection-repair-list/SKILL.md) |
| Compare multiple offers side by side | [offer-terms-table](skills/offer-terms-table/SKILL.md) |

## Workflows

Full instructions are in [workflows.md](workflows.md). Core workflows are the ones to start with.

| ID | Workflow | Priority | Use if | Our skill | Existing skill |
|---|---|---|---|---|---|
| T1 | [Deadline extractor and countdown](workflows.md#t1) | Core | you have a signed agreement | - | [contract-timeline](https://github.com/axelrivera/real-estate-skills/tree/8ab189ab59fc4496631eca42c362fa1e69c87a44/skills/contract-timeline), [transaction-timeline-manager](https://github.com/hoangtng/real-estate-agents/tree/b35e143e0806050ff94f522b36eb3af82df1c00a/skills/transaction-timeline-manager) |
| T2 | [Missing-document chaser](workflows.md#t2) | Core | a file is missing documents | [missing-document-chaser](skills/missing-document-chaser/SKILL.md) | - |
| N4 | [Multiple-offer comparison sheet](workflows.md#n4) | Core | more than one offer has arrived | [offer-terms-table](skills/offer-terms-table/SKILL.md) | [seller-offer-review](https://github.com/axelrivera/real-estate-skills/tree/8ab189ab59fc4496631eca42c362fa1e69c87a44/skills/seller-offer-review), [offer-comparison](https://github.com/polytheseus/real-estate-skills/tree/91df95c7e9c57c2b65456ffbc0b050873af09310/skills/offer-comparison) |
| C2 | [Client status update](workflows.md#c2) | Add when needed | an active client needs an update | [client-status-update](skills/client-status-update/SKILL.md) | - |
| K1 | [Transaction file pre-check](workflows.md#k1) | Add when needed | a file is ready for broker review | [broker-review-precheck](skills/broker-review-precheck/SKILL.md) | [compliance-audit](https://github.com/hoangtng/real-estate-agents/tree/b35e143e0806050ff94f522b36eb3af82df1c00a/skills/compliance-audit) |
| N5 | [Disclosure and HOA reading guide](workflows.md#n5) | Add when needed | a long disclosure or association package arrived | [disclosure-index](skills/disclosure-index/SKILL.md) | - |
| N6 | [Inspection report to repair list](workflows.md#n6) | Add when needed | the inspection report just came back | [inspection-repair-list](skills/inspection-repair-list/SKILL.md) | - |
| N10 | [Offer received confirmation](workflows.md#n10) | Add when needed | offers come in by email | [offer-receipt-confirmation](skills/offer-receipt-confirmation/SKILL.md) | - |
| BO1 | [Deal intake and checklist setup](workflows.md#bo1) | Add when needed | an offer was accepted | [deal-intake-checklist](skills/deal-intake-checklist/SKILL.md) | [transaction-timeline-manager](https://github.com/hoangtng/real-estate-agents/tree/b35e143e0806050ff94f522b36eb3af82df1c00a/skills/transaction-timeline-manager) |
| BO2 | [Signature status watcher](workflows.md#bo2) | Add when needed | documents are out for signature | [signature-status-alert](skills/signature-status-alert/SKILL.md) | - |
| BO12 | [ID and record completeness check](workflows.md#bo12) | Add when needed | you must confirm identity records are complete | [id-record-check](skills/id-record-check/SKILL.md) | [compliance-tracking](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/operations/skills/compliance-tracking) |
| BO13 | [File retention and audit readiness](workflows.md#bo13) | Add when needed | an audit is coming or files are closing | [file-audit-sample](skills/file-audit-sample/SKILL.md) | [audit-support](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/finance/skills/audit-support) |

## Notes on existing skills

- T1: Verify every date against the contract and local rules.
- N4: The existing ones recommend or rank offers.
- BO12: Existing one targets IT audits.
- BO13: Existing one targets financial control testing.

## Install

```bash
/plugin marketplace add n-realty-ai/realty-ai-agent-skills
```

```bash
/plugin install realty-deals@realty-ai-agent-skills
```

Run those two inside Claude Code. Also install `realty-writing`, which the other skills use for client-facing text.
