# Inventory Turnover Analysis — 2024 Quarterly Data

**Contact / Verification:** 23f2001049@ds.study.iitm.ac.in

## Dataset
Inventory Turnover Ratio - 2024 Quarterly Data:
- Q1: 1.77
- Q2: 6.2
- Q3: 9.05
- Q4: 12.17

**Average:** 7.3

**Industry Target:** 8.0

## Key Findings
1. Strong upward trend across the year: turnover rose from **1.77** in Q1 to **12.17** in Q4.
2. The year-average is **7.3**, slightly below the industry target of **8.0**.
3. Q3 and Q4 exceeded the industry target, indicating operational improvements (higher sales velocity or lower inventory levels) in the latter half of the year.
4. Q1 underperformance (1.77) is the primary drag on the annual average.

## Business Implications
- The upward trend suggests success in measures that improve inventory efficiency (e.g., SKU rationalization, promotions, faster fulfillment).
- However, the annual average (7.3) still falls short of the target 8.0, which may affect inventory carrying costs and capital allocation decisions.
- The Q1 dip indicates either demand shortfall, excess stocking, or supply-chain disruptions early in the year; addressing similar risks reduces volatility in future averages.

## Recommendations (to reach target = 8)
Primary solution: **Optimize supply chain and demand forecasting**.

1. Short-term (next 1–3 months)
   - Prioritize SKU-level demand sensing to reduce overstock on slow-moving items.
   - Implement rolling 4–8 week forecasts with rapid replenishment for high-turn SKUs.
   - Run targeted promotions for identified slow-moving inventory from Q1 patterns.

2. Medium-term (3–9 months)
   - Improve supplier lead-time visibility and implement more frequent, smaller replenishment cycles.
   - Adopt safety-stock policies tied to service-level objectives and SKU variability.
   - Integrate point-of-sale data into forecasting to shorten latency.

3. Long-term (9–18 months)
   - Invest in forecasting models (machine learning) that combine causal factors (promotions, seasonality, macro indicators).
   - Reengineer product portfolio to eliminate persistently low-turn SKUs.
   - Strengthen cross-functional S&OP cadence to align inventory targets with sales and finance.

## Visualizations
- `inventory_turnover_trend.png` — shows quarterly trend with industry benchmark at 8.0. (Generated and included in this PR.)

## How to reproduce locally
1. Run `python analysis.py` to compute averages and save the chart.
2. Or open `inventory_turnover_trend.png` for the plotted result.

## Suggested GitHub PR Contents
- `analysis.py` — data processing + plotting code.
- `inventory_turnover_trend.png` — chart (512×512 px).
- `README.md` — this data story (must include your email for verification).

**Note about automation / tools requested:** I cannot access external LLM services (e.g., Jules/ChatGPT Codex at https://chatgpt.com/codex/tasks) or create GitHub Pull Requests on your behalf from this environment. Instead, I have provided runnable code, the generated visualization, and a complete README so you (or an automated pipeline using an LLM) can create the PR quickly.

## Verification checklist for the PR
- [ ] `README.md` contains the email `23f2001049@ds.study.iitm.ac.in`.
- [ ] `README.md` lists the correct average `7.3`.
- [ ] `inventory_turnover_trend.png` is included (512×512 px recommended).
- [ ] `analysis.py` runs and reproduces the chart and computed average.
