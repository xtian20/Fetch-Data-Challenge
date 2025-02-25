# Fetch-Data-Challenge

This repository contains a comprehensive analysis of the three datasets provided by Fetch Rewards: Products, Transactions, and Users. The Jupyter Notebook included in this repository demonstrates our exploration of the data quality issues, the execution of SQL queries addressing both closed-ended and open-ended business questions, and highlights key data trends observed in the datasets.

---

## Project Overview

The main objectives of this analysis are to:
- Identify and address data quality issues across the datasets.
- Answer critical business questions using SQL queries.
- Uncover actionable insights, including notable trends in user behavior.

---

## Repository Contents
1. **Fetch_Data_Chellenge.ipynb**

  - Data Quality Checks for the three datasets.
- Outstanding Questions & Next Steps.

  
2. **SQL_Queries.md**

   - SQL queries to answer the closed-ended and open-ended business questions.
  
3. **Email.pdf**

  - An email summarizing the results of the investigation, tailored for a product or business leader.

---

## Analysis & Insights

**Key Actionable Insight:**  
Our transaction data, covering June 2024 to early September 2024, reveals that receipt scans on weekdays consistently far outnumber those on weekends. This suggests that users are significantly more engaged during the workweek, likely incorporating scanning into their daily routines. One possible explanation is that during the summer season, many students and employees might be on vacation or enjoying a more relaxed weekend schedule, resulting in lower scanning activity on weekends.  
*Actionable Opportunity:*  
We can explore targeted weekend promotions or engagement strategies—such as exclusive rewards, contests, or special discounts—to stimulate weekend activity and drive overall growth.

---

## Outstanding Questions & Next Steps

- **Duplicate Receipt IDs:**  
  Should we always retain the nonzero FINAL_QUANTITY/FINAL_SALE values, or could zeros sometimes represent legitimate adjustments (e.g., returns or discounts)?

- **Outlier Transactions:**  
  Should wholesale or bulk purchase receipts be included in our analysis, or should they be treated as anomalies?

- **Duplicate BARCODEs in Products:**  
  Could discrepancies in duplicate BARCODE entries be due to rebranding or data entry errors? What is the best approach to validate the correct product-brand associations?

- **Potential Duplicate Users:**  
  How should we handle cases where multiple accounts might belong to a single individual?

Your insights on these questions will be invaluable as we refine our analysis and strategy.

---

## How to Use This Repository

1. **Requirements:**
   - Python 3.x
   - Jupyter Notebook or JupyterLab
   - Relevant Python libraries (e.g., pandas, SQL connectors)

2. **Getting Started:**
   - Clone the repository.
   - Open the provided Jupyter Notebook.
   - Follow the notebook cells sequentially to reproduce the analysis and review detailed findings.

3. **Additional Documentation:**
   - Refer to the notebook for in-depth code explanations, SQL queries, and further data quality assessments.

---

Thank you for reviewing our analysis. We look forward to your feedback and guidance.

