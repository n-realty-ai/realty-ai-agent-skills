#!/usr/bin/env python3
"""List missing, late, duplicate and mismatched deposits. Read only.
expected.csv: file,amount,due   ledger.csv: file,amount,date,ref   Dates are YYYY-MM-DD.
One expected deposit per file; files with instalments are reported for a person to check."""
import argparse, csv, datetime as dt
from decimal import Decimal
def money(s): return Decimal(s.replace(',', '').replace('$', '').strip())
def day(s): return dt.date.fromisoformat(s.strip())
def run(expected, ledger, as_of):
    out = []; seen = set()
    for e in expected:
        f = e['file'].strip(); amt = money(e['amount']); due = day(e['due'])
        if f in seen: out.append((f, 'Check by hand', 'more than one expected row')); continue
        seen.add(f); rows = [r for r in ledger if r['file'].strip() == f]; refs = ', '.join(r['ref'] for r in rows)
        if not rows:
            out.append((f, 'Missing' if due <= as_of else 'Not yet due', f'expected {amt:,.2f} due {due}')); continue
        same = [r for r in rows if money(r['amount']) == amt]
        if len(same) > 1: out.append((f, 'Duplicate', f'{amt:,.2f} recorded {len(same)} times: {refs}'))
        total = sum(money(r['amount']) for r in rows)
        if not same: out.append((f, 'Mismatch', f'expected {amt:,.2f}, ledger total {total:,.2f}: {refs}'))
        elif len(rows) > len(same): out.append((f, 'Check by hand', f'extra entries besides the expected amount: {refs}'))
        if min(day(r['date']) for r in rows) > due: out.append((f, 'Late', f'due {due}, first received {min(day(r["date"]) for r in rows)}: {refs}'))
    for r in ledger:
        if r['file'].strip() not in seen: out.append((r['file'].strip(), 'Unexpected entry', r['ref']))
    return out
if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument('expected'); ap.add_argument('ledger'); ap.add_argument('--as-of', default=dt.date.today().isoformat()); a = ap.parse_args()
    rd = lambda p: list(csv.DictReader(open(p, encoding='utf-8-sig')))
    r = run(rd(a.expected), rd(a.ledger), day(a.as_of))
    for row in r: print(' | '.join(row))
    print(f'{len(r)} exception(s). Causes are not assumed; check bank records.')
