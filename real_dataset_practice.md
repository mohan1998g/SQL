# Real Dataset Practice with Solutions

## Dataset: Sales Data
Columns: order_id, customer_id, product, amount, date

## Question 1: Total Revenue
```sql
SELECT SUM(amount) FROM sales;
```

## Question 2: Top Customer
```sql
SELECT customer_id, SUM(amount) total
FROM sales
GROUP BY customer_id
ORDER BY total DESC LIMIT 1;
```

## Question 3: Daily Sales Trend
```sql
SELECT date, SUM(amount)
FROM sales
GROUP BY date;
```

## Question 4: Handle NULLs
```sql
SELECT * FROM sales
WHERE customer_id IS NOT NULL;
```

## Question 5: Duplicate Records
```sql
SELECT order_id, COUNT(*)
FROM sales
GROUP BY order_id
HAVING COUNT(*) > 1;
```

## Question 6: Running Total
```sql
SELECT date,
SUM(amount) OVER (ORDER BY date) AS running_total
FROM sales;
```
