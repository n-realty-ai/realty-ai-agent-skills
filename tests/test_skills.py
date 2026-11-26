import sys, datetime as dt
from decimal import Decimal as D
from pathlib import Path
sys.dont_write_bytecode = True
B = Path(__file__).resolve().parent.parent / 'jobs'
sys.path[:0] = [str(B / p / 'scripts') for p in ('back-office/skills/brokerage-money-checks', 'team-leadership/skills/team-performance-review', 'writing/skills/plain-writing')]
import commission, deposit_exceptions as dx, speed_to_lead as sl, check_writing as cw
n = 0
def ok(c, m):
    global n; assert c, m; n += 1
L, F = commission.run(dict(price=640000, rate=0.025, referral_pct=0.25, agent_split=0.8, fees=[dict(name='Transaction fee', amount=395)])); v = dict(L)
ok(v['Gross commission'] == D('16000.00') and v['Agent share'] == D('9600.00') and v['Before tax'] == D('9205.00'), v); ok('not supplied' in F[0], F)
for bad in (dict(price=1, rate=2.5, agent_split=0.8), dict(price=1, rate=0.02)):
    try: commission.run(bad); ok(False, 'accepted ' + str(bad))
    except SystemExit: ok(True, '')
E = [dict(file=f, amount=a, due=d) for f, a, d in [('A', '25,000', '2026-11-27'), ('B', '10000', '2026-11-20'), ('C', '15000', '2026-11-20'), ('D', '20000', '2026-11-20'), ('E', '12000', '2026-11-20'), ('G', '5000', '2026-12-20')]]
Lg = [dict(file=f, amount=a, date=d, ref=r) for f, a, d, r in [('B', '10000', '2026-11-24', '311'), ('C', '15000', '2026-11-19', '305'), ('C', '15000', '2026-11-19', '306'), ('D', '2000', '2026-11-19', '309'), ('E', '12000', '2026-11-19', '302'), ('Z', '1', '2026-11-19', '999')]]
r = {(a, b) for a, b, _ in dx.run(E, Lg, dt.date(2026, 11, 30))}
ok(r == {('A', 'Missing'), ('B', 'Late'), ('C', 'Duplicate'), ('D', 'Mismatch'), ('G', 'Not yet due'), ('Z', 'Unexpected entry')}, r)
rows = [dict(lead_id=str(i), agent='Casey', source='Portal', received='2026-11-23 09:00', first_response=f'2026-11-23 09:{i:02d}' if i < 11 else '') for i in range(1, 13)]
rows += [dict(lead_id='x', agent='Taylor', source='Referral', received='2026-11-23 09:00', first_response='2026-11-23 08:00')]
out, gaps = sl.run(rows); a = {o['agent']: o for o in out}
ok(a['Casey']['median'] == '6 min' and a['Casey']['never'] == 2 and a['Taylor']['median'] == 'not ranked' and len(gaps) == 1, (out, gaps))
hit = lambda t: {f['id'] for f in cw.check(t)}
for text, pid in [("It's not just a tool, it's a partner.", 'A1'), ('No fluff. No jargon.', 'A2'), ("Let's dive in.", 'A5'), ('The result? Sales.', 'A6'), ('A — B', 'B4'), ('This could potentially help.', 'B5'), ('We delve into it.', 'C1'), ('It serves as a hub.', 'C3'), ('Studies show this works.', 'D4'), ('Nestled by the park.', 'D3'), ('Great question!', 'F2'), ('See [insert link] now', 'F9'), ('x.com?utm_source=chatgpt.com', 'F10'), ('In conclusion, buy.', 'F7'), ('We call. We text. We email.', 'B2')]:
    ok(pid in hit(text), (pid, text, hit(text)))
for clean in ['The deposit is due Friday.', 'Call me if neither time works.', '`leverage` is a code name.', '> We delve into it.', 'Open Customize, then Connectors.', 'The roof was replaced in 2019 and the invoice is on file.']:
    ok(not hit(clean), (clean, hit(clean)))
print(n, 'checks passed')
