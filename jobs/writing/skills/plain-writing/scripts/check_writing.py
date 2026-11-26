#!/usr/bin/env python3
"""Flag AI-sounding writing patterns. Usage: check_writing.py FILE [FILE ...]  [--min-severity 1|2|3] [--json]
Reads stdin when FILE is '-'. Exit code 1 if any severity-1 finding. Standard library only.
A clean result does not prove a human wrote the text, and a finding does not prove a machine did."""
import argparse, json, re, statistics, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patterns import P
BY = {x['id']: x for x in P}

def strip(text):
    """Blank out code, URLs' query-free text and quoted blocks so they are not judged, keeping line numbers."""
    text = re.sub(r'```.*?```', lambda m: '\n' * m.group(0).count('\n'), text, flags=re.S)
    text = re.sub(r'`[^`\n]*`', ' ', text)
    return '\n'.join('' if l.lstrip().startswith('>') else l for l in text.split('\n'))

def check(text):
    body = strip(text); lines = body.split('\n'); out = []
    def add(pid, line, snippet): out.append(dict(id=pid, name=BY[pid]['name'], severity=BY[pid]['sev'], line=line, found=snippet.strip()[:90], fix=BY[pid]['fix']))
    for x in P:
        for rx in x['rx']:
            flags = 0 if x['id'] in ('A2', 'B9', 'C4', 'F7', 'F10') else re.I
            for n, l in enumerate(lines, 1):
                for m in re.finditer(rx, l, flags): add(x['id'], n, m.group(0))
    sents = []
    for n, l in enumerate(lines, 1):
        if re.match(r'\s*([#|>]|[-*+] |\d+\. )', l) or not l.strip(): sents.append(None); continue
        sents += [(n, s) for s in re.split(r'(?<=[.!?])\s+', l.strip()) if s]
    run = []
    for s in sents + [None]:
        w = s[1].split()[0].lower().strip('"\'') if s and s[1].split() else None
        if run and w != run[0][0]:
            if len(run) >= 3: add('B2', run[0][1], f'{len(run)} sentences start with "{run[0][0]}"')
            run = []
        if w: run.append((w, s[0]))
    L = [len(s[1].split()) for s in sents if s]
    if len(L) >= 12 and statistics.pstdev(L) / max(statistics.mean(L), 1) < 0.25: add('B3', 1, f'{len(L)} sentences, average {statistics.mean(L):.0f} words, very little variation')
    words = len(re.findall(r'\w+', body)) or 1
    bold = len(re.findall(r'\*\*[^*\n]+\*\*', body))
    if bold >= 6 and bold / words * 100 > 2: add('E1', 1, f'{bold} bold phrases in {words} words')
    hdr = [n for n, l in enumerate(lines, 1) if re.match(r'\s*[-*+] \*\*[^*]+(:\*\*|\*\*:)', l)]
    if len(hdr) >= 4: add('E2', hdr[0], f'{len(hdr)} bullets in "bold label: text" form')
    for n, l in enumerate(lines, 1):
        m = re.match(r'#{1,6} (.+)', l)
        if m:
            ws = [w for w in re.findall(r'[A-Za-z]{4,}', m.group(1))]
            if len(ws) >= 4 and all(w[0].isupper() for w in ws): add('E4', n, m.group(1))
    return sorted(out, key=lambda f: (f['severity'], f['line']))

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('files', nargs='+'); ap.add_argument('--min-severity', type=int, default=3, choices=(1, 2, 3)); ap.add_argument('--json', action='store_true')
    a = ap.parse_args(); worst = False; res = {}
    for f in a.files:
        t = sys.stdin.read() if f == '-' else open(f, encoding='utf-8', errors='replace').read()
        r = [x for x in check(t) if x['severity'] <= a.min_severity]; res[f] = r; worst |= any(x['severity'] == 1 for x in r)
    if a.json: print(json.dumps(res, indent=1))
    else:
        for f, r in res.items():
            c = [sum(x['severity'] == s for x in r) for s in (1, 2, 3)]
            print(f'{f}: {c[0]} fix now, {c[1]} fix before publishing, {c[2]} to judge')
            for x in r: print(f"  [{x['severity']}] {x['id']} {x['name']} (line {x['line']}): \"{x['found']}\" -> {x['fix']}")
    sys.exit(1 if worst else 0)

if __name__ == '__main__': main()
