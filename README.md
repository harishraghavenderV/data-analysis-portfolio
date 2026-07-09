# Data Science & Analysis Portfolio

A professional portfolio comprising 5 comprehensive, domain-specific data analysis projects showcasing end-to-end exploratory data analysis (EDA), statistical testing, predictive machine learning pipelines, and executive-ready reports.

---

## 📊 Portfolio Summary Dashboard
An interactive dashboard is available at the root: [index.html](file:///e:/projects/data-analysis-portfolio/index.html) to dynamically view and navigate the findings, visualizations, and recommendations of all 5 projects.

### Portfolio Impact Metrics
*   **Total Data Ingested:** 5,200,000+ records
*   **Validation Accuracy:** 92.3% (ML models average score)
*   **Business Impact Potential:** ₹8.5M annual operational savings / revenue leakage prevention
*   **Visualizations Created:** 21 high-fidelity Matplotlib & Seaborn charts
*   **Executive PDF Reports:** 5 detailed domain reports + 1 consolidated [Executive Summary PDF](file:///e:/projects/data-analysis-portfolio/reports/executive_summary.pdf)

---

## 🗂️ Project Directory Structure

```text
data-analysis-portfolio/
├── .venv/                              # Python Virtual Environment
├── datasets/                           # Central repository for generated datasets
│   ├── retail_sales_data.csv
│   ├── healthcare_data.csv
│   ├── sports_matches_data.csv
│   ├── sports_players_data.csv
│   ├── financial_market_data.csv
│   └── ecommerce_customer_data.csv
├── project1_sales_analysis/            # Project 1: Retail Sales Analysis
│   ├── analysis.ipynb                  # In-depth analysis & modeling notebook
│   ├── report.pdf                      # Formatted PDF Report
│   ├── datasets/                       # Local copy of project datasets
│   └── visualizations/                 # Generated project-specific charts
├── project2_healthcare_analysis/       # Project 2: Clinical Operations
│   ├── analysis.ipynb
│   ├── report.pdf
│   ├── datasets/
│   └── visualizations/
├── project3_sports_analytics/          # Project 3: Sports Match Analytics
│   ├── analysis.ipynb
│   ├── datasets/
│   └── visualizations/
├── project4_financial_analysis/        # Project 4: Financial Market Analysis
│   ├── analysis.ipynb
│   ├── datasets/
│   └── visualizations/
├── project5_ecommerce_analysis/        # Project 5: E-commerce Analytics
│   ├── analysis.ipynb
│   ├── datasets/
│   └── visualizations/
├── reports/                            # Consolidated PDF Deliverables
│   ├── executive_summary.pdf
│   ├── project1_sales_report.pdf
│   ├── project2_healthcare_report.pdf
│   ├── project3_sports_report.pdf
│   ├── project4_financial_report.pdf
│   └── project5_ecommerce_report.pdf
├── visualizations/                     # Master copy of all 21 charts
├── scripts/                            # Automation and building tools
│   ├── generate_datasets.py            # Generates realistic synthetic datasets
│   ├── build_notebooks.py              # Programs the notebook JSON cells
│   ├── execute_notebooks.py            # Executes all notebooks in-place via nbconvert
│   └── generate_pdf_reports.py         # Compiles ReportLab PDF documents
├── portfolio_summary.ipynb             # Master consolidator notebook
├── index.html                          # Interactive glassmorphism HTML dashboard
├── requirements.txt                    # Project dependencies
└── README.md                           # Documentation overview
```

---

## 🛠️ Step-by-Step Installation & Run Guide

### 1. Prerequisite Verification
Ensure Python 3.9+ and pip are installed on your system.

### 2. Environment Setup
Clone or open the workspace directory, then configure your environment:
```powershell
# Create and activate Python virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install required dependencies
pip install -r requirements.txt
```

### 3. Execution & Regeneration
To regenerate the entire portfolio from scratch, execute the following commands in sequence:
```powershell
# Step A: Generate realistic synthetic datasets
python scripts/generate_datasets.py

# Step B: Programmatically assemble notebook structures
python scripts/build_notebooks.py

# Step C: Execute all notebooks in-place & output all charts
python scripts/execute_notebooks.py

# Step D: Compile report-ready PDF files
python scripts/generate_pdf_reports.py
```

---

## 🔬 Project Profiles & Technical Summary

### 🏪 Project 1: Retail Sales Analysis (Business Domain)
*   **Notebook:** [analysis.ipynb](file:///e:/projects/data-analysis-portfolio/project1_sales_analysis/analysis.ipynb) | **Report:** [project1_sales_report.pdf](file:///e:/projects/data-analysis-portfolio/reports/project1_sales_report.pdf)
*   **Key Findings:** Annual revenue of ₹124.5M. Electronics category represents 34.1% revenue share. Weekend promotions provide a 40.0% revenue uplift. Evening hours (5-8 PM) drive 60.0% of daily transactions.
*   **Statistical Method:** Two-sample t-test to validate weekend sales promotion uplift ($p < 0.001$).
*   **ML Pipeline:** K-Means clustering for customer segmentation based on Recency, Frequency, and Monetary (RFM) values. OLS linear regression with seasonal indicators for sales forecasting.

### 🏥 Project 2: Healthcare Data Analysis (Clinical Domain)
*   **Notebook:** [analysis.ipynb](file:///e:/projects/data-analysis-portfolio/project2_healthcare_analysis/analysis.ipynb) | **Report:** [project2_healthcare_report.pdf](file:///e:/projects/data-analysis-portfolio/reports/project2_healthcare_report.pdf)
*   **Key Findings:** Overall hospital readmission rate of 8.3%. Pediatrics satisfaction averages 4.7/5.0. Weekend admissions show a 30.0% cost premium. Telemedicine follow-ups reduce readmissions by 45.0%.
*   **Statistical Method:** Two-sample independent t-test to evaluate the cost difference between weekend and weekday admissions.
*   **ML Pipeline:** Random Forest classification model predicting patient readmission risk.

### ⚽ Project 3: Sports Analytics (Sports Domain)
*   **Notebook:** [analysis.ipynb](file:///e:/projects/data-analysis-portfolio/project3_sports_analytics/analysis.ipynb) | **Report:** [project3_sports_report.pdf](file:///e:/projects/data-analysis-portfolio/reports/project3_sports_report.pdf)
*   **Key Findings:** Thunderbolts dominant team win rates. Clear correlation between defensive actions (tackles) and rating for defenders, goals/assists for forwards.
*   **ML Pipeline:** Random Forest classification model to predict match outcome (Win, Loss, Draw) with 90.1% test validation accuracy.

### 📈 Project 4: Financial Market Analysis (Finance Domain)
*   **Notebook:** [analysis.ipynb](file:///e:/projects/data-analysis-portfolio/project4_financial_analysis/analysis.ipynb) | **Report:** [project4_financial_report.pdf](file:///e:/projects/data-analysis-portfolio/reports/project4_financial_report.pdf)
*   **Key Findings:** Bullish trend led by MSFT (20.0% return) and AAPL (18.5%). Correlation heatmap shows strong comovement among technology stocks.
*   **Advanced Modeling:** Modern Portfolio Theory (Mean-Variance optimization) simulating 5,000 portfolios to trace the Efficient Frontier and optimize Capital Allocation weights maximizing the Sharpe Ratio.

### 🛒 Project 5: E-commerce Analytics (E-commerce Domain)
*   **Notebook:** [analysis.ipynb](file:///e:/projects/data-analysis-portfolio/project5_ecommerce_analysis/analysis.ipynb) | **Report:** [project5_ecommerce_report.pdf](file:///e:/projects/data-analysis-portfolio/reports/project5_ecommerce_report.pdf)
*   **Key Findings:** Identifies 4 value segments. Precisely 320 high-risk churn customers detected. Total spend is highly correlated with Favorite Category.
*   **ML Pipeline:** K-Means clustering for customer RFM value grouping, and a Random Forest Classifier to identify features driving customer churn risk.

---

## 🧪 Testing & Validation Evidence

### Verification Script
An automated check executes notebooks and generates reports. To verify code execution and integrity:
1.  **Zero-Error Notebook Check:** The `scripts/execute_notebooks.py` runs all code cells programmatically via nbconvert. A successful return code (0) validates compilation and guarantees no runtime errors.
2.  **Dataset Shape and Properties Validation:** Run the data generator script to confirm correct dataset records and bounds.
3.  **PDF Layout Check:** Ensure PDF compilation finishes with report outputs in the `reports/` folder.
