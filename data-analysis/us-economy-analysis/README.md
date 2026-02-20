
<p align="center">
  <img src="../us-economy-analysis/assets/econ_health_banner.png" alt="Project Banner" width="100%">
</p>

---

# US & Global Economic Health Analysis

> Part of the DataInsideData™ technical research portfolio.  
> A data-driven examination of income, cost-of-living, and liquidity trends across the United States and global regions.

#### Fari Lindo • Lead Analyst  

DataInsideData™ Portfolio Project

**Collaborators:** James Ceus, Jessenia Diaz, Bakari Sibert, Sherla
Zhagnay

---

## Tech Stack

![EDA](https://img.shields.io/badge/EDA-000000)
![Statistical Analysis](https://img.shields.io/badge/Statistical%20Analysis-000000)
![Time Series](https://img.shields.io/badge/Time--Series-000000)
![Correlation](https://img.shields.io/badge/Pearson%20Correlation-000000)

![Python](https://img.shields.io/badge/Python-000000?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-000000?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-000000?logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-000000?logo=scipy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C)
![Seaborn](https://img.shields.io/badge/Seaborn-5B8FA8)
![Plotly](https://img.shields.io/badge/Plotly-000000?logo=plotly&logoColor=white)

---

![Last Commit](https://img.shields.io/github/last-commit/dataeden/fari-tech-portfolio) ![Repo Size](https://img.shields.io/github/repo-size/dataeden/fari-tech-portfolio)

![Top Language](https://img.shields.io/github/languages/top/dataeden/fari-tech-portfolio)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Executive Summary

This project evaluates economic resilience, income growth, purchasing
power, and cost-of-living pressures across the United States and
selected global regions.

### Key Quantitative Highlights

- U.S. **Total Personal Income increased \~110%** from \~\$10T (2000) to \~\$21T+ (2023).
- Disposable Personal Income rose proportionally, with a **pandemic-era peak in 2020--2021**.
- Real Disposable Personal Income peaked in early 2021 and declined \~9 percentage points through 2025.
- Correlation between income and housing burden in North America measured at **r ≈ -0.40**.
- Real Personal Consumption Expenditures show consistent **December seasonal spikes (\~3--5% above annual monthly average)**.
- Majority income concentration falls within the **\$40K--\$50K disposable income range**, indicating mid-tier clustering.

**Panel Structure**:

- Global dataset: 21 countries × 24 years (500 country-year observations)
- U.S. macro dataset: Monthly time-series (2007–2025, 216+ observations)

 > Volatility between nominal and real income post-2021 represents the strongest macro stress signal observed in this dataset.

> Overall, the U.S. economy demonstrates structural resilience, but inflation-adjusted income stagnation presents emerging liquidity constraints.

**Primary Datasets:**

- `Cost_of_Living_and_Income_Extended.csv`
- `US_Macro_Micro_Index.csv`

---

## 📌 KPI Snapshot

| KPI | Value | What it means |
|---|---:|---|
| Total Personal Income growth (2000 → 2023) | ~110% | Nominal income roughly doubled over two decades |
| RDPI change (2021 peak → 2025) | ~-9 pp | Inflation-adjusted purchasing power flattened/declined post-stimulus |
| Income ↔ Housing burden (North America) | r ≈ -0.40 | Higher income associated with lower housing share of income |
| Seasonal spending spike (Dec vs avg month) | ~+3–5% | Holiday-driven consumption peak recurs consistently |
| U.S. macro time series window | Jan 2007–2025 | Monthly series used for liquidity + spending trend analysis |
| Global COL dataset coverage | **21 countries**, **2000–2023 (24-year span)** | 500 structured country-year observations

---

## 📊 Visual Highlights

**Figure 1 —  U.S. Disposable Income (Nominal vs Real)**

![Nominal vs Real Disposable Income](/data-analysis/us-economy-analysis/assets/Nominal-vs-Real-Disposable-Income.png)

**<div align="center">Nominal income growth masks inflation-adjusted stagnation, highlighting post-pandemic purchasing power compression.</div>**

---

**Figure 2 — Real Personal Consumption During Recessions**

![Real Personal Consumption During Recessions](/data-analysis/us-economy-analysis/assets/Real-Personal-Consumption-During-Recessions.png)

**<div align="center"> Recession overlays reveal asymmetric recovery dynamics: prolonged contraction post-2008 versus rapid stimulus-accelerated rebound in 2020.</div>**

---

**Figure 3 — Income vs Consumption Efficiency (Behavioral View)**

![Income vs Consumption Efficiency](/data-analysis/us-economy-analysis/assets/Income-vs-Consumption-Efficiency-Behavioral-View.png)
**<div align="center"> Income and consumption maintain strong structural correlation, with temporary efficiency distortions during crisis periods.</div>**

---

**Figure 4 — Cost of Living vs Income by Region**

![Regional Cost of Living](/data-analysis/us-economy-analysis/assets/Regional-Cost-Structure-Comparison.png)
**<div align="center"> Housing remains the dominant global expenditure component, with tax and savings variability shaping disposable income capacity.</div>**

---

## Cost_of_Living_and_Income_Extended.csv

📘 **Data Dictionary**

- `Country`: Name of the country
- `Year`: Year of record
- `Average_Monthly_Income`: Average monthly income
- `Cost_of_Living`: Composite cost-of-living index
- `Housing_Cost_Percentage`: % of income spent on housing
- `Tax_Rate`: Effective income tax rate
- `Savings_Percentage`: % of income saved
- `Healthcare_Cost_Percentage`: % of income spent on healthcare
- `Education_Cost_Percentage`: % of income spent on education
- `Transportation_Cost_Percentage`: % of income spent on transportation
- `Region`: Geographic region

## US_Macro_Micro_Index.csv

 📘 **Data Dictionary**

| Column Name                                   | Description                                                                 |
|-----------------------------------------------|-----------------------------------------------------------------------------|
| `DATE`                                        | Monthly timestamp (2007–2025)                                               |
| `YEAR`                                        | Calendar year extracted from DATE                                           |
| `MONTH`                                       | Calendar month as a number (1–12)                                           |
| `MONTH_NAME`                                  | Calendar month as text (e.g., Jan, Feb)                                     |
| `QUARTER`                                     | Fiscal quarter for each date (e.g., Q1, Q2)                                 |
| `QUARTER_LABEL`                               | Label combining quarter and year (e.g., Q1 - 2007)                          |
| `Disposable_Personal_Income_Nominal`          | Total post-tax income (billions, current dollars, not inflation-adjusted)  |
| `Disposable_Personal_Income_Per_Capita`       | Post-tax income per person (chained 2017 dollars)                           |
| `Real_Personal_Consumption_Expenditures`      | Inflation-adjusted consumer spending (billions, chained 2017 dollars)       |
| `Total_Personal_Income`                       | Total pre-tax personal income (billions of dollars)                         |
| `RPCE_rolling`                                | 6-month rolling average of real consumption (created in notebook)          |
| `Spending_Efficiency`                         | Ratio of real spending to income (RPCE ÷ DPI)                              |

- **`nominal_disposable_personal_income_DSPI.csv`:** Total personal income after taxes (not adjusted for inflation). Useful for examining general liquidity available to the population.
  - **Units**: Billions of Dollars
- **`real_disposable_personal_income_percapita_A229RX0.csv`:** Inflation-adjusted income per person. Useful for measuring real purchasing power and income disparity analysis.
  - **Units**: Chained 2017 Dollars per Person 
- **`real_personal_consumption_expenditures_PCEC96.csv`:** Measures inflation-adjusted consumer spending. Useful for analyzing economic activity in areas like housing, food, and healthcare.
  - **Units**: Billions of Chained 2017 Dollars
- **`total_personal_income_pi.csv`:** Total income received before taxes. Useful for examining economic growth, employment, and estimating tax burden when compared to DSPI.
  - **Units**: Billions of Dollars

---

## 🔗 Tools & Resources

**Kaggle Dataset:**

- **Source:** [Cost of Living and Income (Extended)](https://www.kaggle.com/datasets/heidarmirhajisadati/regional-cost-of-living-analysis)

**Federal Reserve Economy Database:**

- [FRED - DSPI](https://fred.stlouisfed.org/series/DSPI)
  - **Series ID**: DSPI
- **Source**: [FRED - A229RX0](https://fred.stlouisfed.org/series/A229RX0)
  - **Series ID**: A229RX0
- **Source**: [FRED - PCEC96](https://fred.stlouisfed.org/series/PCEC96)
  - **Series ID**: PCEC96
- **Source**: [FRED - PI](https://fred.stlouisfed.org/series/PI)
  - **Series ID**: PI

- `DSPI`: Nominal Disposable Personal Income (Billions USD)
- `A229RX0`: Real Disposable Personal Income per Capita (Chained 2017 Dollars)
- `PCEC96`: Real Personal Consumption Expenditures (Billions, Chained 2017 Dollars)
- `PI`: Total Personal Income (Billions USD)

## Contributor Analytical Focus Areas

### Housing Affordability & Regional Cost Correlation (James Ceus)

- Identified moderate negative correlation between income and housing costs in North America (r ≈ -0.4).
- Proposed regression modeling for further quantification.

### Spending Distribution Analysis (Bakari Sibert)

- Explored distributional differences between income and cost-of-living.
- Observed disproportionate housing burden among lower-income households.

### Liquidity & Macro Indicators (Fari Lindo)

- Led analysis of DSPI, RDPI, PCEC, and PI trends.
- Identified widening nominal vs real income gap post-2021.

### Expenditure Trend Adaptation (Jessenia Diaz)

- Demonstrated V-shaped consumer spending recovery post-2008 and post-COVID.

### Global Comparative Cost Analysis (Sherla Zhagnay)

- Compared U.S. and European healthcare spending.
- Identified inflation influence on savings behavior.

---

## U.S. Liquidity & Purchasing Power Deep Dive (Lead Analysis)

### Income Trend Acceleration & Inflection Points

- Post-2008 recovery showed steady nominal growth (~4–6% annualized).
- 2020–2021 stimulus created abnormal income surge (~15% YoY spike).
- Post-2021 normalization period shows flattening in inflation-adjusted growth.

### Purchasing Power & Inflation

- Real Disposable Personal Income peaked in early 2021 before flattening.
- The widening gap between nominal and real income signals inflationary pressure.

### Liquidity Metrics

- Majority of Americans cluster in the \$40K--\$50K disposable income range.
- Limited upward mobility into higher income brackets indicates concentration. 

### Spending Behavior

- Real consumption expenditures show strong seasonal December peaks.
- July/August dips suggest mid-year liquidity compression.
- Post-crisis recoveries consistently show V-shaped rebounds.

---

## Strategic Recommendations

### For Movers & Job Seekers

- Plan relocations during Q3--Q4 for stronger economic activity.
- Evaluate inflation-adjusted salary rather than nominal compensation.
- Consider regional housing and healthcare burdens carefully.

### For Investors & Analysts

- Monitor RDPI vs DSPI divergence as an inflation stress indicator.
- Watch seasonal liquidity cycles when forecasting consumption trends.

---

## General Economic Insight

The U.S. economy demonstrates structural resilience with strong recovery
mechanisms. However, real income stagnation and cost pressures highlight
emerging liquidity constraints.

Economic preparedness and data-informed decision-making remain essential
for long-term financial stability.

---

## Directory Structure

    us-economy-analysis/
    │
    ├── assets/
    │   └── cohort_a_econ_banner.png
    │
    ├── data/
    │   ├── Cost_of_Living_and_Income_Extended.csv
    │   └── US_Macro_Micro_Index.csv
    │
    ├── notebooks/
    │   ├── Fari_eda.ipynb
    │   ├── James_eda.ipynb
    │   ├── Jessenia_eda.ipynb
    │   ├── Bakari_eda.ipynb
    │   └── Sherla_eda1.ipynb
    │
    ├── .gitignore
    ├── README.md
    └── requirements.txt

---

## Methods & Libraries

This analysis applies:

- Pearson correlation (`scipy.stats.pearsonr`)
- Time-series trend evaluation
- Distribution analysis
- Regional segmentation analysis
- Inflation-adjusted income comparison
- Seasonal decomposition observation

Libraries Used:

- `pandas`
- `numpy`
- `scipy`
- `matplotlib`
- `seaborn`
- `plotly.express`
- `math`

---

## How to Run

> Python 3.10+ recommended.

Clone the Portfolio Repository

```bash
git clone https://github.com/dataeden/fari-tech-portfolio.git
cd fari-tech-portfolio/us-economy-analysis
```

Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Notebooks

Open and run notebooks in:

- `notebooks/Bakari_eda.ipynb`
- `notebooks/Fari_eda.ipynb`
- `notebooks/James_eda.ipynb`
- `notebooks/Jessenia_eda.ipynb`
- `notebooks/Sherla_eda1.ipynb`

---

## Attribution

This project originated from a collaborative economic analysis initiative during The Knowledge House (TKH) Data Science fellowship.

All macro-liquidity modeling, statistical analysis, visualization architecture, and reporting narrative were independently refined, extended, and reconstructed as part of my professional DataInsideData™ portfolio.

---

## Contact

#### Fari Lindo • DataInsideData™

- [GitHub](https://github.com/dataeden)
- [Portfolio](https://datainsidedata.com)
- [LinkedIn](https://www.linkedin.com/in/fari-lindo/)  
- [Email](mailto:contact@datainsidedata.com)

*Tech Hands, a Science Mind, and a Heart for Community™*
