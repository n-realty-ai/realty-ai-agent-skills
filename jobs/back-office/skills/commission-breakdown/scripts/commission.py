#!/usr/bin/env python3
"""Commission breakdown from documented inputs. Never assumes a rate. Usage: commission.py deal.json
Order used: gross = price x rate; referral = gross x referral_pct; split applies to what remains; fees come out of the agent share; tax only if tax_rate is given.
Confirm that this order matches the compensation plan; if it does not, do not use the result."""
import json, sys
from decimal import Decimal, ROUND_HALF_UP
def d(v): return Decimal(str(v))
def money(v): return v.quantize(Decimal('0.01'), ROUND_HALF_UP)
def run(x):
    missing = [k for k in ('price', 'rate', 'agent_split') if x.get(k) is None]
    if missing: raise SystemExit('MISSING, not guessed: ' + ', '.join(missing))
    for k in ('rate', 'agent_split', 'referral_pct', 'tax_rate'):
        if x.get(k) is not None and not 0 <= d(x[k]) <= 1: raise SystemExit(f'{k} must be a fraction between 0 and 1, for example 0.025')
    gross = money(d(x['price']) * d(x['rate'])); lines = [('Gross commission', gross)]
    ref = money(gross * d(x.get('referral_pct') or 0)); rest = gross - ref
    if ref: lines += [('Referral fee', -ref), ('After referral', rest)]
    agent = money(rest * d(x['agent_split'])); lines += [('Brokerage share', -(rest - agent)), ('Agent share', agent)]
    for f in x.get('fees', []):
        agent -= money(d(f['amount'])); lines.append((f['name'], -money(d(f['amount']))))
    lines.append(('Before tax', agent)); flags = []
    if x.get('tax_rate') is None: flags.append('Tax rate not supplied: tax and net not calculated.')
    else:
        tax = money(agent * d(x['tax_rate'])); lines += [('Tax on agent amount', tax), ('Total including tax', agent + tax)]
        flags.append('Confirm with the accountant that tax applies to this amount and is added, not deducted.')
    if agent < 0: flags.append('Agent amount is negative: check fees.')
    return lines, flags
if __name__ == '__main__':
    lines, flags = run(json.load(open(sys.argv[1])))
    for n, v in lines: print(f'{n:28}{v:>14,.2f}')
    for f in flags: print('FLAG:', f)
