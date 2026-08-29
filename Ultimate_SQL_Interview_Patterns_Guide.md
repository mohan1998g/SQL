# Ultimate SQL Interview Patterns Guide

## Purpose
This guide helps recognize SQL problem patterns instead of memorizing queries.

---

# 1. Aggregation Pattern

## Recognition
Need totals, averages, counts, min/max.

## Key Functions
SUM, AVG, COUNT, MIN, MAX, GROUP BY, HAVING

## Template
```sql
SELECT category, SUM(amount)
FROM sales
GROUP BY category;
```

## 10 Interview Problems
1. Total sales by region
2. Average salary by department
3. Count employees by grade
4. Max order value per customer
5. Min price per category
6. Monthly revenue
7. Daily active users
8. Product sales count
9. Orders per status
10. Average movie rating

## Common Mistakes
- Missing GROUP BY columns
- Using WHERE instead of HAVING

---

# 2. Join Pattern

## Recognition
Data is spread across multiple tables.

## Key Concepts
INNER, LEFT, RIGHT, FULL, CROSS JOIN

## Template
```sql
SELECT *
FROM orders o
JOIN customers c
ON o.customer_id=c.customer_id;
```

## 10 Problems
1. Customer orders
2. Employee departments
3. Product suppliers
4. Student courses
5. Orders without customers
6. Customers without orders
7. Invoice payments
8. Shipment tracking
9. Banking transactions
10. Multi-table reporting

---

# 3. Self Join Pattern

## Recognition
Same table compared with itself.

## Template
```sql
SELECT e.name,m.name
FROM employee e
JOIN employee m
ON e.manager_id=m.emp_id;
```

## 10 Problems
1. Employee-manager
2. Salary comparison
3. Hierarchy mapping
4. Duplicate detection
5. Same city customers
6. Peer comparison
7. Schedule overlap
8. Consecutive records
9. Relative ranking
10. Relationship matching

---

# 4. Subquery Pattern

## Recognition
Need result of one query inside another.

## 10 Problems
1. Salary above average
2. Products above avg price
3. Highest order amount
4. Top customer purchases
5. Second highest salary
6. Customers with no orders
7. Above average departments
8. Best revenue month
9. Top revenue products
10. Largest transaction

---

# 5. CTE Pattern

## Recognition
Complex logic that benefits from step-by-step decomposition.

## Template
```sql
WITH cte AS (
 SELECT * FROM orders
)
SELECT * FROM cte;
```

## 10 Problems
1. Multi-stage reporting
2. Recursive hierarchy
3. Running totals
4. Ranking pipelines
5. Session generation
6. Gap analysis
7. Streak detection
8. Data cleansing
9. Nested calculations
10. KPI dashboards

---

# 6. Ranking Pattern

## Key Functions
ROW_NUMBER, RANK, DENSE_RANK

## Template
```sql
ROW_NUMBER() OVER(PARTITION BY dept ORDER BY salary DESC)
```

## 10 Problems
1. First highest salary
2. Second highest salary
3. Top 3 salaries
4. Best-selling products
5. Customer ranking
6. Student ranking
7. Movie ratings
8. Store ranking
9. Latest record
10. Bottom performers

---

# 7. Window Functions Pattern

## Key Functions
LAG, LEAD, FIRST_VALUE, LAST_VALUE, SUM OVER

## 10 Problems
1. Running revenue
2. Running profit
3. Cumulative users
4. Moving average
5. Closing balance
6. Previous order amount
7. Next transaction
8. Daily trend analysis
9. Month-over-month growth
10. KPI tracking

---

# 8. Top-N Per Group Pattern

## Recognition
Top K records inside each category.

## Template
```sql
ROW_NUMBER() OVER(PARTITION BY dept ORDER BY salary DESC)
```

