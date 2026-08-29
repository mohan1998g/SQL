# Real Debugging Case (7 Table Join Issue)

## Problem
- Joins working until 5 tables
- Fails at 6th/7th

## Root Causes
- INNER JOIN removing unmatched rows
- NULL values in keys
- Duplicate keys

## Debug Steps
1. Check row count after each join
```sql
SELECT COUNT(*) FROM temp_result;
```

2. Switch to LEFT JOIN

3. Validate NULLs
```sql
SELECT COUNT(*) FROM table WHERE id IS NULL;
```

4. Check duplicates
```sql
SELECT id, COUNT(*) FROM table GROUP BY id HAVING COUNT(*)>1;
```

## Fix Strategy
- Use LEFT JOIN
- Clean data
- Deduplicate
