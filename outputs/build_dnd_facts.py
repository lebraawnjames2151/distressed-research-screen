"""Build the Dye & Durham facts + debt page in the layout of facts.html.
Inputs: facts.html (style and scripts), data/*.txt (quotes are checked word for word against these).
Output: outputs/2026-11-12-dye-durham-facts.html
Run from the repo root: python3 outputs/build_dnd_facts.py
"""
import re, json, html as H

ROOT = '.'
tpl = open(f'{ROOT}/facts.html').read()
CSS = tpl[tpl.find('<style>') + 7: tpl.find('</style>')]
scripts = re.findall(r'<script>\n\(\(\) => \{.*?</script>', tpl, re.S)
assert len(scripts) == 2
SCRIPTS = '\n'.join(scripts)

BASE = 'https://investors.dyedurham.com/news/'
DOCS = {
 'Q1':  ('dye-durham-reports-first-quarter-fiscal-2027-financial-results', 'Q1 FY2027 results release', 'Nov 12, 2026'),
 'FY26':('dye-durham-reports-fourth-quarter-and-year-end-fiscal-2026-financial-results', 'Q4 and fiscal 2026 results release', 'Sep 29, 2026'),
 'Q3':  ('dye-durham-reports-third-quarter-fiscal-2026-financial-results', 'Q3 FY2026 results release', 'May 19, 2026'),
 'SA':  ('dye-durham-announces-support-agreements-with-plantro-and-edgepoint-strengthening-governance-with-new-appointments', 'Support agreements with Plantro and EdgePoint', 'Nov 5, 2026'),
 'TC':  ('dye-durham-announces-conclusion-of-transformation-committee-and-announces-appointment-of-interim-ceo-and-new-board-chair', 'Interim CEO and new Board Chair', 'Aug 31, 2026'),
 'CEO': ('dye-durham-announces-ceo-transition', 'CEO transition', 'Jun 23, 2026'),
}
# id: (doc, section, [quotes])
SRC = {
 'S1': ('Q1', 'highlights', ['Revenue was $94.9 million, representing a decrease of $13.4 million, or 12.4% (8% excluding Credas), from Q1 FY2026']),
 'S2': ('Q1', 'highlights', ['Operating costs, comprising of direct costs, technology and operations, general and administrative, and sales and marketing costs, were $48.3 million, a decrease of $9.6 million, or 17%, from Q1 FY2026.',
                             'primarily reflecting a $26.3 million decrease in finance costs, net, to $19.6 million',
                             'The Company was in compliance with the financial maintenance covenants under its senior credit agreement as of September 30, 2026.']),
 'S3': ('Q1', 'selected key metrics, three months ended September 30, 2026 and 2025', ['Cash flow provided by operating activities 31,316 40,217']),
 'S4': ('Q1', 'summary of quarterly results, C$ thousands', ['Quarterly results Q1 2027 Q4 2026 Q3 2026 Q2 2026', 'Revenue 94,866 104,171 91,180 107,024', 'Net income (loss) (1) (11,076) (19,862) 41,406 (21,790)', 'Adjusted EBITDA (2) 46,559 55,099 42,867 50,352',
                             'Quarterly results Q1 2026 Q4 2025 Q3 2025 Q2 2025', 'Revenue 108,302 105,173 103,420 115,746', 'Net loss (1) (38,272) (29,552) (23,449) (19,664)', 'Adjusted EBITDA (2) 50,435 47,744 52,862 64,652']),
 'S5': ('Q1', 'statement of financial position, September 30, 2026 and June 30, 2026, C$ thousands',
        ['Cash and cash equivalents 88,951 41,432', 'Intangible assets, net 540,764 568,856', 'Goodwill 1,062,401 1,061,531 Total assets 1,819,246 1,795,488', 'Property and equipment, net 5,728 6,305',
         'Lease liabilities, current 4,620 4,868 Loans and borrowings, current 27,108 12,435 Convertible debentures 101,330 104,396', 'Lease liabilities 9,078 8,895 Loans and borrowings 1,194,785 1,167,014']),
 'S6': ('FY26', 'selected key metrics, three months and year ended June 30', ['Cash flow provided by operating activities 65,175 56,815 153,432 148,200']),
 'S7': ('FY26', 'Q4 highlights', ['At June 30, 2026, the Company had drawn $28.5 million on the revolving credit facility and the Consolidated First Lien Net Leverage (as such term is defined in the senior credit agreement) ratio was approximately 5.17x.']),
 'S8': ('FY26', 'Q3 2026 adjustments', ["the Company's CEO and CFO concluded that the Company's internal controls over financial reporting were not effective as at June 30, 2026 due to a material weakness"]),
 'S9': ('FY26', 'Q3 2026 adjustments', ['Specifically, net loss for Q3 2026 decreased by $32.5 million', "the repayments made toward the Company's Term Loan B and Senior Secured 2029 Notes"]),
 'S10':('Q3', 'selected key metrics', ['Net income (loss) 66,001 (23,449)']),
 'S11':('Q3', 'update on forward-looking information', ['costs related to the delayed filing of the audited consolidated financial statements for the year ended June 30, 2025',
                             'the waiver the Company received under its senior credit agreement in December 2025', 'Net interest for LTM March 2026 is $110.6 million']),
 'S12':('Q3', 'highlights', ['At March 31, 2026, the Company had drawn $31.5 million on the revolving credit facility and the Consolidated First Lien Net Leverage Ratio (as such term is defined in the senior credit agreement) was approximately 5.52x.']),
 'S13':('Q3', 'update on forward-looking information, notes, dividends', ["the repayment of the Company's 3.75% convertible debentures, which matured on March 1, 2026",
                             'Gain on disposal of subsidiary related to the disposition of Credas, which closed on January 6, 2026', 'has elected to indefinitely suspend the declaration and payment of dividends']),
 'S14':('SA', 'release', ['representing approximately 36% of shares outstanding', 'customary standstill and voting support agreements with the Company until September 2027',
                             'The litigation between Plantro and the Company will be dismissed as part of these agreements.']),
 'S15':('TC', 'release', ["Mr. Schulte has been appointed as the Company's interim CEO effective immediately, while the Board search for a permanent CEO remains ongoing."]),
 'S16':('CEO', 'release', ['George Tsivin is no longer serving as Chief Executive Officer', "The Company's previously announced strategic process remains ongoing."]),
 'S18':('Q1', 'release opening and About Dye & Durham Limited', ['a leading provider of cloud-based legal practice management software', 'The Company has operations in Canada, the United Kingdom, Ireland, Australia, and South Africa.']),
 'S17':('Q1', 'Adjusted EBITDA notes and non-IFRS definitions', ['changes in fair value of convertible debt and derivatives',
                             'adjusts net loss by adding back finance costs, amortization, depreciation and impairment costs']),
}

