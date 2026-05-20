Great question — this is a **classic SQL interview scenario** 👏

***

# ✅ Your Requirement

You want:

👉 **All rows from A AND all rows from B**  
👉 Including **NULL rows from both tables**

***

# ✅ Solution: Use `FULL OUTER JOIN`

***

## ✅ Query

```sql
SELECT *
FROM A
FULL OUTER JOIN B
ON A.id = B.id;
```

***

# ✅ Output (for your data)

### Table A

    id | name
    1  | A
    2  | B
    NULL | C

### Table B

    id | city
    1  | NY
    NULL | LA

***

### ✅ Result

    A.id | name | B.id | city
    --------------------------------
    1    | A    | 1    | NY
    2    | B    | NULL | NULL
    NULL | C    | NULL | NULL
    NULL | NULL | NULL | LA

***

# ✅ Explanation

| Case     | What happened                     |
| -------- | --------------------------------- |
| id = 1   | Matched → combined row            |
| id = 2   | Exists only in A → B columns NULL |
| NULL (A) | No match → kept                   |
| NULL (B) | No match → kept                   |

***

# ✅ Why This Works

👉 `FULL OUTER JOIN`:

*   Includes **all rows from both tables**
*   If no match:
    *   fills missing side with NULL

***

# ✅ Important Note about NULLs

Even in FULL JOIN:

*   `NULL = NULL` is **not considered a match**
*   So:
    *   A.NULL and B.NULL → **do NOT join together**
    *   They appear as **separate rows**

***

# ✅ If You WANT NULLs to Match

👉 Use `COALESCE`

***

## ✅ Query (Force NULL match)

```sql
SELECT *
FROM A
FULL OUTER JOIN B
ON COALESCE(A.id, -1) = COALESCE(B.id, -1);
```

***

### ✅ Output

    A.id | name | B.id | city
    --------------------------------
    1    | A    | 1    | NY
    2    | B    | NULL | NULL
    NULL | C    | NULL | LA

***

✅ Now:

*   NULL from A and NULL from B **matched together**

***

# ✅ Summary (Interview Ready Answer)

> “To retrieve all rows from both tables, including unmatched and NULL rows, we use a FULL OUTER JOIN. Since NULL values do not match by default, they appear as separate rows. If we want NULL values to match, we can use functions like COALESCE in the join condition.”

***

# ✅ When to Use What

| Requirement               | Solution             |
| ------------------------- | -------------------- |
| All rows from A only      | LEFT JOIN            |
| All rows from both tables | FULL OUTER JOIN      |
| Match NULLs also          | FULL JOIN + COALESCE |

***

# ✅ Pro Tip (Important for Interviews)

If interviewer asks:
👉 “Why are NULL rows not joining?”

Answer:

> “Because SQL treats NULL as unknown, so NULL = NULL evaluates to false.”

***
