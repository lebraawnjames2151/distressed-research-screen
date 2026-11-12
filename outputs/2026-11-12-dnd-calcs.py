# Dye & Durham screen calculations. All inputs C$ thousands, from data/ press releases (section named).
# Q1 FY27 = Q1 FY2027 results release, 12 Nov 2026. FY26 = Q4/FY2026 release, 29 Sep 2026. Q3 = Q3 FY2026 release, 19 May 2026.
inp = dict(
  loans_current=27_108, loans_noncurrent=1_194_785, converts=101_330,      # Q1 FY27, statement of financial position, Sep 30 2026
  lease_current=4_620, lease_noncurrent=9_078, cash=88_951,               # same
  ebitda_q1_27=46_559, ebitda_q4_26=55_099, ebitda_q3_26=42_867, ebitda_q2_26=50_352,  # Q1 FY27, summary of quarterly results
  ebitda_q1_26=50_435, ebitda_q4_25=47_744,                               # same table
  net_interest_ltm_mar26=110_600,                                         # Q3 release, "Net interest for LTM March 2026 is $110.6 million"
  ocf_q1_27=31_316, ocf_fy26=153_432, ocf_q1_26=40_217,                   # Q1 FY27 and FY26 selected key metrics
  ni_q3_26_orig=66_001, ni_q3_26_adj=41_406,                              # Q3 release key metrics; Q1 FY27 quarterly table
  rev_q1_27=94_866, rev_q1_26=108_302,
)
g = inp
debt = g['loans_current'] + g['loans_noncurrent'] + g['converts']
leases = g['lease_current'] + g['lease_noncurrent']
net_debt = debt - g['cash']
net_debt_l = net_debt + leases
ltm_ebitda = g['ebitda_q1_27'] + g['ebitda_q4_26'] + g['ebitda_q3_26'] + g['ebitda_q2_26']
ltm_ebitda_mar26 = g['ebitda_q3_26'] + g['ebitda_q2_26'] + g['ebitda_q1_26'] + g['ebitda_q4_25']
ltm_ocf = g['ocf_q1_27'] + g['ocf_fy26'] - g['ocf_q1_26']
out = [
 ("Gross debt (carrying value)", "loans current + loans non-current + convertible debentures", debt),
 ("Net debt ex leases", "gross debt - cash", net_debt),
 ("Net debt incl leases", "net debt + lease liabilities", net_debt_l),
 ("LTM Sep-26 adj EBITDA", "Q2 FY26 + Q3 FY26 + Q4 FY26 + Q1 FY27", ltm_ebitda),
 ("Net leverage ex leases (x)", "net debt / LTM adj EBITDA", round(net_debt/ltm_ebitda,2)),
 ("Net leverage incl leases (x)", "(net debt + leases) / LTM adj EBITDA", round(net_debt_l/ltm_ebitda,2)),
 ("LTM Mar-26 adj EBITDA", "Q4 FY25 + Q1 FY26 + Q2 FY26 + Q3 FY26", ltm_ebitda_mar26),
 ("Interest cover LTM Mar-26 (x)", "LTM Mar-26 adj EBITDA / LTM Mar-26 net interest", round(ltm_ebitda_mar26/g['net_interest_ltm_mar26'],2)),
 ("LTM Sep-26 operating cash flow", "FY26 OCF + Q1 FY27 OCF - Q1 FY26 OCF", ltm_ocf),
 ("Min EV for 60% LTV, all debt", "gross debt / 0.60", round(debt/0.60)),
 ("  as multiple of LTM EBITDA (x)", "(gross debt / 0.60) / LTM adj EBITDA", round(debt/0.60/ltm_ebitda,2)),
 ("Converts as % of cash", "convertible debentures / cash", f"{g['converts']/g['cash']:.0%}"),
 ("Q1 revenue change", "Q1 FY27 / Q1 FY26 - 1", f"{g['rev_q1_27']/g['rev_q1_26']-1:.1%}"),
 ("Q3 FY26 net income restatement", "adjusted - originally reported", g['ni_q3_26_adj']-g['ni_q3_26_orig']),
]
for k,f,v in out: print(f"{k:34} {f:62} {v:>12,}" if isinstance(v,(int,float)) else f"{k:34} {f:62} {v:>12}")
