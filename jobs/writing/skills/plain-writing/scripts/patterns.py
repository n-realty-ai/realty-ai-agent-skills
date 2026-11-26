"""One source of truth for the AI writing pattern catalog and the checker.
Each entry: id, group, name, looks like, fix, severity (1 fix now, 2 fix before publishing, 3 judgment/polish), regexes.
An empty regex list means a person (or Claude) has to judge it."""
G = {'A': 'Staging instead of stating', 'B': 'Rhythm by rule', 'C': 'Stock vocabulary', 'D': 'Inflation and borrowed authority',
     'E': 'Formatting by rule', 'F': 'Chat and drafting leftovers', 'G': 'Wrong reader and false voice'}
P = []
def p(i, name, looks, fix, sev, *rx): P.append(dict(id=i, group=i[0], name=name, looks=looks, fix=fix, sev=sev, rx=list(rx)))

p('A1', 'Not X but Y', 'Denies a framing nobody offered, then supplies the "real" one: "It\'s not just a CRM, it\'s a growth engine."', 'State the claim directly.', 1,
  r"\b(it|this|that)(['’]s| is| was)?n?['’]?t? (not )?(just|only|merely|simply|about)\b[^.?!\n]{0,80}?[,;:.—-]\s*(it|this|that)(['’]s| is)\b", r"\bnot (just|only|merely|simply) [^.?!\n]{1,60}?,? but\b", r"\bis(n['’]t| not) (a|an|the|about) [^.?!\n]{1,60}?[.;]\s*(It|This)(['’]s| is)\b")
p('A2', 'Negation list', '"No fluff. No jargon. Just results."', 'Say what the thing does.', 1, r"\bNo [a-z][\w -]{1,25}[.,] No [a-z][\w -]{1,25}[.,]")
p('A3', 'Punchline closer or dramatic fragment', 'A short line that repeats the paragraph for effect: "That changes everything."', 'Delete it, or fold the one new fact into the paragraph.', 2,
  r"\b(That changes everything|Full stop|Let that sink in|And that matters|Game over|Simple as that)\b")
p('A4', 'Saying that sounds deep', 'A quotable line with no checkable content: "Consistency is the currency of trust."', 'Replace with the concrete point or cut it.', 3, r"\b\w+ is the (new )?(currency|language|backbone|engine|heartbeat|fuel) of\b")
p('A5', 'Run-up before the point', '"Here\'s the thing", "Let\'s dive in", "The best part?"', 'Start with the point.', 1,
  r"\b(here['’]?s (the (thing|truth|kicker|deal|part)|why|what you need to know)|let['’]?s (dive|delve|jump) (in|into)|let['’]?s (explore|break (it|this) down|unpack)|without further ado|buckle up)\b", r"\bthe (best|worst|crazy|surprising) part\?")
p('A6', 'Self-answered rhetorical question', '"The result? More showings."', 'Make it a statement.', 2, r"\b(The (result|catch|solution|answer|reason|upshot)|Why does this matter|Sound familiar|The good news)\?")
p('A7', 'Arguing with no one', 'Sets up an unnamed opponent: "Some may say...", "Forget everything you know."', 'Answer only objections someone actually raised.', 2, r"\b(some (may|might|would) (say|argue)|you might be (thinking|wondering)|forget everything|contrary to popular belief|most people (think|get this wrong))\b")
p('A8', 'Performed candor', '"Let\'s be honest", "Real talk", "To be transparent".', 'Delete the announcement and say the thing.', 2, r"\b(let['’]?s be (honest|real|clear)|real talk|if i['’]?m being honest|the honest (truth|answer) is|in the interest of full disclosure|i would rather flag)\b")
p('A9', 'Borrowed excitement', '"This one is worth your time", "thank me later", "I can\'t stop thinking about this".', 'Give the reason it is useful.', 2, r"\b(worth your time|thank me later|can['’]?t stop thinking about|keep coming back to|you won['’]?t want to miss|this is huge)\b")
p('A10', 'Formula opener', '"In today\'s fast-paced real estate market".', 'Open with the reader\'s problem or the fact.', 1, r"\b(in today['’]?s [\w -]{0,30}(world|market|landscape|age|environment)|in (the|an) (ever[- ]?(evolving|changing)|rapidly (evolving|changing))|in a world where|now more than ever|gone are the days|picture this|imagine a world)\b")

