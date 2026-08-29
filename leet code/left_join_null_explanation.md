# LEFT JOIN with WHERE Clause and NULL Handling

## Query

```sql
SELECT name, bonus
FROM Employee e
LEFT JOIN Bonus b
    ON e.empid = b.empid
WHERE bonus < 1000;
```

## Will this return employees not present in the Bonus table?

**No.**

Although `LEFT JOIN` initially keeps all employees, the `WHERE` clause is applied after the join.

### Intermediate Result

```text
Name    Bonus
----    -----
A       500
B       1200
C       NULL
```

Here, employee `C` has no matching row in the `Bonus` table, so the bonus value is `NULL`.

### WHERE Evaluation

```sql
bonus < 1000
```

Results:

```text
500 < 1000   -> TRUE
1200 < 1000  -> FALSE
NULL < 1000  -> NULL (UNKNOWN)
```

The `WHERE` clause only keeps rows where the condition evaluates to `TRUE`.

Therefore:

- Employee A is returned.
- Employee B is filtered out.
- Employee C is also filtered out because `NULL < 1000` is not TRUE.

## Correct Query to Include Employees with No Bonus

```sql
SELECT name, bonus
FROM Employee e
LEFT JOIN Bonus b
    ON e.empid = b.empid
WHERE bonus < 1000
   OR bonus IS NULL;
```

### Output

```text
Name    Bonus
----    -----
A       500
C       NULL
```

## Important Interview Concept

A common misconception is:

> "LEFT JOIN always keeps all rows from the left table."

This is only true **before** the `WHERE` clause is applied.

If you place a condition on a column from the right table inside the `WHERE` clause, rows containing `NULL` values can be removed unless they are explicitly handled using:

```sql
OR bonus IS NULL
```

## LeetCode 577 Solution

```sql
SELECT name, bonus
FROM Employee e
LEFT JOIN Bonus b
    ON e.empid = b.empid
WHERE bonus < 1000
   OR bonus IS NULL;
```
