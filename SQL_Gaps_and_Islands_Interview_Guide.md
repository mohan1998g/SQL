# SQL Gaps and Islands Approach - Complete Interview Guide

## What is the Gaps and Islands Problem?

- **Island**: A continuous sequence of values (dates, numbers, IDs).
- **Gap**: Missing values between sequences.

Example:

```text
1,2,3,5,6,9,10
```

Islands:

```text
1,2,3
5,6
9,10
```

Gaps:

```text
4
7,8
```

---

# Core Concept

## ROW_NUMBER() Pattern

```sql
SELECT
    num,
    num - ROW_NUMBER() OVER(ORDER BY num) AS grp
FROM Numbers;
```

Consecutive values produce the same group key.

## LAG() Pattern

```sql
SELECT
    num,
    LAG(num) OVER(ORDER BY num) AS prev_num
FROM Numbers;
```

A new island starts when:

```sql
num - prev_num > 1
```

---

# Sample Island Solution

```sql
WITH cte AS
(
    SELECT
        attendance_date,
        attendance_date -
        ROW_NUMBER() OVER(ORDER BY attendance_date) grp
    FROM employee_attendance
)
SELECT
    MIN(attendance_date) start_date,
    MAX(attendance_date) end_date,
    COUNT(*) streak_days
FROM cte
GROUP BY grp;
```

---

# Sample Gap Solution

```sql
WITH cte AS
(
    SELECT
        num,
        LAG(num) OVER(ORDER BY num) prev_num
    FROM Numbers
)
SELECT
    prev_num + 1 AS gap_start,
    num - 1 AS gap_end
FROM cte
WHERE num - prev_num > 1;
```

---

# Finding Every Missing Number

```sql
WITH nums AS
(
    SELECT 1 n
    UNION ALL
    SELECT n + 1
    FROM nums
    WHERE n < 100
)
SELECT n
FROM nums
WHERE n NOT IN
(
    SELECT num FROM Numbers
);
```

---

# Interview Formula Cheat Sheet

## Islands

```sql
value - ROW_NUMBER()
```

or

```sql
date_column - ROW_NUMBER()
```

## Gaps

```sql
LAG()
LEAD()
```

## Longest Streak

```sql
GROUP BY grp
COUNT(*)
```

---

# 20+ Interview Problems Based on Gaps & Islands

## 1. Longest Consecutive Employee Attendance Streak
Find longest continuous attendance period.

## 2. Consecutive Login Days
Identify user login streaks.

## 3. Missing Invoice Numbers
Find missing invoice IDs.

## 4. Continuous Customer Purchase Days
Determine purchasing streaks.

## 5. Missing Order IDs
Locate gaps in order sequences.

## 6. Machine Uptime Periods
Find continuous RUNNING status intervals.

## 7. Machine Downtime Periods
Find continuous DOWN intervals.

## 8. Consecutive Sales Days
Identify sales streak periods.

## 9. Longest Sales Streak
Find maximum number of consecutive sales days.

## 10. Missing Dates in Transaction History
Detect absent transaction dates.

## 11. Website Active Sessions
Group continuous activity periods.

## 12. Patient Hospital Stay Periods
Calculate uninterrupted stay ranges.

## 13. Consecutive Project Working Days
Find work streaks for employees.

## 14. Consecutive Attendance Above Threshold
Find periods where attendance exceeds target.

## 15. Stock Price Rising Streaks
Identify consecutive increase periods.

## 16. Stock Price Falling Streaks
Identify consecutive decline periods.

## 17. Consecutive Days Meeting KPI
Find KPI achievement streaks.

## 18. Missing Ticket Numbers
Detect skipped ticket sequences.

## 19. Continuous Subscription Periods
Group uninterrupted subscription durations.

## 20. Consecutive Shipment Days
Calculate shipment streaks.

## 21. Missing Employee IDs
Find gaps after employee onboarding.

## 22. Consecutive Exam Attendance
Track student attendance streaks.

## 23. Continuous Sensor Readings
Find uninterrupted reading intervals.

## 24. Consecutive Days Without Incidents
Calculate safety streaks.

## 25. Longest Winning Streak
Identify maximum consecutive wins.

---

# Frequently Asked Interview Queries

### Find Longest Login Streak

```sql
WITH cte AS
(
    SELECT
        user_id,
        login_date,
        DATEADD(day,
            -ROW_NUMBER() OVER(
                PARTITION BY user_id
                ORDER BY login_date
            ),
            login_date) grp
    FROM user_logins
)
SELECT
    user_id,
    COUNT(*) streak
FROM cte
GROUP BY user_id, grp;
```

### Find Missing IDs

```sql
WITH cte AS
(
    SELECT
        id,
        LAG(id) OVER(ORDER BY id) prev_id
    FROM orders
)
SELECT
    prev_id + 1,
    id - 1
FROM cte
WHERE id - prev_id > 1;
```

### Find Consecutive Dates

```sql
SELECT
    order_date,
    order_date - ROW_NUMBER() OVER(ORDER BY order_date) grp
FROM orders;
```

---

# Performance Tips

Create supporting indexes:

```sql
CREATE INDEX idx_orders
ON orders(order_date);
```

or

```sql
CREATE INDEX idx_emp
ON employee_attendance(emp_id, attendance_date);
```

---

# Common Mistakes

1. Not sorting before ROW_NUMBER().
2. Duplicate dates causing incorrect streaks.
3. Ignoring PARTITION BY.
4. Missing NULL handling in LAG().
5. Using gaps logic when islands logic is needed.

---

# Quick Revision Notes

### Island

```text
Continuous sequence
```

### Gap

```text
Missing values between sequences
```

### Most Important Pattern

```sql
value - ROW_NUMBER()
```

### Most Important Functions

```sql
ROW_NUMBER()
LAG()
LEAD()
DENSE_RANK()
RANK()
```

### Most Asked Interview Topics

- Login streaks
- Attendance streaks
- Missing IDs
- Missing dates
- Sales streaks
- Order sequences
- Machine uptime
- Machine downtime
- Winning streaks
- Continuous subscriptions

---

# Final Summary

The Gaps and Islands approach is one of the most important advanced SQL interview concepts. Use ROW_NUMBER() to form islands, LAG()/LEAD() to identify gaps, and aggregate grouped records to calculate streak lengths, continuous ranges, missing values, uptime periods, attendance periods, sales streaks, and many other real-world analytical scenarios.