p('B1', 'Forced triad', 'Three items because three sounds complete: "faster, smarter, and better".', 'List as many items as there are.', 3, r"\b\w+er, \w+er,? and \w+er\b", r"\b(seamless|simple|fast|powerful|smart),? (seamless|simple|fast|powerful|smart),? and (seamless|simple|fast|powerful|smart)\b")
p('B2', 'Repeated sentence openings', 'Consecutive sentences start the same way.', 'Merge them or change the subject. (Checked by code.)', 3)
p('B3', 'Uniform rhythm', 'Sentences and paragraphs all about the same length.', 'Let length follow the content. (Checked by code.)', 3)
p('B4', 'Dashes as universal connector', 'Em dashes, spaced en dashes or double hyphens joining clauses. House style: none.', 'Use a period, comma, colon or parentheses.', 1, r"—", r" – ", r"(?<=\w) -- (?=\w)")
p('B5', 'Stacked hedges', '"could potentially", "may possibly", "generally tends to".', 'Keep one hedge, only where you are unsure.', 2, r"\b(could|may|might) (potentially|possibly|perhaps|eventually)\b", r"\b(generally|typically|often) tends? to\b")
p('B6', 'Hyphenated pair stacking', 'Several compound modifiers in a row: "data-driven, client-centric, results-oriented".', 'Name what it does.', 3, r"\b\w+-(driven|centric|oriented|focused|powered|first|enabled|ready),? (and )?\w+-(driven|centric|oriented|focused|powered|first|enabled|ready)\b")
p('B7', 'Missing actor', 'Passive or subjectless lines hide who does what: "Mistakes can be avoided."', 'Name who acts.', 3)
p('B8', 'Synonym cycling', 'One thing renamed each sentence (the home, the property, the residence, the abode).', 'Repeat the plain word.', 3)
p('B9', 'Chopped fragments', 'Sentences broken up to fake a human rhythm. "Fast. Simple. Done."', 'Write full sentences.', 2, r"(?:^|(?<=[.!?] ))(?:[A-Z][a-z]+\. ){2}[A-Z][a-z]+\.(?= |$)")

p('C1', 'Overused AI words', 'delve, tapestry, testament, underscore, pivotal, crucial, intricate, showcase, foster, garner, meticulous, vibrant, interplay, enduring, bolster, multifaceted, nuanced, paramount, realm.', 'Use the everyday word or give the fact.', 2,
  r"\b(delv(e|es|ed|ing)|tapestry|testament|underscor(e|es|ed|ing)|pivotal|crucial|intricat(e|ies|ely)|showcas(e|es|ed|ing)|foster(s|ed|ing)?|garner(s|ed|ing)?|meticulous(ly)?|vibrant|interplay|enduring|bolster(s|ed|ing)?|multifaceted|nuanced|paramount|realm)\b")
p('C2', 'Corporate power verbs', 'leverage, harness, unlock, elevate, empower, streamline, supercharge, revolutionize, transform your, robust, seamless, cutting-edge.', 'Say the action: use, save, send, check.', 2,
  r"\b(leverag(e|es|ed|ing)|harness(es|ed|ing)?|unlock(s|ed|ing)?|elevat(e|es|ed|ing)|empower(s|ed|ing)?|streamlin(e|es|ed|ing)|supercharg(e|es|ed|ing)|revolutioni[sz](e|es|ed|ing)|robust|seamless(ly)?|cutting[- ]edge|best[- ]in[- ]class|next[- ]level|transformative)\b")
p('C3', 'Avoiding is and has', '"serves as", "stands as", "boasts", "plays a role in".', 'Use is, are or has.', 2, r"\b(serves?|stands?|acts?|functions?) as (a|an|the)\b", r"\bboasts?\b", r"\bplays? (a|an) (\w+ )?role\b")
p('C4', 'Transition stacking', 'Moreover, Furthermore, Additionally, Notably, Ultimately at sentence starts.', 'Cut, or use "also" or "but".', 2, r"(?:^|[.!?]\s+)(Moreover|Furthermore|Additionally|Notably|Ultimately|Consequently|Importantly|Interestingly),")
p('C5', 'Empty intensifiers', '"truly", "genuinely", "actually", "real value", "quietly".', 'Delete the word.', 3, r"\b(truly|genuinely|incredibly|remarkably|quietly|deeply|real (value|results|impact))\b")
p('C6', 'Stock metaphors', 'landscape, journey, game changer, north star, roadmap to success, at the heart of, double down, move the needle.', 'Name the literal thing.', 2, r"\b(landscape|game[- ]chang(er|ing)|north star|(your|the) \w+ journey|at the heart of|double down|move the needle|secret sauce|in the trenches)\b")
p('C7', 'Moral words for things', '"an honest number", "a brave design".', 'Describe the property: accurate, complete, unusual.', 3)