def norm(s):
    for a, b in (('|', ' '), ('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), ('\xa0', ' ')):
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip()
TXT = {k: norm(open(f'{ROOT}/data/{v[0]}.txt').read()) for k, v in DOCS.items()}
CHECK = {sid: [norm(q) in TXT[d] for q in qs] for sid, (d, _, qs) in SRC.items()}
n_q = sum(len(v) for v in CHECK.values()); n_ok = sum(sum(v) for v in CHECK.values())

# ---------- calculations (C$ thousands) ----------
v = dict(loans_c=27_108, loans_nc=1_194_785, conv=101_330, lease_c=4_620, lease_nc=9_078, cash=88_951, cash_jun=41_432,
         loans_c_jun=12_435, loans_nc_jun=1_167_014, conv_jun=104_396, lease_c_jun=4_868, lease_nc_jun=8_895,
         gw=1_062_401, intang=540_764, ta=1_819_246, ppe=5_728, ni_q3_orig=66_001, ni_q3_adj=41_406, int_ltm_mar=110_600)
Q = ['Q2 FY25', 'Q3 FY25', 'Q4 FY25', 'Q1 FY26', 'Q2 FY26', 'Q3 FY26', 'Q4 FY26', 'Q1 FY27']
REV = [115_746, 103_420, 105_173, 108_302, 107_024, 91_180, 104_171, 94_866]
EB = [64_652, 52_862, 47_744, 50_435, 50_352, 42_867, 55_099, 46_559]
NI = [-19_664, -23_449, -29_552, -38_272, -21_790, 41_406, -19_862, -11_076]
loans = v['loans_c'] + v['loans_nc']; loans_jun = v['loans_c_jun'] + v['loans_nc_jun']
debt = loans + v['conv']; debt_jun = loans_jun + v['conv_jun']
leases = v['lease_c'] + v['lease_nc']; leases_jun = v['lease_c_jun'] + v['lease_nc_jun']
net = debt - v['cash']; ltm = sum(EB[-4:]); ltm_mar = sum(EB[2:6])
lev = net / ltm; lev_l = (net + leases) / ltm; icov = ltm_mar / v['int_ltm_mar']
ltm_ocf = 153_432 + 31_316 - 40_217
due12 = v['loans_c'] + v['conv']; ev60 = debt / 0.60
CALC = [
 ('Gross debt (carrying value)', 'loans current + loans non-current + convertible debentures', f"27,108 + 1,194,785 + 101,330", f"{debt:,}"),
 ('Net debt', 'gross debt − cash', f"{debt:,} − 88,951", f"{net:,}"),
 ('LTM Sep-26 adjusted EBITDA', 'Q2 + Q3 + Q4 FY26 + Q1 FY27', '50,352 + 42,867 + 55,099 + 46,559', f"{ltm:,}"),
 ('Net leverage', 'net debt / LTM adjusted EBITDA', f"{net:,} / {ltm:,}", f"{lev:.2f}x"),
 ('Net leverage with leases', '(net debt + leases) / LTM adjusted EBITDA', f"({net:,} + {leases:,}) / {ltm:,}", f"{lev_l:.2f}x"),
 ('Interest cover, LTM Mar-26', 'LTM Mar-26 adjusted EBITDA / LTM Mar-26 net interest', f"{ltm_mar:,} / 110,600", f"{icov:.2f}x"),
 ('LTM Sep-26 operating cash flow', 'FY26 + Q1 FY27 − Q1 FY26', '153,432 + 31,316 − 40,217', f"{ltm_ocf:,}"),
 ('Due within 12 months', 'loans current + convertible debentures', '27,108 + 101,330', f"{due12:,}"),
 ('Convertibles / cash', 'convertible debentures / cash', '101,330 / 88,951', f"{v['conv']/v['cash']:.0%}"),
 ('Minimum EV for 60% LTV', 'gross debt / 0.60', f"{debt:,} / 0.60", f"{ev60:,.0f} ({ev60/ltm:.2f}x LTM EBITDA)"),
 ('Goodwill and intangibles share of assets', '(goodwill + intangibles) / total assets', '(1,062,401 + 540,764) / 1,819,246', f"{(v['gw']+v['intang'])/v['ta']:.0%}"),
 ('Q3 FY26 net income change', 'adjusted − originally reported', '41,406 − 66,001', f"{v['ni_q3_adj']-v['ni_q3_orig']:,}"),
]
m = lambda x: f"{x/1000:,.1f}"   # thousands -> millions, 1dp
def chg(a, b): return f"{(a-b)/1000:+,.1f} vs prior quarter ({(a/b-1):+.1%})" if b > 0 else f"{(a-b)/1000:+,.1f} vs prior quarter"

# ---------- helpers ----------
T = lambda *ids: ' '.join(f'<a class="tag" href="#{i}">{i}</a>' for i in ids)
GL = {
 'EBITDA': 'Earnings before interest, taxes, depreciation and amortization.',
 'LTM': 'Last twelve months: the four latest quarters added together.',
 'covenant': 'A promise in a loan agreement, such as a limit on leverage.',
 'LTV': 'Loan to value: debt divided by enterprise value.',
 'IRR': 'Internal rate of return: the annual return that sets the present value of all cash flows to zero.',
 'YTW': 'Yield to worst: the lowest yield across all call and maturity dates.',
 'material weakness': 'A gap in internal controls serious enough that a material error might not be caught in time.',
 'convertible debentures': 'Unsecured bonds the holder can swap into shares at a set price.',
 'SEDAR+': 'The Canadian regulators’ filing system for public companies.',
}
def ab(word, key=None):
    return f'<abbr tabindex="0" data-tip="{H.escape(GL[key or word])}">{word}</abbr>'

def bars(key, series, color, label, wide=True):
    W, Hh, x0, top = (640, 226, 56, 22) if wide else (360, 196, 44, 22)
    base_h = Hh - 26
    lo = min(0, min(series)); hi = max(series)
    step = {True: None}
    rng = hi - lo
    raw = rng / 4
    mag = 10 ** len(str(int(raw))) / 10
    stp = next(s * mag for s in (1, 2, 2.5, 5, 10) if s * mag >= raw)
    lo_t = (lo // stp) * stp; hi_t = -((-hi) // stp) * stp
    y = lambda val: top + (hi_t - val) / (hi_t - lo_t) * (base_h - top)
    out = [f'<svg class="{"wide" if wide else "narrow"}" viewBox="0 0 {W} {Hh}" role="img" aria-label="Results by quarter: {label}">']
    t = lo_t
    while t <= hi_t + 1e-9:
        cls = 'axis' if t == 0 else 'grid'
        out.append(f'<line class="{cls}" x1="{x0}" y1="{y(t):.1f}" x2="{W-8}" y2="{y(t):.1f}"/><text class="sm" x="{x0-6}" y="{y(t)+4:.1f}" text-anchor="end">{t/1000:,.0f}</text>')
        t += stp
    n = len(series); slot = (W - 8 - x0) / n; bw = slot * (0.55 if wide else 0.6)
    for i, val in enumerate(series):
        cx = x0 + slot * (i + .5); y0, y1 = sorted((y(0), y(val)))
        fill = 'var(--neg)' if val < 0 else color
        out.append(f'<rect data-tip="{Q[i]}, {label}: {m(val)}" data-read="results:{key}:{i}" tabindex="0" x="{cx-bw/2:.1f}" y="{y0:.1f}" width="{bw:.1f}" height="{max(y1-y0,1):.1f}" rx="3" fill="{fill}"/>')
        if wide:
            vy = y(val) - 6 if val >= 0 else y(val) + 14
            out.append(f'<text class="val" x="{cx:.1f}" y="{vy:.1f}" text-anchor="middle">{m(val)}</text>')
        lab = Q[i] if wide else Q[i].replace(' FY', '/')
        out.append(f'<text x="{cx:.1f}" y="{Hh-8 if wide else Hh-8}" text-anchor="middle"{" class=\"sm\"" if not wide else ""}>{lab}</text>')
    out.append('</svg>')
    return ''.join(out)

MEAS = [('Revenue', REV, 'var(--c1)'), ('Adjusted EBITDA', EB, 'var(--c2)'), ('Net income', NI, 'var(--c3)')]
panes = ''.join(f'<div class="pane{" on" if k == 0 else ""}" data-group="results" data-key="{k}">{bars(k, s, c, l)}{bars(k, s, c, l, False)}</div>' for k, (l, s, c) in enumerate(MEAS))
readdata = [[{'title': Q[i], 'label': l, 'value': m(s[i]), 'sub': ('first period shown' if i == 0 else chg(s[i], s[i-1]) if s[i-1] > 0 and s[i] > 0 else f"{(s[i]-s[i-1])/1000:+,.1f} vs prior quarter")
              + (' (Q3 FY26 as adjusted; first reported as 66.0)' if (l == 'Net income' and i == 5) else ''), 'tags': ['S4'] + (['S10'] if (l == 'Net income' and i == 5) else [])} for i in range(8)] for (l, s, c) in MEAS]

# ---------- content ----------
crit_rows = [
 ('Net leverage, both funds', '≤ 10.0x', f'{lev:.2f}x net debt / {ab("LTM")} adjusted {ab("EBITDA")} ({lev_l:.2f}x with leases)', 'pass', 'Pass', T('S4', 'S5')),
 ('Same, on adjusted EBITDA less capitalised costs (default)', '≤ 10.0x', 'Capitalised development costs are not in the sources read', 'na', 'Not testable', ''),
 ('Liquidity runway, both funds', '≥ 12 months', f'Cash {m(v["cash"])}. LTM operating cash flow +{m(ltm_ocf)}, so no operating burn. Revolver size and free cash flow not found', 'pass', 'Pass, not confirmed', T('S3', 'S5', 'S6')),
 (f'{ab("LTV")}, CLO', '≤ 60%', f'Needs EV of at least {ev60/1000:,.0f}, or {ev60/ltm:.1f}x LTM EBITDA, counting all debt. Market value and the loan’s place in the stack not found', 'na', 'Not testable', T('S5')),
 ('Maturity wall, CLO', 'none inside 18 months without a plan', f'{m(due12)} classified current, of which {m(v["conv"])} is {ab("convertible debentures")}. No maturity date or plan in the sources read', 'warn', 'Not testable, at risk', T('S5')),
 (f'{ab("IRR")}, opportunities fund', '> 15% over 2 to 5 years', 'No instrument price in the sources read', 'na', 'Not testable', ''),
 ('Interest cover (red flag only)', 'flag below 1.5x', f'{icov:.2f}x, LTM to Mar 31, 2026', 'pass', 'No flag, thin', T('S4', 'S11')),
 ('Hard assets with real value', 'wanted', f'Goodwill and intangibles are {(v["gw"]+v["intang"])/v["ta"]:.0%} of total assets. Property and equipment {m(v["ppe"])}', 'fail', 'Not met', T('S5')),
 ('Sticky recurring revenue with a moat', 'wanted', 'Recurring share and churn not in the sources read. Q1 revenue fell 12.4%', 'na', 'Not shown', T('S1')),
 ('Sponsor adding equity', 'wanted', 'None found. The support agreements cover governance only', 'fail', 'Not met', T('S14')),
 ('Catalysts in 6 to 24 months', 'wanted', 'CEO search, strategic process, standstill to Sep 2027. No dates', 'warn', 'Partly', T('S14', 'S15', 'S16')),
]
PILL = {'pass': 'var(--working)', 'fail': 'var(--neg)', 'warn': 'var(--amber)', 'na': 'var(--muted)'}
crit_html = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td><span class="pill" style="color:{PILL[k]}">{p}</span></td><td>{t}</td></tr>' for a, b, c, k, p, t in crit_rows)

flags = [
 ('audit', 'Audit or controls', 'Sep 29, 2026', ab('Material weakness', 'material weakness'), f'Internal controls over financial reporting were not effective at Jun 30, 2026. The company says the same weakness existed at Mar 31, 2026. {T("S8")}', 'S8'),
 ('audit', 'Audit or controls', 'Sep 29, 2026', 'Q3 FY2026 restated', f'Q3 FY2026 net income was first reported as 66.0 and now shows as 41.4, a change of {(v["ni_q3_adj"]-v["ni_q3_orig"])/1000:,.1f}. The FY2026 release describes the change as $32.5 million. The page does not reconcile the two. {T("S10", "S4", "S9")}', 'S9'),
 ('deadline', 'Covenant', 'Dec 2025', 'Credit agreement waiver', f'The company received a waiver under its senior credit agreement in December 2025. It was in compliance with the maintenance {ab("covenant")}s at Sep 30, 2026. {T("S11", "S2")}', 'S11'),
 ('deadline', 'Filing', 'FY2025', 'Late annual filing', f'The audited statements for the year to Jun 30, 2025 were filed late. {T("S11")}', 'S11'),
 ('context', 'Context', 'Nov 12, 2026', f'Adjusted {ab("EBITDA")}', f'The company’s measure adds back finance costs, amortization, impairment and restructuring costs, among others. It is not an IFRS measure. {T("S17")}', 'S17'),
 ('context', 'Context', 'May 19, 2026', 'Dividend suspended', f'The board suspended dividends indefinitely. {T("S13")}', 'S13'),
]
def qblock(sid):
    return ''.join(f'<q>{H.escape(q)}</q>' for q in SRC[sid][2])
flags_html = ''.join(f'<article class="flag {c}"><p class="f-meta"><span class="f-kind">{k}</span><span>{d}</span></p><h3>{h}</h3><p>{b}</p><details class="words"><summary>The release’s words, {s}</summary>{qblock(s)}</details></article>' for c, k, d, h, b, s in flags)

dates = [
 ('past', 'Dec 2025', f'Waiver received under the senior credit agreement. {T("S11")}'),
 ('past', 'Jan 6, 2026', f'Sale of Credas closed. {T("S13")}'),
 ('past', 'Mar 1, 2026', f'3.75% {ab("convertible debentures")} matured and were repaid. {T("S13")}'),
 ('past', 'May 19, 2026', f'Q3 FY2026 results. Dividend suspended. {T("S13")}'),
 ('past', 'Jun 23, 2026', f'CEO George Tsivin left. A board committee took over the CEO role. {T("S16")}'),
 ('past', 'Aug 31, 2026', f'Todd Schulte named interim CEO. Search for a permanent CEO continues. {T("S15")}'),
 ('past', 'Sep 29, 2026', f'FY2026 results. {ab("Material weakness", "material weakness")} disclosed. {T("S8")}'),
 ('past', 'Nov 5, 2026', f'Support agreements with Plantro and EdgePoint, about 36% of shares. Litigation to be dismissed. {T("S14")}'),
 ('past', 'Nov 12, 2026', f'Q1 FY2027 results. {T("S1")}'),
 ('ahead', 'Sep 2027', f'Standstill and voting support agreements end. {T("S14")}'),
]
dates_html = ''.join(f'<li class="{c}"><time>{d}</time><span>{t}</span></li>' for c, d, t in dates)

gaps = [
 'The Q1 FY2027 MD&A and financial statement notes: not read. ' + ab('SEDAR+') + ' blocked automated download and the company’s report pages are password protected.',
 'Debt by tranche (Term Loan B, Senior Secured 2029 Notes, revolver): amounts, coupons, maturities and security not found in the sources read.',
 'Convertible debentures now outstanding: maturity, coupon and conversion price not found in the sources read.',
 'Revolver size and amount undrawn at Sep 30, 2026: not found in the sources read.',
 'Capitalised development costs and capital expenditure, so free cash flow: not found in the sources read.',
 'Market prices for any instrument, and the share price: not found in the sources read.',
 'Next results date: not announced in the sources read.',
]

cards = [
 ('var(--c1)', 'Loans and borrowings', f'Includes the Term Loan B and the Senior Secured 2029 Notes, by name {T("S9")}', [
   ('Total amount', f'{m(loans)} at Sep 30, 2026: {m(v["loans_c"])} current, {m(v["loans_nc"])} non-current. Carrying value {T("S5")}'),
   ('Split by tranche', 'not found in the sources read'),
   ('Maturity', 'Senior Secured Notes: 2029, from the name only. Term Loan B: not found ' + T('S9')),
   ('Coupon', 'not found in the sources read'),
   ('Current price', 'not found in the sources read')]),
 ('var(--c2)', 'Revolving credit facility', 'Under the senior credit agreement', [
   ('Drawn', f'28.5 at Jun 30, 2026; 31.5 at Mar 31, 2026 {T("S7", "S12")}'),
   ('Drawn at Sep 30, 2026', 'not found in the sources read'),
   ('Commitment', 'not found in the sources read'),
   ('Covenant', f'First-lien net leverage, as defined: about 5.52x at Mar 31 and 5.17x at Jun 30, 2026. In compliance at Sep 30, 2026 {T("S12", "S7", "S2")}')]),
 ('var(--c4)', ab('Convertible debentures', 'convertible debentures'), 'Classified as current', [
   ('Total amount', f'{m(v["conv"])} at Sep 30, 2026; {m(v["conv_jun"])} at Jun 30, 2026. Changes in fair value run through finance costs {T("S5", "S17")}'),
   ('Maturity', 'not found in the sources read. Shown as a current liability ' + T('S5')),
   ('Coupon and conversion price', 'not found in the sources read'),
   ('Earlier series', f'The 3.75% debentures matured on Mar 1, 2026 and were repaid {T("S13")}')]),
 ('var(--c8)', 'Lease liabilities', 'Not counted in gross debt on this page', [
   ('Total amount', f'{m(leases)} at Sep 30, 2026: {m(v["lease_c"])} current, {m(v["lease_nc"])} non-current {T("S5")}')]),
]
cards_html = ''.join(f'<article class="card"><span class="stripe" style="background:{c}"></span><h3>{h}</h3><p class="terms">{t}</p><dl>' + ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in rows) + '</dl></article>' for c, h, t, rows in cards)

def srcs_html():
    out = []
    for sid, (d, sec, qs) in sorted(SRC.items(), key=lambda kv: int(kv[0][1:])):
        slug, name, dt = DOCS[d]
        ok = all(CHECK[sid])
        st = 'Quote found word for word in the saved copy.' if ok else 'Quote NOT FOUND in the saved copy.'
        out.append(f'<li id="{sid}"><span class="sid">{sid}</span><div><a href="{BASE}{slug}" target="_blank" rel="noopener">Dye &amp; Durham, {name}, {sec}</a><span class="sdate">{dt}. {st}</span>' + ''.join(f'<q>{H.escape(q)}</q>' for q in qs) + '</div></li>')
    return ''.join(out)

calc_html = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{r}</td></tr>' for a, b, c, r in CALC)

EXTRA_CSS = '''
.verdict { display: grid; gap: 10px; }
.verdict .v-head { display: flex; flex-wrap: wrap; align-items: baseline; gap: 10px 16px; }
.verdict .v-word { font: 400 44px/1 var(--serif); color: var(--amber); }
.two { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }
.two > div { min-width: 0; }
.two h3 { margin: 0 0 6px; }
ol.flagsl { margin: 0; padding-left: 20px; display: grid; gap: 8px; }
.chip.res { background: var(--amber-bg); color: var(--amber); }
.scroll td.wrap-ok, .scroll.crit td { white-space: normal; }
.scroll.crit td:nth-child(3) { min-width: 16rem; }
.scroll.crit td:first-child { min-width: 10rem; }
.slack { font: 500 13px/1.5 var(--mono); background: var(--soft); border-radius: 8px; padding: 10px 12px; }
'''

page = f'''<title>Dye &amp; Durham Screen</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400..700&amp;family=IBM+Plex+Mono:wght@500;600&amp;family=Instrument+Serif&amp;display=swap">
<style>{CSS}{EXTRA_CSS}</style>
<div class="wrap">
<header class="band">
<div class="meta"><span class="draft">Draft, public filings only</span><span class="draft">Until the trader signs off</span><span>As of Nov 12, 2026</span><span>TSX: DND</span><span>C$ millions unless noted</span></div>
<div class="title-row"><div><p class="kicker">Name brief</p><h1>Dye &amp; Durham Limited</h1><p class="sub">Screen, facts and debt, from public company releases</p></div><div class="chips"><span class="chip res">Screen: Watch</span><span class="chip lane">Analyst lane: not set</span></div></div>
<nav class="tabs" aria-label="Name pages"><a href="#facts-tab" data-tab="facts-tab" aria-current="page">Screen and facts</a><a href="#debt-tab" data-tab="debt-tab">Debt</a></nav>
</header>
<section aria-labelledby="brief"><h2 id="brief">In brief</h2><ul>
<li>Dye &amp; Durham provides cloud-based legal practice management software, with operations in Canada, the UK, Ireland, Australia and South Africa. {T("S18")} Q1 FY2027 revenue fell 12.4% to $94.9 million. {T("S1")}</li>
<li>Gross debt was {m(debt)} at Sep 30, 2026, against cash of {m(v["cash"])}. Net leverage is {lev:.2f}x {ab("LTM")} adjusted {ab("EBITDA")}. {T("S5", "S4")}</li>
<li>{m(v["conv"])} of {ab("convertible debentures", "convertible debentures")} are classified as current, more than the cash balance. {T("S5")}</li>
<li>Internal controls were not effective at Jun 30, 2026, and Q3 FY2026 net income was restated. {T("S8", "S10", "S4")}</li>
<li>The company met its {ab("covenant")}s at Sep 30, 2026, after a waiver in December 2025. {T("S2", "S11")}</li>
<li>Plantro and EdgePoint, about 36% of shares, signed standstill agreements to September 2027. The CEO role is interim. {T("S14", "S15")}</li>
</ul></section>
<p class="note"><strong>Source checks: {n_ok} of {n_q} quotes matched to saved source copies.</strong> The sources are company press releases, not the MD&amp;A or the financial statement notes, and they have no page numbers. Matching words does not verify their interpretation or check for newer filings. Click any tag such as {T("S1")} to read its quote.</p>
<div class="tab-panel on" id="facts-tab">
<section aria-labelledby="screen" class="verdict"><h2 id="screen">Screen against our criteria</h2>
<div class="v-head"><span class="v-word">Watch</span><span class="lede">No hard limit fails on the figures available. The {ab("LTV")}, {ab("IRR")} and maturity-wall tests cannot be run from the press releases. A yes or no needs the Q1 FY2027 MD&amp;A, the debt documents and instrument prices.</span></div>
<div class="two"><div><h3>Top three red flags</h3><ol class="flagsl">
<li>{m(v["conv"])} of convertibles are current, {v["conv"]/v["cash"]:.0%} of cash. Their maturity is not in the sources read. {T("S5")}</li>
<li>{ab("Material weakness", "material weakness")} at Jun 30, 2026, a restated Q3, late FY2025 statements and a waiver in December 2025. {T("S8", "S10", "S11")}</li>
<li>Revenue down 12.4% in Q1. Margin held by a 17% cut in operating costs. Interest cover {icov:.2f}x. No permanent CEO. {T("S1", "S2", "S11", "S15")}</li>
</ol></div><div><h3>Reasons to buy</h3><ol class="flagsl">
<li>LTM operating cash flow of {m(ltm_ocf)}. Cash rose from {m(v["cash_jun"])} to {m(v["cash"])} in the quarter. {T("S3", "S6", "S5")}</li>
<li>First-lien net leverage, as defined, fell from about 5.52x to 5.17x between March and June 2026. Q1 finance costs fell $26.3 million. {T("S12", "S7", "S2")}</li>
<li>Governance settled with the two largest holders. Litigation to be dismissed. {T("S14")}</li>
</ol></div></div>
<div class="scroll crit"><table><thead><tr><th>Criterion</th><th>Limit</th><th>This name</th><th>Result</th><th>Source</th></tr></thead><tbody>{crit_html}</tbody></table></div>
<p class="lede">Slack line, ready to paste:</p>
<p class="slack">Dye &amp; Durham: WATCH. 6.3x leverage passes. $101m current converts vs $89m cash, maturity terms unread. Next: Q1 MD&amp;A from SEDAR+.</p>
</section>
<section class="bare" aria-labelledby="figures"><h2 id="figures" class="vh">Key figures</h2><div class="tiles">
<div class="tile"><p class="t-label">Revenue</p><p class="t-value">94.9</p><p class="t-sub">Q1 FY2027, -13.4 vs Q1 FY2026 (-12.4%) {T("S1")}</p></div>
<div class="tile"><p class="t-label">Adjusted {ab("EBITDA")}</p><p class="t-value">46.6</p><p class="t-sub">Q1 FY2027. {m(ltm)} {ab("LTM")} {T("S4")}</p></div>
<div class="tile neg"><p class="t-label">Net income</p><p class="t-value">-11.1</p><p class="t-sub">Q1 FY2027, vs -38.3 in Q1 FY2026 {T("S4")}</p></div>
<div class="tile"><p class="t-label">Operating cash flow</p><p class="t-value">31.3</p><p class="t-sub">Q1 FY2027. {m(ltm_ocf)} LTM {T("S3", "S6")}</p></div>
<div class="tile date"><p class="t-label">Next dated event</p><p class="t-value">Sep 2027</p><p class="t-sub">Standstill agreements end. No results date announced {T("S14")}</p></div>
</div></section>
<section aria-labelledby="results"><h2 id="results">Results by quarter</h2>
<figure><figcaption><strong>Results by quarter</strong>, C$ millions. Pick a measure, then hover, tap or tab to a bar. Negative bars are in red. {T("S4")}</figcaption>
<div class="switch" role="group" aria-label="Measure" data-switch="results"><button type="button" data-pick="0" aria-pressed="true">Revenue</button><button type="button" data-pick="1" aria-pressed="false">Adjusted EBITDA</button><button type="button" data-pick="2" aria-pressed="false">Net income</button></div>
<div class="viz"><div class="plot">{panes}</div>
<aside class="readout" data-for="results" aria-live="polite"><p class="r-title">Q1 FY27</p><p class="r-label">Revenue</p><p class="r-value">94.9</p><p class="r-sub">{chg(REV[7], REV[6])}</p><ul class="r-rows"></ul><p class="r-tags">Source {T("S4")}</p><p class="r-hint">Hover, tap or tab to a bar to read it here.</p></aside></div></figure>
<script type="application/json" data-for="results">{json.dumps(readdata)}</script>
<div class="scroll"><table><thead><tr><th>Quarter</th><th>Revenue</th><th>Adjusted EBITDA</th><th>Net income</th><th>Source</th></tr></thead><tbody>{''.join(f"<tr><td>{Q[i]}</td><td>{m(REV[i])}</td><td>{m(EB[i])}</td><td>{m(NI[i])}</td><td>{T('S4')}</td></tr>" for i in range(8))}</tbody></table></div>
</section>
<section aria-labelledby="flags"><h2 id="flags">Disclosure flags</h2><p class="lede">Rose: audit or controls. Amber: a covenant or a filing. Grey: context. Open a flag to read the release’s own words.</p><div class="flags">{flags_html}</div></section>
<section aria-labelledby="dates"><h2 id="dates">Key dates</h2><p class="lede">Dates after the as-of date are marked ahead.</p><ul class="dates">{dates_html}</ul></section>
<section aria-labelledby="calcs"><h2 id="calcs">Calculations</h2><p class="lede">Run in code (<code>outputs/build_dnd_facts.py</code>). C$ thousands. Debt is at carrying value, not face. Leverage uses the company’s adjusted EBITDA because capitalised costs are not disclosed in the releases.</p>
<div class="scroll"><table><thead><tr><th>Item</th><th>Formula</th><th>Inputs</th><th>Result</th></tr></thead><tbody>{calc_html}</tbody></table></div></section>
<section aria-labelledby="gaps"><h2 id="gaps">Gaps</h2><p class="lede">What the sources did not answer. Nothing here is guessed.</p><ul>{''.join(f"<li>{g}</li>" for g in gaps)}</ul></section>
<section aria-labelledby="log"><h2 id="log">Change log</h2><h3>Nov 12, 2026: first screen</h3><ul><li>Built from six company press releases saved in <code>data/</code>. Criteria from <code>criteria.md</code> as of Nov 12, 2026; the EBITDA and EV definitions there are defaults, not yet confirmed.</li></ul></section>
</div>
<div class="tab-panel" id="debt-tab">
<section class="bare" aria-labelledby="debt-figures"><h2 id="debt-figures" class="vh">Debt figures</h2><div class="tiles">
<div class="tile"><p class="t-label">Gross debt</p><p class="t-value">{m(debt)}</p><p class="t-sub">Carrying value at Sep 30, 2026, leases excluded {T("S5")}</p></div>
<div class="tile"><p class="t-label">Net debt</p><p class="t-value">{m(net)}</p><p class="t-sub">After cash of {m(v["cash"])} {T("S5")}</p></div>
<div class="tile"><p class="t-label">Net leverage</p><p class="t-value">{lev:.2f}x</p><p class="t-sub">LTM adjusted EBITDA of {m(ltm)} {T("S4")}</p></div>
<div class="tile neg"><p class="t-label">Due within 12 months</p><p class="t-value">{m(due12)}</p><p class="t-sub">Convertibles {m(v["conv"])} plus current loans {m(v["loans_c"])} {T("S5")}</p></div>
</div></section>
<section aria-labelledby="owed"><h2 id="owed">What is owed</h2><p class="lede">From the balance sheet. The releases do not split loans and borrowings by tranche.</p><div class="cards debt">{cards_html}</div></section>
<section aria-labelledby="debt-years"><h2 id="debt-years">Debt by date</h2>
<div class="scroll"><table><thead><tr><th>Date</th><th>Loans and borrowings</th><th>Convertible debentures</th><th>Gross debt</th><th>Leases</th><th>Cash</th><th>Source</th></tr></thead><tbody>
<tr><td>Jun 30, 2026</td><td>{m(loans_jun)}</td><td>{m(v["conv_jun"])}</td><td>{m(debt_jun)}</td><td>{m(leases_jun)}</td><td>{m(v["cash_jun"])}</td><td>{T("S5")}</td></tr>
<tr><td>Sep 30, 2026</td><td>{m(loans)}</td><td>{m(v["conv"])}</td><td>{m(debt)}</td><td>{m(leases)}</td><td>{m(v["cash"])}</td><td>{T("S5")}</td></tr>
</tbody></table></div></section>
</div>
<section aria-labelledby="sources">
<details id="sources-box">
<summary><h2 id="sources">Sources ({len(SRC)})</h2></summary>
<p class="lede">Each entry gives the quote and its check status. Quotes were matched in code against the saved text of each release, ignoring table separators, spacing and curly quote marks. A match does not confirm the claim’s meaning or that the release is the latest.</p>
<ol class="src">{srcs_html()}</ol>
</details>
</section>
<footer>Built by <code>outputs/build_dnd_facts.py</code> in the layout of <code>facts.html</code>. Draft for a person to check. Not advice: no price targets. The screen suggests; the analyst decides. Dotted terms show a general definition on hover; the definitions are reference, not facts from the releases.</footer>
</div>
<div id="tip" role="tooltip"></div>
{SCRIPTS}
'''
assert '—' not in page, 'long dash found'
open(f'{ROOT}/outputs/2026-11-12-dye-durham-facts.html', 'w').write(page)
print(f'quotes {n_ok}/{n_q} FOUND'); [print('NOT FOUND', s, q) for s, (d, _, qs) in SRC.items() for q, ok in zip(qs, CHECK[s]) if not ok]
for a, b, c, r in CALC: print(f'{a:42} {r}')
