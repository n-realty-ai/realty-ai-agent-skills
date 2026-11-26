# Win and launch listings

Prepare the appointment, publish accurate listings and update sellers.

## Skills in this folder

One skill per job. Pick the job you need done.

| Job to be done | Skill |
|---|---|
| Plan a showing route for one client | [showing-route-planner](skills/showing-route-planner/SKILL.md) |
| Schedule the vendors that prepare one listing | [pre-listing-vendor-schedule](skills/pre-listing-vendor-schedule/SKILL.md) |
| Collect missing showing feedback | [showing-feedback-chaser](skills/showing-feedback-chaser/SKILL.md) |
| Check one listing draft against its source documents | [listing-precheck](skills/listing-precheck/SKILL.md) |

## Skills used from other jobs

Listing marketing lives in [Market and build reputation](../marketing/README.md): description, social posts, email, open house, video, feature sheet, price change and just sold.

## Workflows

Full instructions are in [workflows.md](workflows.md). Core workflows are the ones to start with.

| ID | Workflow | Priority | Use if | Our skill | Existing skill |
|---|---|---|---|---|---|
| N1 | [CMA first draft from your comps](workflows.md#n1) | Core | you have a listing appointment coming up | - | [seller-cma](https://github.com/axelrivera/real-estate-skills/tree/8ab189ab59fc4496631eca42c362fa1e69c87a44/skills/seller-cma), [buyer-cma](https://github.com/axelrivera/real-estate-skills/tree/8ab189ab59fc4496631eca42c362fa1e69c87a44/skills/buyer-cma), [cma-generator](https://github.com/hoangtng/real-estate-agents/tree/b35e143e0806050ff94f522b36eb3af82df1c00a/skills/cma-generator), [cma-narrative-builder](https://github.com/SkillMedev/real-estate-agent-stack/tree/d0216171dd74239720abe8bc24854bd9884b7024/skills/cma-narrative-builder) |
| M1 | [One intake, full listing pack](workflows.md#m1) | Core | you just won a listing | [listing-description](../marketing/skills/listing-description/SKILL.md), [just-listed-social-posts](../marketing/skills/just-listed-social-posts/SKILL.md), [just-listed-email](../marketing/skills/just-listed-email/SKILL.md), [open-house-promo](../marketing/skills/open-house-promo/SKILL.md) | [listing-description](https://github.com/TheProsperityAgent/prosperity-real-estate-skills/tree/b262bb92dea1bedac11b139bf1790496df739ea3/skills/listing-description), [listing-description](https://github.com/polytheseus/real-estate-skills/tree/91df95c7e9c57c2b65456ffbc0b050873af09310/skills/listing-description), [fair-housing-overlay](https://github.com/TheProsperityAgent/prosperity-real-estate-skills/tree/b262bb92dea1bedac11b139bf1790496df739ea3/skills/fair-housing-overlay), [property-marketing-plan](https://github.com/hoangtng/real-estate-agents/tree/b35e143e0806050ff94f522b36eb3af82df1c00a/skills/property-marketing-plan) |
| BO14 | [Listing data pre-check](workflows.md#bo14) | Core | a listing is about to go live | [listing-precheck](skills/listing-precheck/SKILL.md) | - |
| M2 | [Weekly seller update](workflows.md#m2) | Core | a seller expects a weekly report | - | [status-report](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/operations/skills/status-report) |
| A2 | [Showing coordination assistant](workflows.md#a2) | Add when needed | you need to book showings | [showing-route-planner](skills/showing-route-planner/SKILL.md) | - |
| N9 | [Pre-listing vendor scheduler](workflows.md#n9) | Add when needed | a listing needs preparing before it goes live | [pre-listing-vendor-schedule](skills/pre-listing-vendor-schedule/SKILL.md) | - |
| N3 | [Showing feedback chaser](workflows.md#n3) | Add when needed | showings are happening but feedback is missing | [showing-feedback-chaser](skills/showing-feedback-chaser/SKILL.md) | - |

## Notes on existing skills

- N1: These suggest a price or range; our sheet does not. You own the price.
- M1: Run output through plain-writing.
- M2: Generic report skill: paste our instruction.

## Install

```bash
/plugin marketplace add n-realty-ai/realty-ai-agent-skills
```

```bash
/plugin install realty-listings@realty-ai-agent-skills
```

Run those two inside Claude Code. Also install `realty-writing`, which the other skills use for client-facing text.