p('D1', 'Inflated significance', '"marks a turning point", "is a testament to", "sets the stage".', 'Report what happened and its measured effect.', 2, r"\b(turning point|sets? the stage|indelible mark|deeply rooted|paradigm shift|new era|ever-evolving|reshap(e|es|ing) the)\b")
p('D2', 'Trailing -ing analysis', 'A clause tacked on to sound analytical: ", highlighting the importance of..."', 'End the sentence, or state the cause with evidence.', 2, r",\s+(highlighting|underscoring|emphasizing|showcasing|reflecting|ensuring|fostering|demonstrating|contributing to|paving the way)\b")
p('D3', 'Sales and listing cliches', 'nestled, stunning, breathtaking, must-see, dream home, look no further, won\'t last long, hidden gem, in the heart of.', 'Give the feature: size, distance, year, material.', 2, r"\b(nestled|stunning|breathtaking|must[- ]see|dream home|look no further|won['’]?t last( long)?|hidden gem|in the heart of|turnkey oasis|entertainer['’]?s dream)\b")
p('D4', 'Unnamed authority', '"Experts say", "studies show", "industry reports".', 'Name and link the source, or drop the claim.', 1, r"\b(experts? (say|agree|believe|argue|recommend)|studies (show|suggest|have shown)|research (shows|suggests)|industry (reports?|data) (show|suggest)|many (believe|argue)|it is widely (known|accepted))\b")
p('D5', 'Vague connection', '"associated with", "in connection with" where the link is unstated.', 'Say the relationship: owns, wrote, sold.', 3, r"\b(in connection with|has been associated with|connected with the)\b")
p('D6', 'Name-dropping coverage', 'Lists outlets or follower counts to imply importance.', 'Cite the one that supports a specific claim.', 3, r"\b(featured in (numerous|several|multiple)|strong (digital|social media) presence|independent coverage)\b")
p('D7', 'Challenges and outlook formula', '"Despite these challenges, the future looks bright."', 'Keep only specific risks and dated plans.', 2, r"\b(despite (these|its) challenges|future outlook|challenges and opportunities|the future (looks|is) bright|only time will tell)\b")
p('D8', 'Generic upbeat ending', '"Happy selling!", "The possibilities are endless."', 'End on the last useful fact or the next action.', 2, r"\b(possibilities are endless|the sky is the limit|happy selling|here['’]?s to your success|take your business to the next level)\b")
p('D9', 'False range', '"from first-time buyers to seasoned investors" used as filler.', 'Name who it is for.', 3, r"\bfrom (first[- ]time \w+|beginners?|novices?) to (seasoned|experienced|experts?)\b")
p('D10', 'Explanation without consequence', 'Describes why something matters without saying what changes.', 'Say what the reader should do or what happens.', 3, r"\bwhy (this|it) matters\b")

p('E1', 'Bold as decoration', 'Bold on many phrases in running text.', 'Bold a term only when a reader must find it. (Checked by code.)', 3)
p('E2', 'Inline-header bullets', 'Every bullet is "**Word:** sentence".', 'Use prose or a table when it reads better. (Checked by code.)', 3)
p('E3', 'Noun-phrase bullet stacks', 'Five or more bullets like "Seamless integration".', 'Write what each does, or merge.', 3)
p('E4', 'Title Case Headings', 'Every Word Of The Heading Capitalised.', 'Use sentence case. (Checked by code.)', 3)
p('E5', 'Emoji decoration', 'Emoji on headings or bullets.', 'Remove them.', 2, r"^\s*(#{1,6}|[-*])\s*[\U0001F300-\U0001FAFF✅✨⚡]")
p('E6', 'Curly quotes in plain text', 'Mixed or curly quotes pasted into plain fields. Weak signal on its own.', 'Use straight quotes where the system expects them.', 3, r"[“”]")
p('E7', 'Heading overload or echo', 'A heading every few lines, or a first sentence that repeats it.', 'Fewer headings; start with new information.', 3)
p('E8', 'Hashtag stuffing', 'A block of hashtags after a post.', 'Keep a few that people search.', 2, r"(#\w+\s+){4,}#\w+")
p('E9', 'Symbols in prose', 'Arrows or emoji used instead of words in sentences.', 'Write the words. Arrows are fine in diagrams and UI paths.', 3, r"[a-z] (→|=>) [a-z]")

