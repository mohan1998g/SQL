# 10 Tricky SQL Join Interview Scenarios

## 1. INNER JOIN Losing Data
- Missing matches cause row drops

## 2. LEFT JOIN Acting Like INNER JOIN
```sql
SELECT * FROM A
LEFT JOIN B ON A.id=B.id
WHERE B.id IS NOT NULL;
```

## 3. Duplicate Explosion
- Non-unique keys create multiple rows

## 4. Missing Join Condition (Cartesian Join)
```sql
SELECT * FROM A, B;
```

## 5. Mismatched Data Types
- INT vs STRING fails join

## 6. NULL Join Keys
- NULL never matches

## 7. Multiple Joins Data Drop
- INNER JOIN removes rows in chain

## 8. Join on Wrong Column
- Logical issue

## 9. Self Join Confusion
- Incorrect alias usage

## 10. Many-to-Many Join Explosion
- Requires deduplication
