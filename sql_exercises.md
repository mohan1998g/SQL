# Hands-on SQL Exercises (Joins + NULLs)

## Exercise 1
Find unmatched records
```sql
SELECT * FROM A
LEFT JOIN B ON A.id=B.id
WHERE B.id IS NULL;
```

## Exercise 2
Find duplicates
```sql
SELECT id, COUNT(*) FROM table GROUP BY id HAVING COUNT(*)>1;
```

## Exercise 3
Handle NULL join
```sql
SELECT * FROM A JOIN B
ON COALESCE(A.id,-1)=COALESCE(B.id,-1);
```

## Exercise 4
Running totals
```sql
SELECT id, SUM(val) OVER (ORDER BY id) FROM table;
```

## Exercise 5
Latest record
```sql
SELECT * FROM (
 SELECT *, ROW_NUMBER() OVER (PARTITION BY id ORDER BY date DESC) rn
 FROM table)
WHERE rn=1;
```