p('F1', 'Chatbot residue', '"Certainly!", "I hope this helps", "As an AI language model".', 'Delete it.', 1, r"\b(i hope this (helps|email finds you well)|as an ai( language model)?|certainly!|absolutely!|here['’]?s (a|the) (revised|updated|rewritten) (version|draft))")
p('F2', 'Flattery', '"Great question!", "You\'re absolutely right."', 'Answer.', 1, r"\b(great question|excellent (question|point)|you['’]?re absolutely right|what a (great|fantastic) (idea|question))\b")
p('F3', 'Knowledge-limit disclaimers', '"As of my last update", "based on available information".', 'State the source and date, or say you could not check.', 1, r"\b(as of my (last|latest) (knowledge )?(update|training)|based on (the )?available information|(is|are) not (widely|publicly) documented)\b")
p('F4', 'Importance announcements', '"It\'s important to note", "It\'s worth mentioning".', 'Just state it.', 1, r"\b(it['’]?s|it is) (important|worth|crucial|essential) (to )?(note|noting|mention(ing)?|remember(ing)?|consider(ing)?)\b")
p('F5', 'Corrective disclaimers', '"This does not by itself establish...", "should be treated as..." added defensively.', 'Say the one limit that changes a decision.', 3, r"\b(does not (by itself|in itself) (establish|prove|mean)|should be treated as)\b")
p('F6', 'Writing about the document', '"In this article, we will explore".', 'Give the content.', 1, r"\bin this (article|post|guide|blog|section|document),? (we|i)['’]?(ll| will| are going to)\b", r"\bthis (article|guide|post) (will )?(explores?|delves?|covers? everything)\b")
p('F7', 'Summary restatement', '"In conclusion", "To sum up", "Overall,".', 'Stop after the last new point.', 2, r"(?:^|[.!?]\s+)(In conclusion|In summary|To sum up|To summarize|In essence|All in all|Overall,)")
p('F8', 'Offer-more closer', '"Would you like me to...", "Let me know if you want..."', 'Remove from finished copy.', 2, r"\b(would you like me to|let me know if you(['’]d| would)? (like|want|need)|feel free to reach out)\b")
p('F9', 'Unfilled placeholders', '[Your Name], [link], INSERT_URL, 2026-XX-XX.', 'Fill or remove before sending.', 1, r"\[(your|client|first|insert|company|agent|date|link|url)[^\]\n]{0,40}\]", r"\bINSERT_[A-Z_]+\b", r"\b20\d\d-XX-XX\b", r"\bLorem ipsum\b")
p('F10', 'Tool markup and tracking leftovers', 'oaicite tokens, utm_source=chatgpt.com, stray citation markers.', 'Strip them and verify the link.', 1, r"oaicite|contentReference|utm_source=(chatgpt\.com|openai|copilot\.com)|referrer=grok\.com|【\d+")
p('F11', 'Invented or broken references', 'Links, studies or quotes that do not exist or do not support the claim.', 'Open every link and confirm the claim.', 1)
p('F12', 'Cut-off text', 'Ends mid-sentence or mid-list.', 'Complete or trim.', 1)

p('G1', 'Explaining what the reader knows', 'Tells agents what a listing is.', 'Write for the person actually reading.', 3)
p('G2', 'Sudden voice change', 'Register shifts sharply from the author\'s samples.', 'Match a real sample.', 3)
p('G3', 'Invented experience or specifics', 'Adds "In my 10 years...", a client story or a number to sound human.', 'Never add facts or experiences the writer did not supply.', 1)
p('G4', 'Compliance reassurance', '"I have ensured this adheres to all guidelines."', 'Show what was checked, or say nothing.', 2, r"\bi(['’]ve| have) (ensured|made sure|carefully (reviewed|crafted))\b")
