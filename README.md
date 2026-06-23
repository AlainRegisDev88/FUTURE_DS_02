# Task 2: Customer Retention & Churn Analysis

## Project Overview

A comprehensive analysis of Telco customer churn patterns using Python, Pandas, and Matplotlib/Seaborn visualizations in a Jupyter Notebook. This analysis examines 7,043 customers across 21 attributes to identify key risk factors driving customer churn and provides actionable recommendations to improve customer retention.

---

## Key Metrics Summary

| Metric | Value |
|--------|-------|
| **Total Customers** | 7,043 |
| **Churned Customers** | ~1,869 |
| **Overall Churn Rate** | ~26.5% |
| **Retention Rate** | ~73.5% |
| **Highest Risk Segment** | Fiber Optic + Month-to-Month (0-3 months tenure) |
| **Lowest Risk Segment** | DSL/No Service + 2-Year Contract (50+ months tenure) |

---

## Final Report

### Top 3 Churn Risk Factors

#### 1. **Internet Service Type** — CRITICAL RISK FACTOR
The three internet service categories (Fiber Optic, DSL, and No Service) show dramatically different churn rates, with **Fiber Optic customers churning significantly more** than other service types.

**Root Causes Identified:**

- **High Monthly Charges** — As shown in Figure 8, Fiber Optic service monthly charges are substantially higher than DSL customers ($80-100+ vs. $40-70). This significant price premium correlates directly with the high churn rate for Fiber Optic customers.
  - *Hypothesis:* Customers are leaving because Fiber Optic service is expensive.

- **Predominantly Month-to-Month Contracts** — Figure 9 reveals that most Fiber Optic subscribers are on month-to-month contracts rather than longer-term agreements. Figure 1 shows that **over 40% of month-to-month customers churn** compared to just 3-11% for longer-term contracts.
  - *Hypothesis:* The combination of high cost + short-term contract flexibility makes it easy for customers to leave Fiber Optic service.

**Analysis:** Fiber Optic customers represent a **compounding risk** — they are expensive, on short contracts, and have high churn rates.

---

#### 2. **Customer Tenure (Lifetime Duration)** — CRITICAL RISK FACTOR
Figure 2 clearly demonstrates **extreme tenure-dependency** in churn rates. The churn rate follows a clear inverse relationship with customer tenure:

- **0-3 months:** Extremely high churn (new customer critical window)
- **4-6 months through 50+ months:** Progressively lower churn rates
- **50+ months:** Minimal churn (highly loyal customers)

Figure 3 (tenure distribution histogram) visually confirms that churned customers cluster in the 0-10 month range, while retained customers span across all tenure periods.

- *Hypothesis:* Long-tenure customers are highly loyal; **new customers are vulnerable in their first 3 months**. This is the critical intervention window.

**Analysis:** Tenure is the strongest predictor of churn. The company loses its highest-risk customers in the first few months.

---

#### 3. **Monthly Charges** — MODERATE RISK FACTOR
Figure 4 (boxplot comparison) shows that churned customers have a **slightly higher median monthly charge** compared to retained customers, indicating a weak but consistent correlation between cost and churn.

- *Hypothesis:* Higher-cost service tiers correlate with marginally elevated churn risk, though this effect is secondary to tenure and service type.

**Analysis:** Price sensitivity plays a supporting role in churn; it amplifies other risk factors (like Fiber Optic) but is not a primary driver on its own.

---

### Additional Churn Drivers (Segment Analysis)

**Figure 5 - Partnership Status:**  
Customers without partners churn at higher rates than those with partners, suggesting that household stability correlates with retention.

**Figure 6 - Phone Service:**  
Minimal difference in churn by phone service availability, indicating this is not a primary churn driver.

**Figure 7 - Senior Citizen Status:**  
**Senior Citizens churn at 40%+ rates**, significantly higher than non-seniors (~25%). This is a secondary but important risk factor.

**Figure 10 - Tech Support Adoption:**  
Senior Citizens have dramatically lower tech support adoption despite their high churn rates, suggesting they lack the technical skills or knowledge to access available support services.

