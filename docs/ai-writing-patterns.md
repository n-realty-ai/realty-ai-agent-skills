# AI writing patterns to avoid

**Skill that prevents these:** [plain-writing](../jobs/writing/skills/plain-writing/SKILL.md). It sets drafting rules and runs a checker before anything is delivered.

```bash
python3 jobs/writing/skills/plain-writing/scripts/check_writing.py your-draft.md
```

61 patterns in 7 groups. "Script" means check_writing.py flags at least some cases; "judge by reading" means it cannot. Severity: 1 fix now, 2 fix before publishing, 3 your judgment.

Sources: compiled in our own words from [blader/humanizer](https://github.com/blader/humanizer) (MIT), [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) (MIT), Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (read in part) and real estate copy examples added here. No list of this kind is complete, and the habits change as models change.

These signs do not prove a machine wrote something. Wikipedia warns against relying on them or on AI detectors alone.

## A. Staging instead of stating

| ID | Pattern | What it looks like | Do this instead | Severity | Detection |
|---|---|---|---|---|---|
| A1 | Not X but Y | Denies a framing nobody offered, then supplies the "real" one: "It's not just a CRM, it's a growth engine." | State the claim directly. | 1 | Script |
| A2 | Negation list | "No fluff. No jargon. Just results." | Say what the thing does. | 1 | Script |
| A3 | Punchline closer or dramatic fragment | A short line that repeats the paragraph for effect: "That changes everything." | Delete it, or fold the one new fact into the paragraph. | 2 | Script |
| A4 | Saying that sounds deep | A quotable line with no checkable content: "Consistency is the currency of trust." | Replace with the concrete point or cut it. | 3 | Script |
| A5 | Run-up before the point | "Here's the thing", "Let's dive in", "The best part?" | Start with the point. | 1 | Script |
| A6 | Self-answered rhetorical question | "The result? More showings." | Make it a statement. | 2 | Script |
| A7 | Arguing with no one | Sets up an unnamed opponent: "Some may say...", "Forget everything you know." | Answer only objections someone actually raised. | 2 | Script |
| A8 | Performed candor | "Let's be honest", "Real talk", "To be transparent". | Delete the announcement and say the thing. | 2 | Script |
| A9 | Borrowed excitement | "This one is worth your time", "thank me later", "I can't stop thinking about this". | Give the reason it is useful. | 2 | Script |
| A10 | Formula opener | "In today's fast-paced real estate market". | Open with the reader's problem or the fact. | 1 | Script |

## B. Rhythm by rule

| ID | Pattern | What it looks like | Do this instead | Severity | Detection |
|---|---|---|---|---|---|
| B1 | Forced triad | Three items because three sounds complete: "faster, smarter, and better". | List as many items as there are. | 3 | Script |
| B2 | Repeated sentence openings | Consecutive sentences start the same way. | Merge them or change the subject. | 3 | Script |
| B3 | Uniform rhythm | Sentences and paragraphs all about the same length. | Let length follow the content. | 3 | Script |
| B4 | Dashes as universal connector | Em dashes, spaced en dashes or double hyphens joining clauses. House style: none. | Use a period, comma, colon or parentheses. | 1 | Script |
| B5 | Stacked hedges | "could potentially", "may possibly", "generally tends to". | Keep one hedge, only where you are unsure. | 2 | Script |
| B6 | Hyphenated pair stacking | Several compound modifiers in a row: "data-driven, client-centric, results-oriented". | Name what it does. | 3 | Script |
| B7 | Missing actor | Passive or subjectless lines hide who does what: "Mistakes can be avoided." | Name who acts. | 3 | Judge by reading |
| B8 | Synonym cycling | One thing renamed each sentence (the home, the property, the residence, the abode). | Repeat the plain word. | 3 | Judge by reading |
| B9 | Chopped fragments | Sentences broken up to fake a human rhythm. "Fast. Simple. Done." | Write full sentences. | 2 | Script |

## C. Stock vocabulary

| ID | Pattern | What it looks like | Do this instead | Severity | Detection |
|---|---|---|---|---|---|
| C1 | Overused AI words | delve, tapestry, testament, underscore, pivotal, crucial, intricate, showcase, foster, garner, meticulous, vibrant, interplay, enduring, bolster, multifaceted, nuanced, paramount, realm. | Use the everyday word or give the fact. | 2 | Script |
| C2 | Corporate power verbs | leverage, harness, unlock, elevate, empower, streamline, supercharge, revolutionize, transform your, robust, seamless, cutting-edge. | Say the action: use, save, send, check. | 2 | Script |
| C3 | Avoiding is and has | "serves as", "stands as", "boasts", "plays a role in". | Use is, are or has. | 2 | Script |
| C4 | Transition stacking | Moreover, Furthermore, Additionally, Notably, Ultimately at sentence starts. | Cut, or use "also" or "but". | 2 | Script |
| C5 | Empty intensifiers | "truly", "genuinely", "actually", "real value", "quietly". | Delete the word. | 3 | Script |
| C6 | Stock metaphors | landscape, journey, game changer, north star, roadmap to success, at the heart of, double down, move the needle. | Name the literal thing. | 2 | Script |
| C7 | Moral words for things | "an honest number", "a brave design". | Describe the property: accurate, complete, unusual. | 3 | Judge by reading |

## D. Inflation and borrowed authority

| ID | Pattern | What it looks like | Do this instead | Severity | Detection |
|---|---|---|---|---|---|
| D1 | Inflated significance | "marks a turning point", "is a testament to", "sets the stage". | Report what happened and its measured effect. | 2 | Script |
| D2 | Trailing -ing analysis | A clause tacked on to sound analytical: ", highlighting the importance of..." | End the sentence, or state the cause with evidence. | 2 | Script |
| D3 | Sales and listing cliches | nestled, stunning, breathtaking, must-see, dream home, look no further, won't last long, hidden gem, in the heart of. | Give the feature: size, distance, year, material. | 2 | Script |
| D4 | Unnamed authority | "Experts say", "studies show", "industry reports". | Name and link the source, or drop the claim. | 1 | Script |
| D5 | Vague connection | "associated with", "in connection with" where the link is unstated. | Say the relationship: owns, wrote, sold. | 3 | Script |
| D6 | Name-dropping coverage | Lists outlets or follower counts to imply importance. | Cite the one that supports a specific claim. | 3 | Script |
| D7 | Challenges and outlook formula | "Despite these challenges, the future looks bright." | Keep only specific risks and dated plans. | 2 | Script |
| D8 | Generic upbeat ending | "Happy selling!", "The possibilities are endless." | End on the last useful fact or the next action. | 2 | Script |
| D9 | False range | "from first-time buyers to seasoned investors" used as filler. | Name who it is for. | 3 | Script |
| D10 | Explanation without consequence | Describes why something matters without saying what changes. | Say what the reader should do or what happens. | 3 | Script |

## E. Formatting by rule

| ID | Pattern | What it looks like | Do this instead | Severity | Detection |
|---|---|---|---|---|---|
| E1 | Bold as decoration | Bold on many phrases in running text. | Bold a term only when a reader must find it. | 3 | Script |
| E2 | Inline-header bullets | Every bullet is "**Word:** sentence". | Use prose or a table when it reads better. | 3 | Script |
| E3 | Noun-phrase bullet stacks | Five or more bullets like "Seamless integration". | Write what each does, or merge. | 3 | Judge by reading |
| E4 | Title Case Headings | Every Word Of The Heading Capitalised. | Use sentence case. | 3 | Script |
| E5 | Emoji decoration | Emoji on headings or bullets. | Remove them. | 2 | Script |
| E6 | Curly quotes in plain text | Mixed or curly quotes pasted into plain fields. Weak signal on its own. | Use straight quotes where the system expects them. | 3 | Script |
| E7 | Heading overload or echo | A heading every few lines, or a first sentence that repeats it. | Fewer headings; start with new information. | 3 | Judge by reading |
| E8 | Hashtag stuffing | A block of hashtags after a post. | Keep a few that people search. | 2 | Script |
| E9 | Symbols in prose | Arrows or emoji used instead of words in sentences. | Write the words. Arrows are fine in diagrams and UI paths. | 3 | Script |

## F. Chat and drafting leftovers

| ID | Pattern | What it looks like | Do this instead | Severity | Detection |
|---|---|---|---|---|---|
| F1 | Chatbot residue | "Certainly!", "I hope this helps", "As an AI language model". | Delete it. | 1 | Script |
| F2 | Flattery | "Great question!", "You're absolutely right." | Answer. | 1 | Script |
| F3 | Knowledge-limit disclaimers | "As of my last update", "based on available information". | State the source and date, or say you could not check. | 1 | Script |
| F4 | Importance announcements | "It's important to note", "It's worth mentioning". | Just state it. | 1 | Script |
| F5 | Corrective disclaimers | "This does not by itself establish...", "should be treated as..." added defensively. | Say the one limit that changes a decision. | 3 | Script |
| F6 | Writing about the document | "In this article, we will explore". | Give the content. | 1 | Script |
| F7 | Summary restatement | "In conclusion", "To sum up", "Overall,". | Stop after the last new point. | 2 | Script |
| F8 | Offer-more closer | "Would you like me to...", "Let me know if you want..." | Remove from finished copy. | 2 | Script |
| F9 | Unfilled placeholders | [Your Name], [link], INSERT_URL, 2026-XX-XX. | Fill or remove before sending. | 1 | Script |
| F10 | Tool markup and tracking leftovers | oaicite tokens, utm_source=chatgpt.com, stray citation markers. | Strip them and verify the link. | 1 | Script |
| F11 | Invented or broken references | Links, studies or quotes that do not exist or do not support the claim. | Open every link and confirm the claim. | 1 | Judge by reading |
| F12 | Cut-off text | Ends mid-sentence or mid-list. | Complete or trim. | 1 | Judge by reading |

## G. Wrong reader and false voice

| ID | Pattern | What it looks like | Do this instead | Severity | Detection |
|---|---|---|---|---|---|
| G1 | Explaining what the reader knows | Tells agents what a listing is. | Write for the person actually reading. | 3 | Judge by reading |
| G2 | Sudden voice change | Register shifts sharply from the author's samples. | Match a real sample. | 3 | Judge by reading |
| G3 | Invented experience or specifics | Adds "In my 10 years...", a client story or a number to sound human. | Never add facts or experiences the writer did not supply. | 1 | Judge by reading |
| G4 | Compliance reassurance | "I have ensured this adheres to all guidelines." | Show what was checked, or say nothing. | 2 | Script |
