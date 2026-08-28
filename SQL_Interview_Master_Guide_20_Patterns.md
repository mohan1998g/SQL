# SQL Interview Master Guide - 20 Core Problem Solving Patterns

## How to Use This Guide
Most SQL interview questions are variants of a small set of patterns. Learn to identify the pattern first, then apply the corresponding technique.

---

# 1. Aggregation
**Use when:** Totals, averages, counts, min/max.

**Key Functions:** SUM, AVG, COUNT, MIN, MAX, GROUP BY, HAVING

**Examples (10):**
1. Total sales by region
2. Avg salary by department
3. Employee count by location
4. Max order value per customer
5. Min product price by category
6. Monthly revenue
7. Daily active users
8. Product order count
9. Orders by status
10. Avg movie rating

---
# 2. Filtering Pattern
**Use when:** Restricting rows.

**Key Clauses:** WHERE, HAVING

**Examples:**
1. Salary > average
2. Orders in last 30 days
3. Top-performing stores
4. Active users only
5. High-value customers
6. Failed transactions
7. Open tickets
8. Premium products
9. Expired subscriptions
10. Delayed shipments

---
# 3. Join Pattern
**Use when:** Data exists across tables.

**Key Concepts:** INNER, LEFT, RIGHT, FULL JOIN

**Examples:** Employee-department, customer-orders, invoice-payments, supplier-products, student-courses, shipment-orders, policy-claims, banking transactions, store-sales, CRM reporting.

---
# 4. Self Join Pattern
**Use when:** Comparing rows in the same table.

**Examples:** manager hierarchy, duplicate detection, salary comparison, peers, overlapping schedules, same-city customers, relationship mapping, ancestor-child mapping, seat swapping, account comparisons.

---
# 5. Subquery Pattern
**Use when:** One query depends on another.

**Examples:** above-average salary, second highest salary, largest order, department top earners, highest-rated products, best revenue month, no-order customers, top sellers, largest transaction, premium customers.

---
# 6. CTE Pattern
**Use when:** Breaking complex logic into steps.

**Examples:** reporting pipelines, session analysis, recursive hierarchy, ranking workflow, running totals, gap analysis, KPI calculation, transformations, cleansing, audit reports.

---
# 7. Ranking Pattern
**Functions:** ROW_NUMBER, RANK, DENSE_RANK

**Examples:** highest salary, second highest salary, top 3 earners, top products, customer ranking, class rank, movie rank, store rank, latest record, bottom performers.

---
# 8. Running Total Pattern
**Functions:** SUM() OVER()

**Examples:** cumulative sales, running profit, account balance, YTD sales, inventory tracking, subscriber growth, daily totals, ticket counts, attendance totals, expense tracking.

---
# 9. Moving Average Pattern
**Functions:** AVG() OVER(...ROWS BETWEEN...)

**Examples:** stock trends, forecasting, sales smoothing, demand planning, revenue trends, traffic analysis, KPI monitoring, sensor analytics, usage trends, retention trends.

---
# 10. Top-N Per Group Pattern
**Use when:** Need top K per category.

**Examples:** top 3 salaries per department, top products by category, latest order per customer, top stores by city, top students per class, best seller per month, largest transaction per account, best movie per genre, top employees per project, top customers per region.

---
# 11. Gaps and Islands Pattern
**Use when:** Consecutive sequences or missing values.

**Core Formula:**
```sql
value - ROW_NUMBER() OVER(ORDER BY value)
```

**Examples:** login streaks, attendance streaks, winning streaks, uptime periods, downtime periods, sales streaks, missing invoice IDs, missing order IDs, missing dates, subscription continuity.

---
# 12. Window Functions Pattern
**Functions:** LAG, LEAD, FIRST_VALUE, LAST_VALUE, SUM OVER

**Examples:** previous order, next transaction, trend analysis, growth %, cumulative values, customer journey, balance tracking, KPI comparisons, retention, audit trails.

---
# 13. Pivot / Unpivot Pattern
**Use when:** Rows ↔ Columns transformation.

**Examples:** monthly sales matrix, attendance report, survey output, product comparison, scorecards, KPI dashboard, revenue matrix, grade report, inventory report, quarterly reporting.

---
# 14. Recursive CTE Pattern
**Use when:** Hierarchies and trees.

**Examples:** org chart, folder hierarchy, category tree, bill of materials, reporting chain, graph traversal, ancestor lookup, descendants, path finding, genealogy.

---
# 15. Sequence Generation Pattern
**Use when:** Create number/date series.

**Examples:** calendar tables, missing dates, gap analysis, forecasting periods, simulation ranges, date expansion, reporting periods, testing data, invoice generation, recurring schedules.

---
# 16. Conditional Aggregation Pattern
**Template:**
```sql
SUM(CASE WHEN condition THEN 1 END)
```

**Examples:** gender counts, active users, open tickets, revenue by status, customer segmentation, KPI bands, category counts, SLA tracking, regional metrics, conversion metrics.

---
# 17. Sessionization Pattern
**Key Function:** LAG()

**Examples:** web sessions, app sessions, ATM sessions, shopping sessions, trading sessions, streaming sessions, helpdesk sessions, customer visits, sensor sessions, device usage.

---
# 18. Event Stream Analysis Pattern
**Examples:** first purchase, last purchase, previous event, next event, journey funnels, conversions, status changes, lifecycle analysis, clickstream analytics, subscription events.

---
# 19. Deduplication Pattern
**Template:**
```sql
ROW_NUMBER() OVER(PARTITION BY key ORDER BY date DESC)
```

**Examples:** duplicate customers, duplicate emails, duplicate products, duplicate logs, duplicate invoices, imported data cleanup, duplicate sessions, duplicate transactions, duplicate employees, duplicate contacts.

---
# 20. Change Detection Pattern
**Key Function:** LAG()

**Examples:** status transitions, salary changes, address changes, price updates, account changes, inventory changes, service interruptions, workflow transitions, customer tier movement, KPI movements.

---
# Pattern Recognition Cheat Sheet

- Totals → Aggregation
- Filter records → Filtering
- Multiple tables → Join
- Same table comparison → Self Join
- Query inside query → Subquery
- Multi-step logic → CTE
- Ranking needed → Ranking
- Cumulative values → Running Total
- Trend smoothing → Moving Average
- Top K per category → Top-N
- Consecutive records → Gaps & Islands
- Previous/Next row → Window Functions
- Rows to columns → Pivot
- Hierarchy → Recursive CTE
- Generate ranges → Sequence Generation
- Conditional metrics → Conditional Aggregation
- User activity grouping → Sessionization
- Event timelines → Event Stream Analysis
- Remove duplicates → Deduplication
- Detect state changes → Change Detection

# SQL Learning Roadmap

Beginner:
1. SELECT
2. WHERE
3. GROUP BY
4. HAVING
5. JOINS

Intermediate:
6. Subqueries
7. CASE WHEN
8. CTEs
9. Set Operators
10. Aggregations

Advanced:
11. Window Functions
12. Ranking
13. Running Totals
14. Top-N Per Group
15. Deduplication

Expert:
16. Gaps & Islands
17. Recursive CTE
18. Sessionization
19. Event Stream Analysis
20. Change Detection

## Final Advice
80-90% of SQL interview questions can be mapped to one of these 20 patterns. Focus on pattern recognition, then memorize the core SQL constructs that solve each pattern.
