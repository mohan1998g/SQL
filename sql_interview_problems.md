# 20 Real SQL Interview Problems (Amazon/Google Style)

## 1. Second Highest Salary
Write a query to find the second highest salary.

## 2. Nth Highest Salary
Generalize the above for nth salary.

## 3. Find Duplicates
```sql
SELECT id, COUNT(*)
FROM table
GROUP BY id HAVING COUNT(*) > 1;
```

## 4. Remove Duplicates
Use ROW_NUMBER window function.

## 5. Running Total
Use:
```sql
SUM(col) OVER (ORDER BY date)
```

## 6. Top N per Group
Use RANK or DENSE_RANK.

## 7. Find Missing IDs

## 8. Self Join (Manager-Employee)

## 9. Find Consecutive Records

## 10. Pivot Data

## 11. Unpivot Data

## 12. Latest Record per User

## 13. Rank vs Dense Rank Difference

## 14. Window vs Aggregate

## 15. Conditional Aggregation

## 16. Join with NULL Handling

## 17. Data Skew Problem

## 18. Query Optimization

## 19. Subquery vs Join

## 20. CTE vs Subquery
