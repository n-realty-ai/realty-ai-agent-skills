# Market and build reputation

Create content, collect reviews and stay in touch.

## Skills in this folder

One skill per job. Pick the job you need done.

### Market a listing

| Job to be done | Skill |
|---|---|
| Write the MLS description for one home | [listing-description](skills/listing-description/SKILL.md) |
| Announce one new listing on social media | [just-listed-social-posts](skills/just-listed-social-posts/SKILL.md) |
| Email your database about one new listing | [just-listed-email](skills/just-listed-email/SKILL.md) |
| Promote one open house | [open-house-promo](skills/open-house-promo/SKILL.md) |
| Script a walkthrough video for one listing | [listing-video-script](skills/listing-video-script/SKILL.md) |
| Make the one-page feature sheet for showings | [property-feature-sheet](skills/property-feature-sheet/SKILL.md) |
| Announce a price change on one listing | [price-change-announcement](skills/price-change-announcement/SKILL.md) |
| Announce one sale | [just-sold-post](skills/just-sold-post/SKILL.md) |

### Publish local content

| Job to be done | Skill |
|---|---|
| Write a guide to one neighbourhood | [neighbourhood-guide](skills/neighbourhood-guide/SKILL.md) |
| Report one month of local market numbers | [market-update-post](skills/market-update-post/SKILL.md) |
| Write a blog post answering one client question | [client-question-blog-post](skills/client-question-blog-post/SKILL.md) |
| Update one old blog post | [blog-post-refresh](skills/blog-post-refresh/SKILL.md) |
| Write one Google Business Profile update | [google-business-profile-post](skills/google-business-profile-post/SKILL.md) |
| Script one short advice video from a voice note | [short-video-script](skills/short-video-script/SKILL.md) |
| Write one monthly client newsletter | [client-newsletter](skills/client-newsletter/SKILL.md) |
| Plan next week of posts | [weekly-content-calendar](skills/weekly-content-calendar/SKILL.md) |
| Write one agent bio | [agent-bio](skills/agent-bio/SKILL.md) |

### Build reputation and stay in touch

| Job to be done | Skill |
|---|---|
| Ask a client for an honest review | [review-request](skills/review-request/SKILL.md) |
| Reply to one online review | [review-reply](skills/review-reply/SKILL.md) |
| Turn one closing into a client story | [client-story](skills/client-story/SKILL.md) |
| Draft home anniversary notes for past clients | [past-client-anniversary-note](skills/past-client-anniversary-note/SKILL.md) |

### Check and measure

| Job to be done | Skill |
|---|---|
| Check one ad before it is published | [ad-precheck](skills/ad-precheck/SKILL.md) |
| Review where good and poor leads came from | [lead-source-quality](skills/lead-source-quality/SKILL.md) |

## Workflows

Full instructions are in [workflows.md](workflows.md). Core workflows are the ones to start with.

| ID | Workflow | Priority | Use if | Our skill | Existing skill |
|---|---|---|---|---|---|
| N8 | [Video script and repurpose pack](workflows.md#n8) | Core | making content eats your week | [short-video-script](skills/short-video-script/SKILL.md) | [social](https://github.com/coreyhaines31/marketingskills/tree/2bf95edb4ebd37198ab7fd18b99ba95c2145ec64/skills/social), [video](https://github.com/coreyhaines31/marketingskills/tree/2bf95edb4ebd37198ab7fd18b99ba95c2145ec64/skills/video) |
| C1 | [Closing-triggered review request](workflows.md#c1) | Core | a deal just closed | [review-request](skills/review-request/SKILL.md) | [review-reputation](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/small-business/skills/review-reputation), [referrals](https://github.com/coreyhaines31/marketingskills/tree/2bf95edb4ebd37198ab7fd18b99ba95c2145ec64/skills/referrals) |
| M3 | [Weekly content and profile queue](workflows.md#m3) | Core | your content or profiles are going stale | [weekly-content-calendar](skills/weekly-content-calendar/SKILL.md), [google-business-profile-post](skills/google-business-profile-post/SKILL.md) | [social](https://github.com/coreyhaines31/marketingskills/tree/2bf95edb4ebd37198ab7fd18b99ba95c2145ec64/skills/social), [social-content-engine](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/small-business/skills/social-content-engine) |
| F4 | [Anniversary and life-event touches](workflows.md#f4) | Add when needed | past clients are not hearing from you | [past-client-anniversary-note](skills/past-client-anniversary-note/SKILL.md) | [buyer-nurture-sequence](https://github.com/SkillMedev/real-estate-agent-stack/tree/d0216171dd74239720abe8bc24854bd9884b7024/skills/buyer-nurture-sequence), [emails](https://github.com/coreyhaines31/marketingskills/tree/2bf95edb4ebd37198ab7fd18b99ba95c2145ec64/skills/emails) |
| K2 | [Advertising pre-flight](workflows.md#k2) | Add when needed | you are about to publish an ad | [ad-precheck](skills/ad-precheck/SKILL.md) | [fair-housing-overlay](https://github.com/TheProsperityAgent/prosperity-real-estate-skills/tree/b262bb92dea1bedac11b139bf1790496df739ea3/skills/fair-housing-overlay), [compliance-audit](https://github.com/hoangtng/real-estate-agents/tree/b35e143e0806050ff94f522b36eb3af82df1c00a/skills/compliance-audit), [brand-review](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/marketing/skills/brand-review) |
| O3 | [Lead quality digest](workflows.md#o3) | Add when needed | lead quality is poor | [lead-source-quality](skills/lead-source-quality/SKILL.md) | [lead-triage](https://github.com/anthropics/knowledge-work-plugins/tree/5e504ae11498f2b8daa30d86b7dab97b2ecd8092/sales/skills/lead-triage) |

## Notes on existing skills

- K2: US fair-housing focus: check local rules.

## Install

```bash
/plugin marketplace add n-realty-ai/realty-ai-agent-skills
```

```bash
/plugin install realty-marketing@realty-ai-agent-skills
```

Run those two inside Claude Code. Also install `realty-writing`, which these skills use for client-facing text.
