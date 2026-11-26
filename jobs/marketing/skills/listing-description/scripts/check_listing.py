#!/usr/bin/env python3
"""Check a listing description. Usage: check_listing.py FILE [--limit CHARACTERS]  (FILE '-' reads stdin)
Counts characters and flags wording to review. It is a prompt to read, not a fair housing or MLS review:
a clean result does not make a description compliant. Standard library only. Exit code 1 if anything is flagged."""
import argparse, re, sys

CHECKS = [
    ('Who should live there', r'\b(perfect|ideal|great|suited)\s+for\s+(a\s+)?(young\s+)?(famil\w+|couples?|singles?|professionals?|retirees?|seniors?|students?|bachelors?|empty[- ]nesters?)'),
    ('Who should live there', r'\b(family[- ](friendly|neighbou?rhood)|adults? only|no (kids|children)|bachelor pad|christian|exclusive (community|neighbou?rhood))\b'),
    ('Safety or school judgment', r'\b(safe|quiet,? safe|low[- ]crime)\s+(area|neighbou?rhood|street|community)\b|\b(best|top|great|excellent|good)[- ](rated )?schools?\b'),
    ('Empty or hype wording', r"\b(must[- ]see|don'?t miss|won'?t last|nestled|boasts?|stunning|breathtaking|turn[- ]?key|dream home|hidden gem|one of a kind)\b"),
    ('Promise needing proof', r'\b(great investment|guaranteed|will appreciate|income potential|legal suite)\b'),
    ('Contact detail or link', r'(\(?\b\d{3}\)?[-. ]\d{3}[-. ]\d{4}\b|https?://\S+|www\.\S+|\b[\w.+-]+@[\w-]+\.\w+)'),
    ('All capitals', r'\b[A-Z]{4,}(\s+[A-Z]{2,})+\b'),
    ('Repeated punctuation', r'[!?]{2,}'),
]

def check(text, limit=None):
    text = text.strip()
    out = []
    if limit is not None and len(text) > limit:
        out.append(('Over the limit', f'{len(text) - limit} characters too long'))
    for name, rx in CHECKS:
        flags = 0 if name == 'All capitals' else re.I
        out += [(name, m.group(0)) for m in re.finditer(rx, text, flags)]
    return out

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('file'); ap.add_argument('--limit', type=int)
    a = ap.parse_args()
    text = sys.stdin.read() if a.file == '-' else open(a.file, encoding='utf-8', errors='replace').read()
    found = check(text, a.limit)
    print(f'{len(text.strip())} characters' + (f' of {a.limit}' if a.limit else ' (no limit given)') + f', {len(found)} to review')
    for name, snippet in found:
        print(f'  {name}: "{snippet}"')
    sys.exit(1 if found else 0)

if __name__ == '__main__':
    main()
