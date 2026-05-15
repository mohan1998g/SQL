# 🧠 FAANG SQL Interview Preparation (50+ Problems + Case Studies)

---

# ✅ SECTION 1: 50+ SQL QUESTIONS WITH DIFFICULTY

## 🟢 EASY (1–15)

### 1. Find all employees
SELECT * FROM employees;

### 2. Count total employees
SELECT COUNT(*) FROM employees;

### 3. Highest salary
SELECT MAX(salary) FROM employees;

### 4. Lowest salary
SELECT MIN(salary) FROM employees;

### 5. Average salary
SELECT AVG(salary) FROM employees;

### 6. Employees in a department
SELECT * FROM employees WHERE department_id = 10;

### 7. Sort employees by salary
SELECT * FROM employees ORDER BY salary DESC;

### 8. Find NULL manager
SELECT * FROM employees WHERE manager_id IS NULL;

### 9. Distinct departments
SELECT DISTINCT department_id FROM employees;

### 10. Count per department
SELECT department_id, COUNT(*) FROM employees GROUP BY department_id;

### 11. Employees above salary threshold
SELECT * FROM employees WHERE salary > 50000;

### 12. Employees hired after date
SELECT * FROM employees WHERE hire_date > '2023-01-01';

### 13. Limit rows
SELECT * FROM employees LIMIT 10;

### 14. Offset usage
SELECT * FROM employees LIMIT 10 OFFSET 5;

### 15. Basic join
SELECT e.name, d.name FROM employees e JOIN departments d ON e.department_id = d.id;

---

## 🟡 MEDIUM (16–35)

### 16. Second highest salary
SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees);

### 17. Top 3 salaries per dept
SELECT * FROM (
 SELECT *, DENSE_RANK() OVER(PARTITION BY department_id ORDER BY salary DESC) r
 FROM employees) t WHERE r <= 3;

### 18. Employee above dept avg
SELECT * FROM employees e
WHERE salary > (SELECT AVG(salary) FROM employees WHERE department_id=e.department_id);

### 19. Running total
SELECT order_date, SUM(amount) OVER(ORDER BY order_date) FROM orders;

### 20. Row numbering
SELECT ROW_NUMBER() OVER(ORDER BY salary DESC) FROM employees;

### 21. Rank employees
SELECT RANK() OVER(ORDER BY salary DESC) FROM employees;

### 22. Dense rank
SELECT DENSE_RANK() OVER(ORDER BY salary DESC) FROM employees;

### 23. Duplicate records
SELECT email, COUNT(*) FROM users GROUP BY email HAVING COUNT(*) > 1;

### 24. First order
SELECT * FROM (
SELECT *, ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date) r FROM orders) t WHERE r=1;

### 25. Last order
SELECT * FROM (
SELECT *, ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date DESC) r FROM orders) t WHERE r=1;

### 26. Customers with no orders
SELECT * FROM customers c LEFT JOIN orders o ON c.id=o.customer_id WHERE o.id IS NULL;

### 27. Self join hierarchy
SELECT e.name, m.name FROM employees e LEFT JOIN employees m ON e.manager_id=m.id;

### 28. Gap detection
SELECT id+1 FROM t1 LEFT JOIN t1 t2 ON t1.id+1=t2.id WHERE t2.id IS NULL;

### 29. Pivot data
SELECT SUM(CASE WHEN quarter='Q1' THEN sales END) FROM sales;

### 30. Daily active users
SELECT login_date, COUNT(DISTINCT user_id) FROM logins GROUP BY login_date;

### 31. Moving average
SELECT AVG(amount) OVER(ORDER BY order_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) FROM orders;

### 32. Nth highest salary
SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 4;

### 33. Median
SELECT AVG(salary) FROM (
 SELECT salary, ROW_NUMBER() OVER() rn, COUNT(*) OVER() cnt FROM employees
) t WHERE rn IN (cnt/2, cnt/2+1);

### 34. Group filtering
SELECT department_id FROM employees GROUP BY department_id HAVING COUNT(*) > 5;

### 35. Join 3 tables
SELECT * FROM a JOIN b ON a.id=b.id JOIN c ON b.id=c.id;

---

## 🔴 HARD (36–55)

### 36. Consecutive logins
SELECT user_id FROM (
 SELECT user_id, login_date,
 login_date - ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY login_date) grp
 FROM logins
) t GROUP BY user_id, grp HAVING COUNT(*)>=3;

### 37. Retention analysis
SELECT l1.user_id FROM logins l1 JOIN logins l2
ON l1.user_id=l2.user_id AND l2.login_date=l1.login_date+1;

### 38. Cohort analysis
-- cohort grouping by signup month

### 39. Top customer revenue
SELECT customer_id, SUM(amount) FROM orders GROUP BY customer_id ORDER BY 2 DESC LIMIT 1;

### 40. Cumulative share
SELECT amount/SUM(amount) OVER() FROM orders;

### 41. Percentile
SELECT PERCENT_RANK() OVER(ORDER BY salary) FROM employees;

### 42. Recursive hierarchy
WITH RECURSIVE t AS (
 SELECT id, manager_id FROM employees WHERE manager_id IS NULL
 UNION ALL
 SELECT e.id, e.manager_id FROM employees e JOIN t ON e.manager_id = t.id
) SELECT * FROM t;

### 43. Split strings (DB specific)

### 44. JSON parsing (DB specific)

### 45. Window lag
SELECT LAG(salary) OVER(ORDER BY salary) FROM employees;

### 46. Window lead
SELECT LEAD(salary) OVER(ORDER BY salary) FROM employees;

### 47. Sessionization
-- user session grouping based on time gaps

### 48. Funnel analysis
-- user journey tracking

### 49. Top N per group optimized

### 50. Multi-step CTE pipeline

### 51. Ranking with ties handling

### 52. Anti-join pattern
SELECT * FROM a WHERE NOT EXISTS (SELECT 1 FROM b WHERE a.id=b.id);

### 53. Semi-join pattern
SELECT * FROM a WHERE EXISTS (SELECT 1 FROM b WHERE a.id=b.id);

### 54. Window frame tuning

### 55. Complex aggregation cube

---

# ✅ SECTION 2: REAL FAANG CASE STUDIES

## 📦 Amazon Case Study: Customer Retention

### Problem
Find customers who made repeat purchases within 7 days.

### Solution
SELECT DISTINCT o1.customer_id
FROM orders o1
JOIN orders o2
ON o1.customer_id=o2.customer_id
AND o2.order_date BETWEEN o1.order_date AND o1.order_date + 7;

---

## 🔍 Google Case Study: Search Engagement

### Problem
Measure daily active users and retention.

### Solution
SELECT login_date, COUNT(DISTINCT user_id)
FROM logins
GROUP BY login_date;

---

## 📱 Meta Case Study: User Growth Funnel

### Problem
Track users from signup to purchase.

### Solution
-- Step-based funnel using joins or events table

---

## 🎬 Netflix Case Study: Watch Time Ranking

### Problem
Top watched shows per region.

### Solution
SELECT * FROM (
 SELECT show_id, region, SUM(watch_time),
 RANK() OVER(PARTITION BY region ORDER BY SUM(watch_time) DESC) r
 FROM views GROUP BY show_id, region
) t WHERE r=1;

---

# ✅ SUMMARY

- Covers 50+ FAANG-level SQL problems
- Includes Easy, Medium, Hard categorization
- Real interview case studies
- Strong focus on window functions, joins, analytics

