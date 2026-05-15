Here is your requested content formatted as a **Markdown (.md) file** 👇

***

````markdown
# 🧠 Real Interview-Level Complex SQL Problems with Step-by-Step Solutions

---

## ✅ Problem 1: Find Top 3 Highest Paid Employees per Department

### 📌 Requirement
Return the top 3 highest-paid employees in each department.

---

### ✅ Solution

```sql
SELECT *
FROM (
    SELECT 
        e.*,
        DENSE_RANK() OVER (
            PARTITION BY department_id 
            ORDER BY salary DESC
        ) AS rank_num
    FROM employees e
) ranked
WHERE rank_num <= 3;
````

***

### 🔍 Explanation

1.  Use `DENSE_RANK()` window function
2.  Partition by `department_id`
3.  Order salaries in descending order
4.  Filter ranks <= 3

***

## ✅ Problem 2: Find Customers Who Purchased Every Product

### 📌 Requirement

Identify customers who have purchased **all available products**.

***

### ✅ Solution

```sql
SELECT customer_id
FROM purchases
GROUP BY customer_id
HAVING COUNT(DISTINCT product_id) = (
    SELECT COUNT(*) FROM products
);
```

***

### 🔍 Explanation

1.  Count distinct products purchased by each customer
2.  Compare with total products in the products table
3.  Match → customer bought all products

***

## ✅ Problem 3: Detect Duplicate Records

### 📌 Requirement

Find duplicate email entries in a table.

***

### ✅ Solution

```sql
SELECT email, COUNT(*) AS duplicate_count
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

***

### 🔍 Explanation

1.  Group by email
2.  Count occurrences
3.  Filter where count > 1

***

## ✅ Problem 4: Get Second Highest Salary

### 📌 Requirement

Find the second highest salary from employees table.

***

### ✅ Solution

```sql
SELECT MAX(salary) AS second_highest_salary
FROM employees
WHERE salary < (
    SELECT MAX(salary) FROM employees
);
```

***

### 🔍 Explanation

1.  Get highest salary
2.  Filter values less than that
3.  Take max of remaining

***

## ✅ Problem 5: Running Total of Sales

### 📌 Requirement

Calculate cumulative sales per day.

***

### ✅ Solution

```sql
SELECT 
    sale_date,
    SUM(amount) OVER (
        ORDER BY sale_date
    ) AS running_total
FROM sales;
```

***

### 🔍 Explanation

1.  Use window function `SUM()`
2.  Order by date
3.  Calculates cumulative total

***

## ✅ Problem 6: Find Employees Without Managers

### 📌 Requirement

Get employees who do not have a manager.

***

### ✅ Solution

```sql
SELECT *
FROM employees
WHERE manager_id IS NULL;
```

***

### 🔍 Explanation

1.  Employees with `NULL` manager\_id
2.  Represent top-level employees

***

## ✅ Problem 7: Find Highest Sales per Region

### 📌 Requirement

Get highest sale in each region.

***

### ✅ Solution

```sql
SELECT region, MAX(sales_amount) AS highest_sale
FROM sales
GROUP BY region;
```

***

### 🔍 Explanation

1.  Group data by region
2.  Retrieve maximum sales

***

## ✅ Problem 8: Identify Gaps in Sequence

### 📌 Requirement

Find missing order IDs in a sequence.

***

### ✅ Solution

```sql
SELECT t1.order_id + 1 AS missing_id
FROM orders t1
LEFT JOIN orders t2 
    ON t1.order_id + 1 = t2.order_id
WHERE t2.order_id IS NULL;
```

***

### 🔍 Explanation

1.  Self join orders table
2.  Compare current ID with next ID
3.  Missing value identified

***

## ✅ Problem 9: Pivot Data (Row to Column)

### 📌 Requirement

Convert rows into columns for quarterly sales.

***

### ✅ Solution

```sql
SELECT 
    product_id,
    SUM(CASE WHEN quarter = 'Q1' THEN sales ELSE 0 END) AS Q1,
    SUM(CASE WHEN quarter = 'Q2' THEN sales ELSE 0 END) AS Q2,
    SUM(CASE WHEN quarter = 'Q3' THEN sales ELSE 0 END) AS Q3,
    SUM(CASE WHEN quarter = 'Q4' THEN sales ELSE 0 END) AS Q4
FROM sales
GROUP BY product_id;
```

***

### 🔍 Explanation

1.  Use conditional aggregation
2.  Map rows into columns
3.  Aggregate per product

***

## ✅ Problem 10: Find Consecutive Login Days

### 📌 Requirement

Identify users who logged in for 3 consecutive days.

***

### ✅ Solution

```sql
SELECT user_id
FROM (
    SELECT 
        user_id,
        login_date,
        login_date - INTERVAL '1 day' * ROW_NUMBER() 
            OVER (PARTITION BY user_id ORDER BY login_date) AS grp
    FROM logins
) t
GROUP BY user_id, grp
HAVING COUNT(*) >= 3;
```

***

### 🔍 Explanation

1.  Assign row numbers per user
2.  Normalize dates using row\_number trick
3.  Group consecutive dates
4.  Filter groups with 3+ records

***

# 🚀 Final Tips

*   Break problems into smaller components
*   Use CTEs for readability
*   Master window functions
*   Validate results step-by-step

***
