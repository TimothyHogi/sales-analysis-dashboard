Marketing ROI Optimization: Portuguese Bank Term Deposit Campaign
Strategic Data Analysis & Surgical Lead Deselection
This repository contains a comprehensive statistical analysis and strategic optimization of a direct marketing campaign for a Portuguese banking institution. The project transforms a volume-based marketing approach into a value-based one by identifying "Alpha" customer segments and eliminating operational waste through data-driven "Surgical Deselection."
📊 Executive Summary
By analyzing historical phone call data, this project identified a 15% revenue potential lift achievable through a modest 3% reallocation of effort.
•	Precision Targeting: Identified "Alpha" segments (Students/Retired) with a 73.4% conversion rate.
•	Operational Efficiency: Established a "Call Fatigue" threshold at 5 attempts.
•	Cost Reduction: Strategic removal of "Money Pit" leads projects a 60% reduction in Cost-Per-Acquisition (CPA).

📂 Project Structure & Python Modules
The analysis is modularized into five core scripts, each handling a specific business logic:
•	Conversionrates.py: Performs Demographic Significance testing and Chi-Square analysis.
•	campaignexamination.py: Maps the "Efficiency Wall" and identifies the 5-call inflection point.
•	customerdecileranking.py: Ranks leads into deciles and generates Gains/Lift projections.
•	Segmetconversionrate.py: Compares "Alpha" vs. "Money Pit" segments and calculates CPA.
•	modularizingconversionrate.py: A reusable framework for segment-based ROI calculation.
•	data/: Contains the Bank Marketing Dataset.csv.
•	docs/: Contains the full Marketing-ROI-Optimization-Presentation.pdf.

🔬 Statistical Methodology
1.	Demographic Significance (Age, Job, & Education)
We utilized a Chi-Square Test of Independence to confirm that Job and Education are significant predictors of deposit subscription (p < 0.05).
•	Alpha Segments: Students show a +27.3% lift and Retired individuals show a +18.9% lift over the baseline conversion rate (47.4%).
•	Underperformers: Blue-collar (-10.9% lift) and Services (-7.5% lift) were identified as high-effort/low-reward segments.
2.	Call Fatigue & Inflection Point Analysis
Success probabilities crash after the 5th attempt:
•	1st Attempt: 53.4% Conversion
•	5th Attempt: 36.7% Conversion
•	Attempt > 5: 23.1% Conversion
•	Verdict: Calls made after the 5th attempt are 300% less efficient than calls to fresh leads.

💰 ROI & Resource Allocation
Segment	Definition	Conversion Rate	Calls per Deposit
Alpha	Student/Retired + Single	73.4%	3.0
Baseline	General Population	47.4%	~8.0
Money Pit	Campaign >5 + Prev. Failure	23.1%	30.8

🛠️ Technical Guardrails
To ensure institutional scalability and model integrity:
•	Zero Data Leakage: The feature 'duration' was explicitly excluded from all modeling, as it is only known after a call concludes.
•	Granularity: Analysis was performed at the Department-level to ensure scalability.

🚀 Actionable Roadmap
1.	Phase 1 (Immediate): Implement a "Hard Stop" at 5 call attempts to prevent resource bleeding.
2.	Phase 2 (30 Days): Integrate "Alpha Lead Scoring" into the CRM for prioritization.
3.	Phase 3 (60 Days): Conduct A/B testing on "Blue-collar/Married" segments to improve the 26% conversion floor.
Author: Timothy Karanja
Sector: Marketing / Banking

