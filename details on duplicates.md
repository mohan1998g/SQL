Short answer: **No, there is no built-in `DUPLICATES()` function in SQL.**
But SQL gives you **standard patterns** to *find*, *count*, and *remove* duplicates.

Below are **all the common ways**, depending on what you want.

---

## 1. Find duplicate values (most common)

### Find values that appear more than once

```sql
SELECT col, COUNT(*) AS cnt
FROM table_name
GROUP BY col
HAVING COUNT(*) > 1;
```

---

## 2. Find duplicate rows (multiple columns)

```sql
SELECT col1, col2, COUNT(*)
FROM table_name
GROUP BY col1, col2
HAVING COUNT(*) > 1;
```

---

## 3. See the actual duplicate rows

### Using `IN`

```sql
SELECT *
FROM table_name
WHERE col IN (
    SELECT col
    FROM table_name
    GROUP BY col
    HAVING COUNT(*) > 1
);
```

---

## 4. Find duplicates using window functions (best & modern)

```sql
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY col
               ORDER BY id
           ) AS rn
    FROM table_name
) t
WHERE rn > 1;
```

* Keeps first row (`rn = 1`)
* Flags all additional duplicates

---

## 5. Count duplicates per row

```sql
SELECT *,
       COUNT(*) OVER (PARTITION BY col) AS duplicate_count
FROM table_name;
```

---

## 6. Remove duplicates (keep one row)

### MySQL / PostgreSQL / SQL Server

```sql
DELETE FROM table_name
WHERE id NOT IN (
    SELECT MIN(id)
    FROM table_name
    GROUP BY col
);
```

---

### Using window functions (safer)

```sql
DELETE FROM table_name
WHERE id IN (
    SELECT id
    FROM (
        SELECT id,
               ROW_NUMBER() OVER (
                   PARTITION BY col
                   ORDER BY id
               ) AS rn
        FROM table_name
    ) t
    WHERE rn > 1
);
```

---

## 7. Prevent duplicates (best solution)

### Use constraints

```sql
ALTER TABLE table_name
ADD CONSTRAINT unique_col UNIQUE (col);
```

### Or composite uniqueness

```sql
UNIQUE (col1, col2)
```

---

## 8. `DISTINCT` is NOT a duplicates function

```sql
SELECT DISTINCT col FROM table_name;
```

* Removes duplicates in output
* Does **not** detect or delete them

---

## Summary table

| Goal                | SQL pattern                        |
| ------------------- | ---------------------------------- |
| Find duplicates     | `GROUP BY ... HAVING COUNT(*) > 1` |
| Show duplicate rows | `ROW_NUMBER() OVER (...)`          |
| Count duplicates    | `COUNT(*) OVER (...)`              |
| Delete duplicates   | `ROW_NUMBER() + DELETE`            |
| Prevent duplicates  | `UNIQUE` constraint                |

---

### Key takeaway

> SQL doesn’t have a `DUPLICATES()` function because **duplicates are a data relationship**, not a scalar value — so SQL handles them via grouping and window functions.

If you want, tell me:

* Your database (MySQL / Postgres / SQL Server)
* Whether you want to **find**, **flag**, or **delete** duplicates

I’ll tailor the exact query for you 👍
