# Closed-Ended Questions
## What are the top 5 brands by receipts scanned among users 21 and over?

```
SELECT 
    p.CATEGORY_1
  , p.BRAND
  , COUNT(DISTINCT t.RECEIPT_ID) AS num_receipts
FROM transactions as t 
JOIN users as u 
ON t.USER_ID = u.ID
JOIN products as p 
ON t.BARCODE = p.BARCODE
WHERE 1=1
AND BIRTH_DATE <= DATE('now', '-21 years') -- Users aged 21 and over
GROUP BY 1,2
ORDER BY 3 DESC
LIMIT 5
```

## What are the top 5 brands by sales among users that have had their account for at least six months?

```
SELECT 
    p.CATEGORY_1
  , p.BRAND
  , SUM(t.FINAL_SALE) AS total_sales
FROM transactions as t 
JOIN users as u 
ON t.USER_ID = u.ID
JOIN products as p 
ON t.BARCODE = p.BARCODE
WHERE 1=1
AND DATE('now', '-6 months') >= CREATED_DATE -- Users that have had their account for at least six months
GROUP BY 1,2
ORDER BY 3 DESC
LIMIT 5
```


## What is the percentage of sales in the Health & Wellness category by generation?

```
WITH CTE AS (
SELECT 
    u.ID
  , u.BIRTH_DATE
  , CASE 
        WHEN CAST(strftime('%Y', BIRTH_DATE) AS INTEGER) BETWEEN 1928 AND 1945 THEN 'Silent Generation'
        WHEN CAST(strftime('%Y', BIRTH_DATE) AS INTEGER) BETWEEN 1946 AND 1964 THEN 'Baby Boomers'
        WHEN CAST(strftime('%Y', BIRTH_DATE) AS INTEGER) BETWEEN 1965 AND 1980 THEN 'Gen X'
        WHEN CAST(strftime('%Y', BIRTH_DATE) AS INTEGER) BETWEEN 1981 AND 1996 THEN 'Millennials'
        WHEN CAST(strftime('%Y', BIRTH_DATE) AS INTEGER) BETWEEN 1997 AND 2012 THEN 'Gen Z'
        WHEN CAST(strftime('%Y', BIRTH_DATE) AS INTEGER) >= 2013 THEN 'Gen Alpha'
        ELSE 'Unknown'
    END AS generation
  , t.FINAL_SALE
FROM users as u
JOIN transactions as t 
ON u.ID = t.USER_ID
JOIN products as p 
ON t.BARCODE = p.BARCODE
WHERE p.CATEGORY_1 = 'Health & Wellness'
)
SELECT 
    c.generation
  , ROUND(SUM(c.FINAL_SALE)*100 / (SELECT SUM(FINAL_SALE) FROM CTE), 2) AS health_wellness_percentage
FROM CTE as c
GROUP BY 1
ORDER BY 2 DESC
```


# Open-Ended Questions
## Who are Fetch’s power users?
Fetch is a reward-based platform where users earn points by scanning and uploading receipts. The goal is to identify power users—those who frequently upload receipts, engage consistently over time, and demonstrate long-term retention. These high-engagement users play a critical role in the platform’s success by driving activity, increasing transaction volume, and contributing to overall user retention.

To measure power user behavior, let's first define them as users who **regularly scan and upload receipts**, indicating **high transaction volume**. Therefore, **Total Receipts Uploaded per User per Year** will be the key metric for identifying power users.

```
SELECT 
    t.USER_ID
  , strftime('%Y', t.SCAN_DATE) AS year
  , COUNT(DISTINCT t.RECEIPT_ID) AS total_receipts_uploaded
FROM transactions as t 
GROUP BY 1,2
ORDER BY 2, 3 DESC
```


## Which is the leading brand in the Dips & Salsa category?

To identify the leading brand in the Dips & Salsa category, we first define clearly what "leading" means from a product strategy perspective. In other words, what does success look like for a brand within this category?

We can consider the following product-focused criteria:
1. **Sales Volume (Revenue)**:
    * Identify the brand generating the highest overall sales revenue, indicating strong consumer demand or higher price points.
2. **Purchase Frequency (Unit Sold)**:
    * Find the brand with the most units sold, highlighting strong consumer preference and repeat purchases.
3. **Customer Reach (Number of Unique Customers)**: 
    * Determine which brand reaches the broadest audience, indicating widespread popularity or strong brand recognition.
4. **Transaction Presence (Number of Transactions)**:
    * Assess which brand appears most frequently on scanned receipts, suggesting regular consumer engagement.
5. **Consistency Over Time (Stability)**:
    * Identify brands maintaining steady performance across multiple months, demonstrating reliable and sustained consumer loyalty rather than short-term spikes.


Assuming at this time, stores are looking for brands with **strong brand recognition**, the best metrics should focus on **how many unique customers purchase each brand**. 

```
WITH CTE AS (
SELECT 
    p.CATEGORY_2
  , p.BRAND
  , COUNT(DISTINCT t.USER_ID) AS unique_customers
  , DENSE_RANK() OVER(ORDER BY COUNT(DISTINCT t.USER_ID)) AS rnk
FROM transactions as t
JOIN products as p 
ON t.BARCODE = p.BARCODE
WHERE p.CATEGORY_2 = 'Dips & Salsa'
GROUP BY 1,2
)

SELECT 
    cte.CATEGORY_2
  , cte.BRAND
  , cte.unique_customers
FROM CTE
WHERE rnk=1
```

## At what percent has Fetch grown year over year?

As a receipt-based rewards platform, Fetch’s success is driven by **user activity**, **transaction volume**, and **engagement levels**. To assess growth, we need to define the KPIs that reflect the platform’s expansion and increasing user value.

Here are four critical dimensions of Fetch’s growth:
1. **User Growth** - Measuring Expansion of the User Base
    *  A larger user base increases data collection, brand partnerships, and revenue potential. 
2. **Transaction Growth** – Measuring Usage Frequency
    *  More transactions scanned indicate higher engagement, stronger platform habit-building, and increased data volume for analytics.
3. **Sales Growth** – Measuring Economic Impact
    *  Higher spending levels suggest greater adoption of Fetch by power users, stronger partner brand engagement, and increased monetization opportunities.
4. **Engagement Growth** – Measuring User Retention & Activity
    *  A rising engagement rate indicates that users find value in continuously using the platform, leading to long-term retention and brand loyalty.

Assume Fetch's primary goal is to **scale its user base**, the most important metric is **User Growth**—tracking the growth rate of active users tells us if more people are adopting the platform.


```
WITH active_users_per_year AS (
SELECT 
    strftime('%Y', t.SCAN_DATE) AS year
  , COUNT(DISTINCT t.USER_ID) AS active_users
FROM transactions as t
GROUP BY 1
)


SELECT 
    au.year as current_year
  , au.active_users as current_active_users
  , au2.active_users as previous_active_users
  , ROUND((au.active_users - au2.active_users)*100/au2.active_users, 2) AS growth_rate
FROM active_users_per_year as au
LEFT JOIN active_users_per_year as au2 
ON au.year = au2.year - 1
WHERE au2.year IS NOT NULL
```