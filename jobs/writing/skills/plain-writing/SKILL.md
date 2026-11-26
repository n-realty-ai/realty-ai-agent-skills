---
name: plain-writing
description: Stop AI-sounding writing before it ships. Use whenever you draft, rewrite, edit or review anything a person will read, including emails, texts, listing descriptions, social posts, video scripts, blog posts, ad copy, reports, SEO and AEO audit write-ups and client updates, even if the user only says "write this" or "tidy this up". Also use when asked to remove AI-isms, humanize text, make something sound less like ChatGPT, or check a draft for AI patterns. Includes a catalog of the patterns and a script that flags them.
---

# Plain writing

Readers trust writing that says specific things in an ordinary way. Most "AI sound" comes from filling space: staging a point instead of stating it, reaching for stock words, and adding rhythm or emphasis the facts did not earn. The aim is clearer writing. Passing a detector is not the aim.

## While drafting

1. Know the reader, the one thing they should learn or do, and the facts you have. Write only from those facts.
2. Lead with the answer.
3. Prefer is, has, send, check, save over grander verbs.
4. Give the number, name, date or place. If you do not have it, say so or ask. Never invent one.
5. Use no em dashes. Use sentence-case headings. Add bold, bullets and headings only when they help someone find something.
6. If the writer gave a sample of their own writing, match its sentence length, word choice and openings.

## Before delivering

1. Save the draft to a file and run:
   `python3 scripts/check_writing.py draft.md`
2. Fix every severity 1 finding. Fix severity 2 unless the word is the accurate one here. Judge severity 3.
3. Read `references/patterns.md` and look for the patterns the script cannot detect (those marked "judge by reading"), especially invented specifics (G3) and unchecked references (F11).
4. Run the script again after editing. Rewrites often introduce a new pattern while removing an old one.

## Rewriting someone else's text

- Keep the meaning, facts, order of claims and the writer's stance. Subtract and sharpen.
- Do not add first-person experience, opinions, jokes, "honestly" or choppy fragments to sound human. That swaps one recognisable voice for another.
- Leave quotations, titles, proper names, legal wording and required disclosures unchanged, even if they match a pattern.
- If a vague sentence needs a fact you do not have, flag it for the writer instead of filling it.

## Reporting

Give the revised text first. Then, if useful, one short list: what you changed, and what the writer still has to supply or verify. In review-only requests, list findings with line numbers and change nothing.

## Limits

A pattern is evidence of weak writing, not proof of who wrote it. People use all of these on purpose sometimes, and a clean score does not make a text accurate. Do not use this skill to accuse a person of using AI.
