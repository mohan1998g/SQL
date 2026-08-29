# SQL LEAD() and LAG() Complete Guide

## What are LEAD() and LAG()?

`LEAD()` and `LAG()` are SQL window functions that allow you to access data from another row without using a self-join.

- `LAG()` looks at a previous row. - the values comes down
- `LEAD()` looks at a subsequent (next) row. - the values goes up

These functions are commonly used for:
- Trend analysis
- Comparing current and previous values
- Comparing current and next values
- Detecting consecutive values
- Calculating differences between rows

---

## Syntax

### LAG()

```sql
LAG(column_name, offset, default_value)
OVER (ORDER BY column_name)
```

### LEAD()

```sql
LEAD(column_name, offset, default_value)
OVER (ORDER BY column_name)
```

### Parameters

- `column_name` : Value to retrieve.
- `offset` : Number of rows backward/forward. Default = 1.
- `default_value` : Returned when the requested row does not exist.

---

## Sample Table

```text
Employees

+--------+----------+--------+
| emp_id | emp_name | salary |
+--------+----------+--------+
| 1      | John     | 5000   |
| 2      | Mary     | 6000   |
| 3      | David    | 5500   |
| 4      | Smith    | 7000   |
+--------+----------+--------+
```

---

## Using LEAD and LAG Together

```sql
SELECT
    emp_id,
    emp_name,
    salary,
    LAG(salary, 1) OVER (ORDER BY emp_id) AS lag_salary,
    LEAD(salary, 1) OVER (ORDER BY emp_id) AS lead_salary
FROM Employees;
```

### Output

```text
+--------+----------+--------+------------+-------------+
| emp_id | emp_name | salary | lag_salary | lead_salary |
+--------+----------+--------+------------+-------------+
| 1      | John     | 5000   | NULL       | 6000        |
| 2      | Mary     | 6000   | 5000       | 5500        |
| 3      | David    | 5500   | 6000       | 7000        |
| 4      | Smith    | 7000   | 5500       | NULL        |
+--------+----------+--------+------------+-------------+
```

---

## Visual Representation

```text
Previous Row <---------------- Current Row ----------------> Next Row

       LAG()                       |                      LEAD()
         |                          |                         |
         V                          V                         V

+------+--------+
| ID=1 | 5000   |
+------+--------+
         |
         V
+------+--------+
| ID=2 | 6000   |
+------+--------+
         |
         V
+------+--------+
| ID=3 | 5500   |
+------+--------+
         |
         V
+------+--------+
| ID=4 | 7000   |
+------+--------+
```

For employee ID=3:

```text
lag_salary  = 6000
salary      = 5500
lead_salary = 7000
```

---

## Offset Example

```sql
SELECT
    emp_id,
    salary,
    LAG(salary, 2) OVER (ORDER BY emp_id)  AS lag_2_rows,
    LEAD(salary, 2) OVER (ORDER BY emp_id) AS lead_2_rows
FROM Employees;
```

### Output

```text
+--------+--------+------------+-------------+
| emp_id | salary | lag_2_rows | lead_2_rows |
+--------+--------+------------+-------------+
| 1      | 5000   | NULL       | 5500        |
| 2      | 6000   | NULL       | 7000        |
| 3      | 5500   | 5000       | NULL        |
| 4      | 7000   | 6000       | NULL        |
+--------+--------+------------+-------------+
```

---

## Default Value Example

```sql
SELECT
    emp_id,
    salary,
    LAG(salary,1,0) OVER (ORDER BY emp_id) AS previous_salary
FROM Employees;
```

Output:

```text
emp_id salary previous_salary
------ ------ ----------------
1      5000   0
2      6000   5000
3      5500   6000
4      7000   5500
```

---

## Calculate Difference from Previous Row

```sql
SELECT
    emp_id,
    salary,
    salary - LAG(salary,1) OVER (ORDER BY emp_id) AS salary_difference
FROM Employees;
```

Output:

```text
John   -> NULL
Mary   -> +1000
David  -> -500
Smith  -> +1500
```

---

## Consecutive Numbers Problem Using LAG

```sql
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT
        num,
        LAG(num,1) OVER (ORDER BY id) AS prev1,
        LAG(num,2) OVER (ORDER BY id) AS prev2
    FROM Logs
) t
WHERE num = prev1
  AND num = prev2;
```

Logic:

```text
Current Row = 1
Previous Row = 1
2 Rows Back = 1

1 = 1 = 1
=> Three consecutive occurrences found
```

---

## LEAD vs LAG Quick Comparison

```text
+----------------------+------------------+------------------+
| Feature              | LAG()            | LEAD()           |
+----------------------+------------------+------------------+
| Direction            | Backward         | Forward          |
| Looks At             | Previous Row     | Next Row         |
| Default Offset       | 1                | 1                |
| Trend Analysis       | Yes              | Yes              |
| Running Comparisons  | Yes              | Yes              |
+----------------------+------------------+------------------+
```

---

## Interview Tips

1. LEAD and LAG are window functions.
2. They do not require self-joins.
3. ORDER BY inside OVER() is mandatory for meaningful results.
4. Offset defaults to 1.
5. Frequently used in analytics and reporting queries.
6. Useful for comparing current, previous, and next records.
