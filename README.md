# Fetch-Data-Challenge

This repository contains a comprehensive analysis of the three datasets provided by Fetch Rewards: Products, Transactions, and Users. The Jupyter Notebook included in this repository demonstrates our exploration of the data quality issues, the execution of SQL queries addressing both closed-ended and open-ended business questions, and highlights key data trends observed in the datasets.

---

## Project Overview

The main objectives of this analysis are to:
- Identify and address data quality issues across the datasets.
- Answer critical business questions using SQL queries.
- Uncover actionable insights, including notable trends in user behavior.

---

## Data Quality Checks

**Transactions Dataset:**
- **Missing BARCODE Values (12%):**  
  Approximately 12% of records lack BARCODE values, which are essential for joining with the Products dataset. These records were removed to ensure accurate mapping.
- **Duplicate Receipt IDs:**  
  We identified 25,389 instances where duplicate receipt IDs had conflicting FINAL_QUANTITY or FINAL_SALE values (one row with zero and another with a valid value). These were merged by retaining the nonzero values.
- **Exact Duplicates:**  
  171 duplicate rows were removed to avoid data inflation.
- **Date Inconsistencies:**  
  94 receipts with a SCAN_DATE earlier than the PURCHASE_DATE were removed due to probable data entry errors.
- **Outlier Transaction:**  
  One receipt with an unrealistic FINAL_SALE value of 276 was removed as an outlier.

**Products Dataset:**
- **CATEGORY_4 Field:**  
  Over 90% of records in this field are missing, suggesting that this level of product categorization is incomplete or inconsistently recorded. It has been excluded from the analysis.
- **Missing Manufacturer/Brand Information:**  
  Approximately 26% of records lack values in the MANUFACTURER and BRAND fields, which could affect brand-level insights.
- **BARCODE Integrity Issues:**  
  3,968 records missing BARCODE values were removed. Additionally, duplicate BARCODE entries with conflicting BRAND values were flagged for further validation.
- **Duplicate Rows:**  
  57 duplicate rows were removed to reduce redundancy.

**Users Dataset:**
- **GENDER Inconsistencies:**  
  Variations in gender entries (e.g., “non_binary” vs. “Non-Binary”) require standardization for accurate demographic segmentation.
- **Date Anomalies:**  
  Records where CREATED_DATE precedes BIRTH_DATE were removed to maintain data integrity.
- **Missing LANGUAGE Data:**  
  Approximately 30% of user records are missing LANGUAGE values.
- **Potential Duplicate Users:**  
  Cases where multiple accounts (with similar BIRTH_DATE, STATE, and LANGUAGE) may belong to the same individual have been flagged for further investigation.

For a more detailed analysis and the complete list of data quality checks, please refer to the attached Jupyter Notebook.

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