## 10 Problems
1. Top 3 salaries by department
2. Top 5 customers by region
3. Top products by category
4. Latest order by customer
5. Best movie by genre
6. Best student by class
7. Highest monthly order
8. Largest account transaction
9. Best performing store
10. Top employee per project

---

# 9. Deduplication Pattern

## Recognition
Need unique records.

## Template
```sql
ROW_NUMBER() OVER(PARTITION BY email ORDER BY created_date DESC)
```

## 10 Problems
1. Duplicate customers
2. Duplicate emails
3. Duplicate products
4. Duplicate logs
5. Duplicate transactions
6. Duplicate sessions
7. Duplicate invoices
8. Duplicate phone numbers
9. Duplicate employee records
10. Imported data cleanup

---

# 10. Gaps and Islands Pattern

## Recognition
Consecutive sequences or missing values.

## Core Formula
```sql
value - ROW_NUMBER() OVER(ORDER BY value)
```

## 10 Problems
1. Login streaks
2. Attendance streaks
3. Winning streaks
4. Sales streaks
5. KPI streaks
6. Machine uptime
7. Machine downtime
8. Missing invoice IDs
9. Missing order IDs
10. Missing dates

---

# 11. Conditional Aggregation Pattern

## Template
```sql
SUM(CASE WHEN status='ACTIVE' THEN 1 END)
```

## Problems
1. Gender counts
2. Active users
3. Revenue by status
4. Open tickets
5. Closed tickets
6. Product category counts
7. Sales band reports
8. Regional metrics
9. Monthly KPI reports
10. Customer segmentation

---

# 12. Recursive CTE Pattern

## Recognition
Hierarchical/tree structures.

## Problems
1. Org hierarchy
2. Folder hierarchy
3. Category tree
4. Bill of materials
5. Reporting chain
6. Graph traversal
7. Descendants
8. Ancestors
9. Path generation
10. Multi-level rollups

---

# 13. Sessionization Pattern

## Key Function
LAG()

## Problems
1. User sessions
2. Browser sessions
3. ATM usage sessions
4. Shopping sessions
5. App sessions
6. Trading sessions
7. Call center sessions
8. Device sessions
9. Sensor sessions
10. Streaming activity

---

# 14. Event Stream Analysis Pattern

## Problems
1. First purchase
2. Last purchase
3. Previous event
4. Next event
5. Status changes
6. Journey funnel
7. Cart conversion
8. Customer lifecycle
9. Subscription events
10. Clickstream analysis

---

# 15. Pivot and Unpivot Pattern

## Problems
1. Monthly sales matrix
2. Quarterly reports
3. Attendance matrix
4. Product comparison
5. KPI dashboards
6. Survey reports
7. Revenue pivot
8. Headcount reports
9. Grade reports
10. Inventory matrix

---

# SQL Interview Roadmap

## Beginner
- SELECT
- WHERE
- ORDER BY
- GROUP BY
- HAVING
- JOINS

## Intermediate
- Subqueries
- CASE WHEN
- CTEs
- Set Operators

## Advanced
- Window Functions
- Ranking
- Running Totals
- Top-N Per Group
- Deduplication

## Expert
- Gaps & Islands
- Recursive CTE
- Sessionization
- Event Stream Analysis
- Time-Series Analytics

---

# Pattern Recognition Cheat Sheet

| Requirement | Pattern |
|------------|----------|
| Totals | Aggregation |
| Multiple tables | Join |
| Same table compare | Self Join |
| Above average | Subquery |
| Complex steps | CTE |
| Ranking | Rank Functions |
| Running total | Window Function |
| Top K in group | Top-N Pattern |
| Remove duplicates | Deduplication |
| Consecutive records | Gaps & Islands |
| Hierarchy | Recursive CTE |
| User activity groups | Sessionization |
| Sequence of events | Event Stream |
| Rows to columns | Pivot |

# Final Advice

Most SQL interview questions fall into these 15 patterns. Focus on recognizing patterns first, then learning the associated SQL techniques and window functions.
