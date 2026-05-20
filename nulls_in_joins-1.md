Understanding **NULL behavior in JOINs** is a **very important SQL/BigQuery interview topic** — many real-world bugs come from this.

***

# ✅ Core Concept (Must Remember)

👉 **NULL never equals anything — not even another NULL**

So:

```sql
NULL = NULL   → FALSE
```

***

# ✅ What Happens in Join Conditions with NULLs?

When you write:

```sql
ON A.id = B.id
```

👉 If either side is NULL:

*   Condition fails
*   Row is **not matched**

***

# ✅ Scenario-Based Explanation (Very Important)

***

# 🔹 Scenario 1: INNER JOIN with NULLs

### ✅ Tables

**Table A**

    id | name
    1  | A
    2  | B
    NULL | C

**Table B**

    id | city
    1  | NY
    NULL | LA

***

### ✅ Query

```sql
SELECT *
FROM A
INNER JOIN B
ON A.id = B.id;
```

***

### ✅ Result

    id | name | city
    1  | A    | NY

***

### ❗ What happened?

*   NULL rows **did not join**
*   Even `NULL = NULL` is NOT true

***

✅ Key Insight:

> INNER JOIN drops rows with NULL join keys

***

# 🔹 Scenario 2: LEFT JOIN with NULLs

***

### ✅ Query

```sql
SELECT *
FROM A
LEFT JOIN B
ON A.id = B.id;
```

***

### ✅ Result

    id | name | city
    1  | A    | NY
    2  | B    | NULL
    NULL | C  | NULL

***

### ❗ What happened?

*   All rows from A are kept
*   No match → NULL values on right side

***

✅ Key Insight:

> LEFT JOIN keeps NULL rows from left table

***

# 🔹 Scenario 3: NULL in Right Table Only

***

### ✅ Tables

**Table A**

    id
    1
    2

**Table B**

    id
    1
    NULL

***

### ✅ Query

```sql
SELECT *
FROM A
LEFT JOIN B
ON A.id = B.id;
```

***

### ✅ Result

    1 | 1
    2 | NULL

***

### ❗ What happened?

*   Row with NULL in table B didn’t match anything

***

# 🔹 Scenario 4: Both Tables Have NULL

***

### ✅ Query

```sql
SELECT *
FROM A
JOIN B
ON A.id = B.id;
```

Where both have NULLs.

***

### ❗ Result

✅ NULL rows **still won’t match**

***

✅ Key Insight:

> NULL ≠ NULL in SQL joins

***

# 🔹 Scenario 5: Using COALESCE to Handle NULLs

👉 Sometimes business logic wants NULLs to match

***

### ✅ Query

```sql
SELECT *
FROM A
JOIN B
ON COALESCE(A.id, -1) = COALESCE(B.id, -1);
```

***

### ✅ Result

*   NULL treated as -1
*   Now NULL values can match

***

✅ Key Insight:

> Use COALESCE to force matching

***

# 🔹 Scenario 6: Data Missing Due to NULL

👉 Real-world issue you faced 👇

***

### Query

```sql
SELECT *
FROM T1
JOIN T2 ON T1.id = T2.id
JOIN T3 ON T2.id = T3.id
```

***

### ❗ Problem

If `T2.id` is NULL:

*   T3 join fails
*   Data disappears

***

✅ Fix:

```sql
LEFT JOIN T3 ON T2.id = T3.id
```

***

# 🔹 Scenario 7: Unexpected NULLs in Result

***

### Query

```sql
SELECT *
FROM A
LEFT JOIN B
ON A.id = B.id;
```

***

### ❗ Output shows NULLs in B columns

👉 Why?

*   No match found

***

✅ This is expected behavior

***

# 🔹 Scenario 8: Filtering NULL in WHERE Clause

***

### Query

```sql
SELECT *
FROM A
LEFT JOIN B
ON A.id = B.id
WHERE B.id IS NOT NULL;
```

***

### ❗ What happens?

👉 LEFT JOIN behaves like INNER JOIN

***

✅ Key Insight:

> WHERE condition can remove NULL rows

***

# 🔹 Scenario 9: Multiple Joins + NULLs (Your Case)

If:

*   First 5 joins OK
*   6th join uses NULL column

👉 Result:

*   Rows drop suddenly

***

### ✅ Debug Tip

```sql
SELECT COUNT(*) before_join
SELECT COUNT(*) after_join
```

***

# ✅ Summary Table

| Scenario                      | Result               |
| ----------------------------- | -------------------- |
| INNER JOIN + NULL             | Row dropped          |
| LEFT JOIN + NULL (left side)  | Row kept             |
| LEFT JOIN + NULL (right side) | NULL output          |
| NULL = NULL                   | FALSE                |
| COALESCE used                 | Can match            |
| WHERE filter                  | May remove NULL rows |

***

# ✅ Interview Answer (Perfect)

👉 You can say:

> “In SQL, NULL values do not match with any value, including another NULL, so rows with NULL join keys are excluded in INNER JOINs. In LEFT JOINs, rows from the left table are preserved, but unmatched rows result in NULL values on the right side. To handle NULLs, we can use functions like COALESCE or adjust join types depending on the requirement.”

***

# ✅ Pro Tips (Advanced)

✅ Always check:

*   NULL count in join columns

```sql
SELECT COUNT(*) WHERE id IS NULL;
```

✅ Use LEFT JOIN to debug missing data  
✅ Use COALESCE only if business logic allows

***
