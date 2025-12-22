Got it — here’s **everything you can do with `COUNT()` in SQL**, organized clearly from basics to advanced, with examples.

---

## 1. `COUNT(*)` — count all rows

```sql
COUNT(*)
```

* Counts **every row**
* Includes rows with `NULL` values
* Fast and optimized by most databases

```sql
SELECT COUNT(*) FROM Orders;
```

---

## 2. `COUNT(column)` — count non-NULL values

```sql
COUNT(price)
```

* Counts rows where `price IS NOT NULL`

```sql
SELECT COUNT(price) FROM Orders;
```

---

## 3. `COUNT(DISTINCT column)` — count unique values

```sql
COUNT(DISTINCT customer_id)
```

* Ignores duplicates
* Ignores `NULL`

```sql
SELECT COUNT(DISTINCT customer_id) FROM Orders;
```

---

## 4. `COUNT(expression)` — count non-NULL expressions

```sql
COUNT(price * quantity)
```

* Counts rows where the expression result is NOT NULL

```sql
SELECT COUNT(price * quantity) FROM Orders;
```

---

## 5. `COUNT(CASE WHEN ...)` — conditional counting

```sql
COUNT(CASE WHEN status = 'shipped' THEN 1 END)
```

* Counts only rows that meet the condition
* `ELSE NULL` is implicit

```sql
SELECT
  COUNT(*) AS total,
  COUNT(CASE WHEN status = 'shipped' THEN 1 END) AS shipped
FROM Orders;
```

---

## 6. `COUNT(IF(...))` (MySQL-specific)

```sql
COUNT(IF(status = 'shipped', 1, NULL))
```

* Same idea as `CASE`
* Works in MySQL

---

## 7. `COUNT(*) with GROUP BY`

```sql
SELECT customer_id, COUNT(*)
FROM Orders
GROUP BY customer_id;
```

* Counts rows **per group**

---

## 8. `COUNT(DISTINCT ...) with GROUP BY`

```sql
SELECT customer_id, COUNT(DISTINCT product_id)
FROM Orders
GROUP BY customer_id;
```

* Counts unique values **per group**

---

## 9. Window function: `COUNT() OVER ()`

```sql
COUNT(*) OVER ()
```

* Returns total row count **on every row**

```sql
SELECT
  order_id,
  COUNT(*) OVER () AS total_orders
FROM Orders;
```

---

## 10. Window function: `COUNT() OVER (PARTITION BY ...)`

```sql
COUNT(*) OVER (PARTITION BY customer_id)
```

* Count per group **without collapsing rows**

```sql
SELECT
  order_id,
  customer_id,
  COUNT(*) OVER (PARTITION BY customer_id) AS orders_per_customer
FROM Orders;
```

---

## 11. Window function with `ORDER BY`

```sql
COUNT(*) OVER (ORDER BY order_date)
```

* Running (cumulative) count

```sql
SELECT
  order_date,
  COUNT(*) OVER (ORDER BY order_date) AS running_total
FROM Orders;
```

---

## 12. Filtered window count (PostgreSQL / SQL Server)

```sql
COUNT(*) FILTER (WHERE status = 'shipped')
```

* Cleaner conditional counting (not in MySQL)

---

## 13. `COUNT` in `HAVING`

```sql
HAVING COUNT(*) > 5
```

* Filters groups based on count

```sql
SELECT customer_id
FROM Orders
GROUP BY customer_id
HAVING COUNT(*) >= 3;
```

---

## 14. `COUNT` with `JOIN`

```sql
SELECT c.customer_id, COUNT(o.order_id)
FROM Customers c
LEFT JOIN Orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id;
```

* Counts matching rows
* `LEFT JOIN` keeps zero-count rows

---

## 15. `COUNT` vs `SUM`

```sql
COUNT(CASE WHEN condition THEN 1 END)
SUM(CASE WHEN condition THEN 1 ELSE 0 END)
```

* Functionally equivalent for conditional counting
* `COUNT` ignores `NULL`
* `SUM` requires `ELSE 0`

---

## 16. Things `COUNT` cannot do ❌

```sql
COUNT(col1, col2)   -- invalid
COUNT(col > 10)     -- invalid in most DBs
COUNT(SELECT ...)   -- invalid
```

---

## Mental model (important)

> **`COUNT()` counts rows, not values.**
> The argument only decides **which rows qualify**.

---

## Quick cheat sheet

| Syntax                 | What it counts              |
| ---------------------- | --------------------------- |
| `COUNT(*)`             | All rows                    |
| `COUNT(col)`           | Non-NULL column values      |
| `COUNT(DISTINCT col)`  | Unique non-NULL values      |
| `COUNT(expr)`          | Non-NULL expression results |
| `COUNT(CASE WHEN ...)` | Conditional rows            |
| `COUNT() OVER (...)`   | Windowed counts             |

---

If you want next, I can:

* Show **common interview traps**
* Compare `COUNT(*)` vs `COUNT(1)`
* Explain **performance differences**
* Give **practice problems with answers**

Just say 👍
