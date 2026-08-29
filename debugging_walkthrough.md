# Live Debugging Walkthrough (7 Table Join Issue)

## Scenario
Joining 7 tables; fails at 6th and 7th join.

## Step 1: Baseline Check
```sql
SELECT COUNT(*) FROM table1;
```

## Step 2: Incremental Join
Add tables one by one and check count.

## Step 3: Identify Drop
Check where count drops drastically.

## Step 4: Switch INNER to LEFT
```sql
LEFT JOIN table6 ON ...
```

## Step 5: Check NULLs
```sql
SELECT COUNT(*) FROM table6 WHERE key IS NULL;
```

## Step 6: Check Duplicates
```sql
SELECT key, COUNT(*) FROM table7 GROUP BY key HAVING COUNT(*)>1;
```

## Step 7: Validate Data Types
Ensure matching types.

## Step 8: Final Fix
- Use LEFT JOIN
- Deduplicate
- Clean NULLs

## Key Learning
- Join failures usually due to NULLs, duplicates, or wrong join type
