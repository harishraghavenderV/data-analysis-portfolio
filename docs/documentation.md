# Data Science & Analysis Portfolio - Documentation

This document provides in-depth technical documentation covering the methodologies, machine learning pipeline details, statistical tests, and domain recommendations implemented across the portfolio.

---

## 1. Project 1: Retail Sales Analysis

### Analysis Questions
1. What are the key transactional trends over the fiscal year?
2. Does weekend sales promotion provide a statistically significant uplift?
3. Which product category leads revenue and profit contributions?
4. How do daily transactions distribute by hour?

### Technical Implementation & Methods
*   **Data Preparation:** Timestamps are parsed and indexed. Sales and profit are scaled to represent an average transaction value of ₹1,458.
*   **Statistical Testing:** We apply a **Two-Sample Independent t-test** to compare average sales on weekends (Saturday/Sunday) under promotional influence against weekdays.
    *   *Hypothesis:* $H_0: \mu_{weekend} = \mu_{weekday}$ vs $H_1: \mu_{weekend} \neq \mu_{weekday}$.
    *   *Result:* Rejected the null hypothesis ($p < 0.001$), confirming a statistically significant sales boost of **40.0%** on weekends.
*   **Machine Learning Modeling:**
    *   *Clustering:* **K-Means Clustering** applied to RFM (Recency, Frequency, Monetary) metrics to segment customers into value tiers. Features are normalized using `StandardScaler`.
    *   *Forecasting:* A daily time-series forecast model fitted using **Ordinary Least Squares (OLS) Linear Regression** with a linear trend, day-of-week dummy features, and a December peak indicator variable.

### Business Recommendations
1.  **Inventory Optimization:** Increase Electronics inventory levels by 20% to leverage its 45% profit margin.
2.  **Staffing Allocation:** Deploy peak staffing hours between 5 PM and 8 PM (which captures 60.0% of daily transactions).
3.  **Loyalty Program:** Target the top 20% customers contributing 65.0% of total revenue.

---

## 2. Project 2: Healthcare Data Analysis

### Analysis Questions
1. Does admission day (weekday vs. weekend) affect patient treatment costs?
2. Do telemedicine follow-up programs decrease readmission risk?
3. Which clinical departments show the highest satisfaction rates?

### Technical Implementation & Methods
*   **Cost Analysis:** We evaluate average treatment cost across admission days using a **Two-Sample t-test** which confirms weekend costs are **30.0%** higher due to staff premiums.
*   **Readmission Risk Factors:** Telemedicine follow-up reduces readmission by 45%. Patients discharged early ($\le 3$ days length of stay) show a 25% lower readmission rate, indicating optimal recovery at home for low-severity cases.
*   **Machine Learning Modeling:**
    *   **Random Forest Classifier** trained on patient demographics (`Age`), clinical metrics (`LengthOfStay`, `StaffToPatientRatio`, `TreatmentCost`), and follow-up indicators (`TelemedicineFollowUp`) to predict readmission risk (0 or 1).
    *   *Validation:* Evaluated using ROC Area Under Curve (AUC), showing robust classification performance.

### Clinical Recommendations
1.  **Workflow Audits:** Perform operational workflow audits for weekend clinical resources to contain the 30% cost premium.
2.  **Telemedicine Deployment:** Standardize telemedicine check-ins for all discharged patients.

---

## 3. Project 3: Sports Analytics

### Analysis Questions
1. Can match outcome be predicted using possession and match dynamics?
2. How do goals and player performance metrics correlate with player position?

### Technical Implementation & Methods
*   **Exploratory Data Analysis:** Highlighted team standings, verifying the Thunderbolts' 65% win probability dominance.
*   **Correlation Analysis:** A heatmap correlates goals, assists, tackles, pass accuracy, and ratings. Defenders show positive correlation between tackle counts and ratings, whereas forwards' ratings correlate with goals and assists.
*   **Machine Learning Modeling:**
    *   **Random Forest Classifier** trained to predict match outcome (Win, Loss, Draw) using match features (`Possession_TeamA`, `Shots_TeamA`, `WinProbability`).
    *   *Accuracy:* Validation check shows **90.1%** classification accuracy.

### Tactical Recommendations
1.  **Player Scouting:** Identify midfielders with high pass accuracy metrics and forwards with a high Goals-to-Rating efficiency score.
2.  **Tactical Evaluation:** Use the outcome model to simulate tactics (possession vs. direct counter-attacks) to optimize win chance.

---

## 4. Project 4: Financial Market Analysis

### Analysis Questions
1. How do daily stock returns correlate across different tickers?
2. What is the optimized portfolio weights combination to maximize Sharpe Ratio?

### Technical Implementation & Methods
*   **Trend Analysis:** Pivot close prices to calculate daily returns. Volatility (risk) is computed as the annualized standard deviation.
*   **Modern Portfolio Theory (MPT):**
    *   Simulated 5,000 random weight portfolios to map out the **Efficient Frontier**.
    *   Determined the **Maximum Sharpe Ratio** portfolio (highest return per unit of risk) and the **Minimum Volatility** portfolio.
    *   *Outputs:* MSFT and AAPL occupy the highest portfolio allocations due to high drift and controlled volatility. TSLA is minimized due to extreme historical volatility (45.0%).

### Financial Recommendations
1.  **Asset Weights:** Follow the Sharpe optimized capital allocation (overweighting MSFT and AAPL).
2.  **Quarterly Rebalancing:** Adjust asset weights quarterly to track shifts along the Efficient Frontier.

---

## 5. Project 5: E-commerce Analytics

### Analysis Questions
1. How can customer lifetime value (CLV) be profiled across categories?
2. What are the key predictors of customer churn?

### Technical Implementation & Methods
*   **CLV Profiling:** E-commerce spend analysis shows Electronics and Home Decor categories yield the highest total customer lifetime spend.
*   **Customer Segmentation:** K-Means clustering segments customers into four core value groups: Champions, Loyal, At-Risk, and Lost.
*   **Machine Learning Modeling:**
    *   **Random Forest Classifier** trained to identify churn risk status.
    *   **Feature Importance** extraction shows **Recency** (days since last purchase) has the absolute highest influence on churn risk.

### Marketing Recommendations
1.  **Retention Alert:** Target the 320 high-risk churn customers identified with reactivation campaigns (such as a 20% discount coupon).
2.  **Cross-selling:** Cross-sell Electronics and Home Decor items to clothing segments to increase CLV.
