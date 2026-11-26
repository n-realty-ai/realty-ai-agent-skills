# Realty AI agent skills

Claude skills and workflow instructions for real estate agents, teams and brokerages, grouped by the job to be done.

61 workflows, 26 marked core, and 65 skills.

| Job | What it covers | Workflows | Core | Skills here |
|---|---|---|---|---|
| [Win and follow up leads](jobs/leads/README.md) | Answer new inquiries fast and keep every lead moving. | 7 | 5 | [5 skills](jobs/leads/README.md#skills-in-this-folder) |
| [Run your day](jobs/day-to-day/README.md) | Know what matters, clear the inbox and record what happened. | 6 | 4 | Uses existing skills |
| [Win and launch listings](jobs/listings/README.md) | Prepare the appointment, publish accurate listings and update sellers. | 7 | 4 | [4 skills](jobs/listings/README.md#skills-in-this-folder) |
| [Market and build reputation](jobs/marketing/README.md) | Create content, collect reviews and stay in touch. | 6 | 3 | [23 skills](jobs/marketing/README.md#skills-in-this-folder) |
| [Move deals to closing](jobs/deals/README.md) | Track dates, chase documents and compare offers. | 12 | 3 | [11 skills](jobs/deals/README.md#skills-in-this-folder) |
| [Lead your team](jobs/team-leadership/README.md) | Check lead handling, see the weekly numbers and answer agent questions. | 8 | 4 | [7 skills](jobs/team-leadership/README.md#skills-in-this-folder) |
| [Run the back office](jobs/back-office/README.md) | Check commissions, close the month and catch expiries. | 15 | 3 | [14 skills](jobs/back-office/README.md#skills-in-this-folder) |
| [Plain writing](jobs/writing/README.md) | Shared across every job | - | - | [plain-writing](jobs/writing/skills/plain-writing/SKILL.md) |

## Install in Claude Code

Add the marketplace, then install the jobs you need.

```bash
/plugin marketplace add n-realty-ai/realty-ai-agent-skills
```

```bash
/plugin install realty-writing@realty-ai-agent-skills
```

Plugin names: `realty-leads`, `realty-listings`, `realty-marketing`, `realty-deals`, `realty-team-leadership`, `realty-back-office`, `realty-writing`.

To use one skill without plugins, copy its folder into `~/.claude/skills/`.

## Before you use these

- No workflow has been tested on real work. The script tests use made-up data.
- Keep a person in control of anything that sends, pays, files, books or approves.
- Get brokerage approval before connecting client information, and check consent, do-not-call, MLS, privacy and fair housing rules where you operate.
- Nothing here is legal, financial or tax advice.
- Tool plans and features change. Confirm them with the vendor.

## More

- [Third-party skills we link to](docs/third-party-skills.md)
- [AI writing patterns to avoid](docs/ai-writing-patterns.md)
- [Workflow to skill map (CSV)](docs/workflow-skill-map.csv)

## Run the script tests

```bash
python3 tests/test_skills.py
```

## License

[MIT](LICENSE). Third-party repositories linked from here have their own licenses.
