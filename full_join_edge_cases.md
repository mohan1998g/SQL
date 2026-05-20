Here are **advanced, tricky FULL OUTER JOIN edge cases** that are **frequently asked in interviews** and also occur in real projects.

***

# ✅ 1. NULL vs NULL (Still DOES NOT Match)

### Data

    A:             B:
    id  name       id  city
    NULL C         NULL LA

### Query

```sql
SELECT *
FROM A
FULL OUTER JOIN B
ON A.id = B.id;
```

### ✅ Output

    NULL | C | NULL | NULL
    NULL | NULL | NULL | LA

### ❗ Key Point

*   NULL ≠ NULL
*   You get **two separate rows**

***

# ✅ 2. Forcing NULL to Match (COALESCE Trick)

### Query

```sql
SELECT *
FROM A
FULL OUTER JOIN B
ON COALESCE(A.id, -1) = COALESCE(B.id, -1);
```

### ✅ Output

    NULL | C | NULL | LA

✅ Now NULL rows merge

***

# ✅ 3. Duplicate Records Explosion

### Data

    A:               B:
    id name          id city
    1  A             1  NY
    1  A2            1  LA

### Query

```sql
SELECT *
FROM A
FULL OUTER JOIN B
ON A.id = B.id;
```

### ✅ Output

    1 A   1 NY
    1 A   1 LA
    1 A2  1 NY
    1 A2  1 LA

### ❗ Problem

*   **Cartesian multiplication**
*   2 × 2 = 4 rows

***

### ✅ Fix

Use aggregation or deduplication:

```sql
SELECT DISTINCT id, name FROM A
```

***

# ✅ 4. FULL JOIN + WHERE Clause (Common Mistake)

### Query

```sql
SELECT *
FROM A
FULL OUTER JOIN B
ON A.id = B.id
WHERE A.id IS NOT NULL;
```

### ❗ Result

👉 Behaves like LEFT JOIN (loses B-only rows)

***

### ✅ Correct Way

```sql
WHERE A.id IS NOT NULL OR B.id IS NOT NULL;
```

***

# ✅ 5. Finding Unmatched Records (Very Common)

### ✅ Rows only in A

```sql
SELECT *
FROM A
FULL OUTER JOIN B
ON A.id = B.id
WHERE B.id IS NULL;
```

***

### ✅ Rows only in B

```sql
SELECT *
FROM A
FULL OUTER JOIN B
ON A.id = B.id
WHERE A.id IS NULL;
```

***

### ✅ Rows in either but not both

```sql
WHERE A.id IS NULL OR B.id IS NULL;
```

***

# ✅ 6. Join Condition on Multiple Columns

### Data Issue

    A(id, type)
    B(id, type)

If:

```sql
ON A.id = B.id AND A.type = B.type
```

👉 Even if id matches:

*   If type differs → no match

***

### ❗ Result

*   Unexpected NULL rows

***

# ✅ 7. Type Mismatch in FULL JOIN

```sql
ON A.id = B.id
```

If:

*   A.id = INT
*   B.id = STRING

👉 No match happens → everything becomes unmatched

***

### ✅ Fix

```sql
ON CAST(A.id AS STRING) = B.id
```

***

# ✅ 8. FULL JOIN with Filters on One Side

### Query

```sql
SELECT *
FROM A
FULL OUTER JOIN B
ON A.id = B.id
AND B.city = 'NY';
```

### ❗ Result

*   Only rows matching NY join
*   Others appear as NULL

👉 Looks like incorrect join

***

# ✅ 9. FULL JOIN with Aggregation Issues

```sql
SELECT COUNT(*)
FROM A
FULL JOIN B
ON A.id = B.id;
```

### ❗ Problem

*   Count includes:
    *   matched rows
    *   unmatched A rows
    *   unmatched B rows

👉 Can mislead totals

***

# ✅ 10. FULL JOIN on Large Tables (Performance Issue)

*   BigQuery:
    *   heavy shuffle
    *   expensive query

***

### ✅ Optimization

*   Filter before join:

```sql
SELECT *
FROM (SELECT * FROM A WHERE id IS NOT NULL) A
FULL JOIN B
ON A.id = B.id;
```

***

# ✅ 11. FULL JOIN + ORDER BY NULL Behavior

```sql
ORDER BY id
```

👉 NULLs:

*   appear first or last (depends on DB)

***

### ✅ Control explicitly

```sql
ORDER BY id NULLS LAST;
```

***

# ✅ 12. FULL JOIN + IS NULL Confusion

```sql
WHERE A.id IS NULL AND B.id IS NULL;
```

👉 Result = empty set (almost always)

👉 Because:

*   NULL ≠ NULL → they don’t match in same row

***

# ✅ 13. FULL JOIN Chained (Multi-table Issue)

```sql
A FULL JOIN B
FULL JOIN C
```

👉 If:

*   B has NULL keys → C join fails
*   Chain breaks unexpectedly

***

### ✅ Fix

*   Use COALESCE or staged joins

***

# ✅ 14. FULL JOIN vs UNION (Tricky Confusion)

### Alternative approach:

```sql
SELECT * FROM A
UNION
SELECT * FROM B;
```

👉 Difference:

*   UNION removes duplicates
*   FULL JOIN preserves relationship between tables

***

# ✅ Final Summary (Interview Ready)

> “FULL OUTER JOIN returns all records from both tables, including unmatched rows. However, NULL values do not match by default, duplicates can cause row explosion, and applying filters incorrectly can change the join behavior. Proper handling using COALESCE, filtering, and deduplication is critical.”

***

# ✅ Quick Cheat Sheet

| Issue               | Fix                     |
| ------------------- | ----------------------- |
| NULL not matching   | COALESCE                |
| Duplicate explosion | Deduplicate             |
| Missing rows        | Check JOIN type         |
| Wrong results       | Validate join condition |
| Performance issue   | Filter before join      |

***

