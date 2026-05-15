# Advanced SQL Interview Problems (FAANG Level)

This document contains 20+ advanced SQL problems with solutions and sample datasets.

---

## Dataset (Sample Tables)

```sql
CREATE TABLE employees (
    id INT,
    name VARCHAR(50),
    department_id INT,
    salary INT,
    manager_id INT
);

CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    order_date DATE,
    amount INT
);

CREATE TABLE logins (
    user_id INT,
    login_date DATE
);
```

---

## Problems & Solutions

### 1. Top 3 Salaries per Department
```sql
SELECT * FROM (
  SELECT *, DENSE_RANK() OVER(PARTITION BY department_id ORDER BY salary DESC) r
  FROM employees
) t WHERE r <= 3;
```

### 2. Second Highest Salary
```sql
SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees);
```

### 3. Employees Earning Above Department Avg
```sql
SELECT * FROM employees e
WHERE salary > (
  SELECT AVG(salary) FROM employees WHERE department_id = e.department_id
);
```

### 4. Running Total
```sql
SELECT order_date, SUM(amount) OVER(ORDER BY order_date) FROM orders;
```

### 5. Consecutive Logins (3 days)
```sql
SELECT user_id FROM (
  SELECT user_id, login_date,
  login_date - ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY login_date) AS grp
  FROM logins
) t GROUP BY user_id, grp HAVING COUNT(*) >= 3;
```

### 6. Duplicate Emails
```sql
SELECT email, COUNT(*) FROM users GROUP BY email HAVING COUNT(*) > 1;
```

### 7. Manager with Highest Team Salary
```sql
SELECT manager_id, SUM(salary) total FROM employees GROUP BY manager_id ORDER BY total DESC LIMIT 1;
```

### 8. Customers with No Orders
```sql
SELECT * FROM customers c LEFT JOIN orders o ON c.id=o.customer_id WHERE o.customer_id IS NULL;
```

### 9. Rank Employees Globally
```sql
SELECT name, RANK() OVER(ORDER BY salary DESC) FROM employees;
```

### 10. Median Salary
```sql
SELECT AVG(salary) FROM (
 SELECT salary, ROW_NUMBER() OVER(ORDER BY salary) rn,
 COUNT(*) OVER() cnt FROM employees
) t WHERE rn IN (cnt/2, cnt/2+1);
```

### 11. First Order per Customer
```sql
SELECT * FROM (
 SELECT *, ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date) rn FROM orders
) t WHERE rn=1;
```

### 12. Last Order per Customer
```sql
SELECT * FROM (
 SELECT *, ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date DESC) rn FROM orders
) t WHERE rn=1;
```

### 13. Employees without Manager
```sql
SELECT * FROM employees WHERE manager_id IS NULL;
```

### 14. Department-wise Max Salary
```sql
SELECT department_id, MAX(salary) FROM employees GROUP BY department_id;
```

### 15. Pivot Example
```sql
SELECT product_id,
SUM(CASE WHEN quarter='Q1' THEN sales END) Q1
FROM sales GROUP BY product_id;
```

### 16. Gap Detection
```sql
SELECT id+1 FROM table1 t1 LEFT JOIN table1 t2 ON t1.id+1=t2.id WHERE t2.id IS NULL;
```

### 17. nth Highest Salary
```sql
SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 2;
```

### 18. Self Join Hierarchy
```sql
SELECT e.name, m.name manager FROM employees e LEFT JOIN employees m ON e.manager_id=m.id;
```

### 19. Daily Active Users
```sql
SELECT login_date, COUNT(DISTINCT user_id) FROM logins GROUP BY login_date;
```

### 20. Retention Analysis
```sql
SELECT l1.user_id FROM logins l1 JOIN logins l2 ON l1.user_id=l2.user_id AND l2.login_date=l1.login_date+1;
```

---

## ✅ Summary

This file contains advanced SQL patterns widely asked in FAANG interviews.
Practice step-by-step and understand window functions deeply.

