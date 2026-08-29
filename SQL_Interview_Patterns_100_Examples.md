# SQL Problem Solving Patterns - Interview Master Guide

This guide covers 10 major SQL patterns and 10 interview-style problems for each pattern.

## 1. Aggregation Pattern
1. Total sales by region
2. Average salary by department
3. Employee count per location
4. Highest order value per customer
5. Lowest price per category
6. Monthly revenue
7. Daily active users
8. Product sales count
9. Orders per status
10. Average rating per movie

## 2. Join Pattern
1. Employee and department details
2. Customer and order details
3. Products with suppliers
4. Students with courses
5. Orders without customers
6. Customers without orders
7. Match invoices to payments
8. Employee-manager mapping
9. Shipment and order mapping
10. Multi-table reporting

## 3. Self Join Pattern
1. Employees earning more than manager
2. Employee-manager hierarchy
3. Find duplicates
4. Compare consecutive dates
5. Find peer employees
6. Same-city customers
7. Detect overlapping schedules
8. Compare current vs previous records
9. Pairwise combinations
10. Team-member relationships

## 4. Subquery Pattern
1. Salary above average
2. Products above category average
3. Top customer purchases
4. Largest order per customer
5. Second highest salary
6. Customers with no orders
7. Departments above average headcount
8. Maximum revenue month
9. Employees in top salary band
10. Highest-rated products

## 5. CTE Pattern
1. Modular reporting queries
2. Multi-step aggregations
3. Recursive hierarchy traversal
4. Running calculations
5. Data cleansing workflow
6. Streak calculations
7. Session building
8. Ranking pipelines
9. Gap detection
10. Complex transformations

## 6. Ranking Pattern
1. Highest salary
2. Second highest salary
3. Top 3 earners per department
4. Top products by sales
5. Top customers by revenue
6. Rank movies by rating
7. Rank stores by sales
8. Competitive leaderboard
9. Latest record per entity
10. Bottom performers

## 7. Running Total & Window Pattern
1. Running revenue
2. Running profit
3. Cumulative users
4. Year-to-date sales
5. Rolling inventory
6. Moving average
7. Running balance
8. Cumulative attendance
9. Running ticket count
10. Rolling KPI

## 8. Top-N Per Group Pattern
1. Top 3 salaries per department
2. Top 5 customers per region
3. Latest order per customer
4. Top-selling products per category
5. Best movie per genre
6. Top students per class
7. Highest order per month
8. Latest transaction per account
9. Top stores per city
10. Top employees per project

## 9. Deduplication Pattern
1. Remove duplicate customers
2. Remove duplicate emails
3. Keep latest transaction
4. Keep earliest order
5. Deduplicate phone numbers
6. Remove duplicate logs
7. Unique product catalog
8. Merge customer records
9. Remove duplicate sessions
10. Clean imported data

## 10. Gaps and Islands Pattern
1. Attendance streaks
2. Login streaks
3. Sales streaks
4. Winning streaks
5. Machine uptime periods
6. Machine downtime periods
7. Missing invoice numbers
8. Missing order IDs
9. Missing dates
10. Subscription continuity

---

# Key Techniques

## Aggregation
```sql
GROUP BY
SUM()
AVG()
COUNT()
```

## Ranking
```sql
ROW_NUMBER()
RANK()
DENSE_RANK()
```

## Window Functions
```sql
SUM() OVER()
AVG() OVER()
LAG()
LEAD()
```

## Gaps and Islands
```sql
value - ROW_NUMBER() OVER(ORDER BY value)
```

```sql
LAG()
LEAD()
```

# Learning Roadmap
1. Aggregation
2. Joins
3. Subqueries
4. CTEs
5. Ranking
6. Window Functions
7. Top-N Per Group
8. Deduplication
9. Gaps and Islands
10. Recursive CTEs

# Interview Preparation Summary
Mastering these 10 patterns covers the majority of SQL interview questions asked across service and product companies. The most important advanced topics are Window Functions, Ranking, Top-N Per Group, Deduplication, and Gaps & Islands.