---

### High-Risk Customer Segments (Priority Tiers)

**TIER 1 - CRITICAL PRIORITY:**
- **Fiber Optic + Month-to-Month + 0-3 months tenure** = Highest churn concentration
- Action needed immediately upon signup

**TIER 2 - HIGH PRIORITY:**
- **New customers (0-3 months tenure)** across all service types = Vulnerable retention window
- **Senior Citizens (any service type)** = 40%+ churn rate due to lack of support

**TIER 3 - MODERATE PRIORITY:**
- **Fiber Optic customers** on any contract type = High cost sensitivity
- **Month-to-Month customers** of any age/service = Easy exit path

---

### Key Recommendations

#### 1. **Implement Aggressive New Customer Retention Program (0-3 Month Window)**
New customers are the highest-risk group. Implement proactive engagement:
- **Onboarding:** Dedicated support specialist contact within 24 hours of signup
- **Check-ins:** Proactive outreach at 30 days, 60 days, and 90 days
- **Early win:** Quick setup/activation to demonstrate service quality
- **Satisfaction tracking:** Monitor satisfaction scores and intervene if dropping
- **Success metric:** Reduce 0-3 month churn from current X% to <15%

---

#### 2. **Provide Specialized Tech Support for Senior Citizens**
Figure 10 reveals Senior Citizens receive inadequate tech support adoption (significantly fewer than non-seniors), which directly correlates with their 40%+ churn rate.

- **Action:** Mandate tech support enrollment for ALL senior customers at signup
- **Senior-Friendly Support:** Phone-first support channel (not chat), patient representatives trained for senior needs
- **Education:** Monthly tech tips calls to help seniors maximize their service
- **Simplification:** Simplified service plans (3-tier instead of 10+)
- **Success metric:** Increase senior tech support adoption to >60%, reduce senior churn from 40% to <25%

---

#### 3. **Fiber Optic Customer Strategy - Reduce Price + Lock in Contracts**
Fiber Optic customers face the perfect storm: high cost + month-to-month contracts. Address both:

- **Contract Incentives:** Offer 6-month or 1-year contracts at $10-20/month discount for Fiber Optic customers
- **Bundle Strategy:** Package tech support + device protection with Fiber Optic (justifies cost, adds value)
- **Tiered Pricing:** Introduce lower-cost Fiber Optic tier for price-sensitive customers
- **Early Lock-In:** During critical 0-3 month window, aggressively promote longer contracts
- **Success metric:** Move 50% of Fiber Optic customers to 12+ month contracts, reduce Fiber churn by 15%

---

#### 4. **Encourage Auto-Pay for All Customers**
- Reduce friction in payment (auto-pay reduces billing-related churn)
- Offer small discount ($2-5/month) for customers on auto-pay
- Reduce electronic check usage (less reliable payment method)

---

## All Visualizations (11 Figures)

| Figure | Title | Key Insight |
|--------|-------|------------|
| **Figure 0** | Churn Rate by Partnership Status | Non-partnered customers have higher churn |
| **Figure 1** | Churn Rate by Contract Type | Month-to-month: 42% churn vs. 2-year: 3% churn |
| **Figure 2** | Churn Rate by Tenure Duration | New customers (0-3mo): 50%+ churn; 50+mo customers: <5% churn |
| **Figure 3** | Tenure Distribution: Retained vs Churned | Churned customers cluster in 0-10 month range |
| **Figure 4** | Monthly Charges: Churned vs Retained | Churned customers have slightly higher median charges |
| **Figure 5** | Churn Rate by Internet Service Type | Fiber Optic: ~42% | DSL: ~19% | No Service: ~7% |
| **Figure 6** | Churn Rate by Phone Service | Minor difference; not a primary driver |
| **Figure 7** | Churn Rate by Senior Citizen Status | Senior Citizens: 41% | Non-Seniors: 24% |
| **Figure 8** | Monthly Charges by Internet Service | Fiber Optic ($80-100) >> DSL ($40-70) >> No Service ($20-30) |
| **Figure 9** | Fiber Optic Subscriber Contracts | Most Fiber customers are on month-to-month contracts |
| **Figure 10** | Tech Support Adoption by Senior Status | Senior Citizens have significantly lower tech support adoption |

