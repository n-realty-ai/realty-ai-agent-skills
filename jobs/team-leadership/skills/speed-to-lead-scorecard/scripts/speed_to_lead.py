#!/usr/bin/env python3
"""Speed-to-lead by agent and source. CSV columns: lead_id,agent,source,received,first_response
Times like 2026-11-23 14:05. Blank first_response counts as never contacted. Pass human responses only."""
import argparse, csv, datetime as dt, statistics
from collections import defaultdict
def t(s): return dt.datetime.fromisoformat(s.strip())
def fmt(m): return f'{m:.0f} min' if m < 120 else f'{m/60:.1f} h'
def run(rows, minimum=10):
    g = defaultdict(list)
    for r in rows: g[(r['agent'].strip() or 'UNASSIGNED', r['source'].strip() or 'UNKNOWN')].append(r)
    out = []; gaps = []
    for k, L in sorted(g.items()):
        mins = []; never = 0
        for r in L:
            if not (r.get('first_response') or '').strip(): never += 1; continue
            m = (t(r['first_response']) - t(r['received'])).total_seconds() / 60
            if m < 0: gaps.append(f"lead {r['lead_id']}: response before receipt, excluded")
            else: mins.append(m)
        ok = len(L) >= minimum and bool(mins)
        out.append(dict(agent=k[0], source=k[1], leads=len(L), median=fmt(statistics.median(mins)) if ok else 'not ranked', slowest=fmt(max(mins)) if ok else 'not ranked', never=never))
    return out, gaps
if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument('csv'); ap.add_argument('--min-leads', type=int, default=10); a = ap.parse_args()
    out, gaps = run(list(csv.DictReader(open(a.csv, encoding='utf-8-sig'))), a.min_leads)
    print('Agent | Source | Leads | Median | Slowest | No response recorded')
    for r in out: print(' | '.join(str(v) for v in r.values()))
    for x in gaps: print('DATA GAP:', x)
    print('A blank response time may mean the channel is missing from the export.')
