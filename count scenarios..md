In SQL, **`COUNT` doesn’t take “variables” in the programming sense**. It takes **arguments (expressions)**. What you can put inside `COUNT()` determines *what* gets counted.

Here are the valid forms and what they mean 👇

---

## 1. `COUNT(*)`

```sql
COUNT(*)
```

**Counts all rows** in the result set.

* Includes rows with `NULL` values
* Most common and safest form

Example:

```sql
SELECT COUNT(*) FROM Customer;
```

---

## 2. `COUNT(column_name)`

```sql
COUNT(product_key)
```

**Counts non-NULL values** in that column.

* Rows where `product_key` is `NULL` are ignored

Example:

```sql
SELECT COUNT(product_key) FROM Customer;
```

---

## 3. `COUNT(DISTINCT column_name)`

```sql
COUNT(DISTINCT product_key)
```

**Counts unique non-NULL values**.

Example:

```sql
SELECT COUNT(DISTINCT product_key) FROM Customer;
```

---

## 4. `COUNT(expression)`

```sql
COUNT(product_key + 1)
```

Counts rows where the **expression is not NULL**.

Example:

```sql
SELECT COUNT(price * quantity) FROM Sales;
```

If either `price` or `quantity` is `NULL`, that row is not counted.

---

## 5. `COUNT(CASE WHEN ...)`

```sql
COUNT(CASE WHEN status = 'completed' THEN 1 END)
```

Counts rows where the condition is true.

Equivalent to:

```sql
SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END)
```

---

## What you **cannot** put in `COUNT()`

❌ Multiple columns:

```sql
COUNT(col1, col2) -- invalid
```

❌ Boolean conditions directly:

```sql
COUNT(col > 10) -- invalid in most SQL dialects
```

---

## Summary table

| Syntax                 | Counts                         |
| ---------------------- | ------------------------------ |
| `COUNT(*)`             | All rows                       |
| `COUNT(col)`           | Non-NULL values in `col`       |
| `COUNT(DISTINCT col)`  | Unique non-NULL values         |
| `COUNT(expr)`          | Non-NULL results of expression |
| `COUNT(CASE WHEN ...)` | Rows matching condition        |

---

## Key takeaway

> **`COUNT` counts rows, not values.**
> What changes is *which rows qualify* to be counted.

If you want, I can also explain:

* `COUNT` vs `SUM`
* How `COUNT` works with `GROUP BY`
* Window-function versions like `COUNT() OVER (...)`

Just tell me 🙂