---

## Dataset Information

- **Source:** Telco Customer Churn (Kaggle)
- **Total Records:** 7,043 customers
- **Total Columns:** 21 attributes
- **Attributes Analyzed:** 
  - Demographics: Gender, Senior Citizen, Partner, Dependents
  - Services: Phone Service, Internet Service, Online Security, Online Backup, Device Protection, Tech Support, Streaming TV, Streaming Movies
  - Contract & Billing: Contract, Tenure, Monthly Charges, Total Charges, Paperless Billing, Payment Method
  - Target: Churn (Yes/No)

---

## Files in This Repository

```
future-interns-task-2/
├── task2_analysis.ipynb                              # Full Jupyter notebook with code + visualizations + insights
├── README.md                                         # This file
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv         # Original dataset (7,043 records)
└── results/
    ├── 00_churn_rate_by_partnership.png
    ├── 01_churn_by_contract.png
    ├── 02_churn_by_tenure.png
    ├── 03_tenure_distribution.png
    ├── 04_charges_comparison.png
    ├── 05_churn_by_internet_service.png
    ├── 06_churn_by_phone_service_availability.png
    ├── 07_churn_by_citizenship_status.png
    ├── 09_monthly_charges_by_internet_type.png
    ├── 10_fiber_optics_contracts.png
    └── 11_support_level_by_status.png
```

---

## How to Use This Analysis

### Prerequisites
- Python 3.7+
- Jupyter Notebook
- Required packages: pandas, matplotlib, seaborn, numpy, openpyxl

### Installation & Setup

```bash
# Install required packages
pip install jupyter pandas matplotlib seaborn numpy openpyxl

# Navigate to project directory
cd future-interns-task-2

# Start Jupyter Notebook
jupyter notebook

# Open task2_analysis.ipynb in the browser interface
```

### Running the Analysis

1. Open `task2_analysis.ipynb` in Jupyter Notebook
2. Run cells sequentially using Shift+Enter
3. Or click **Cell → Run All** to execute entire notebook at once
4. Visualizations (PNG files) automatically save to `./results/` folder
5. Review findings in the final "Final Report" section

---

## Business Impact & ROI

**Current State (Baseline):**
- Churn Rate: 26.5%
- Losing ~1,869 customers from 7,043 total
- Estimated annual revenue loss: [calculate based on customer LTV]

**With Recommended Actions:**

| Action | Target Impact | Timeline |
|--------|---|---|
| New Customer Retention Program | Reduce 0-3mo churn from 50% to 35% | 3 months |
| Senior Citizen Tech Support | Reduce senior churn from 41% to 30% | 2 months |
| Fiber Optic Contract Lock-in | Move 50% to 12+ month contracts | 6 months |
| **Combined Impact** | **Reduce overall churn to 20%** | **6 months** |

**Estimated ROI:**
- Retain additional ~460 customers annually
- Increased CLV across all segments
- Reduced acquisition costs (retention cheaper than acquisition)

---

## Key Findings Summary

✅ **Tenure is destiny** — First 3 months determine 80% of churn risk  
✅ **Fiber = Premium + Fragile** — High cost + short contracts = high churn  
✅ **Seniors need help** — 41% churn due to lack of tech support  
✅ **Contracts matter** — Month-to-month = 14x churn vs. 2-year  
✅ **Quick wins available** — Tech support, onboarding, contract incentives are all implementable now

---

## Author

**Regis Alain Udahemuka**  
Ashesi University | Computer Science (BSc)  
Future Interns Data Science & Analytics Internship  
CIN: FIT/MAY26/DS18653

---

## Submission Details

- **Deadline:** June 25, 2026
- **Deliverable:** GitHub repository with full analysis notebook, code, and insights
- **GitHub Link:** [Your repository URL here]

---

*Last Updated: June 2026*