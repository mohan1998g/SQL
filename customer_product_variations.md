Good question 👍 — this is a **common confusion in SQL interviews**.

Let’s break down what’s actually happening.

***

# ✅ Your Concern

> If a customer buys the same product multiple times (e.g., quantity = 2), and misses another product → count may still match?

***

# 🔍 Why Your Current Query Still Works

Your query:

```sql
SELECT customer_id
FROM purchases
GROUP BY customer_id
HAVING COUNT(DISTINCT product_id) = (
    SELECT COUNT(*) FROM products
);
```

### ✅ Key Point:

*   `COUNT(DISTINCT product_id)` **ignores duplicates**

### Example

#### Products table:

| product\_id |
| ----------- |
| A           |
| B           |
| C           |

👉 Total products = **3**

***

#### Customer purchases:

| customer\_id | product\_id |
| ------------ | ----------- |
| 1            | A           |
| 1            | A           |
| 1            | B           |

👉 `COUNT(DISTINCT product_id)` = **2 (A, B)**  
👉 Missing product C → customer **WILL NOT be selected**

✅ So your query is **already correct**

***

# 🚨 When the Problem Actually Occurs

The issue happens only if **products table has duplicates**

Example:

| product\_id |
| ----------- |
| A           |
| B           |
| B           |
| C           |

👉 `COUNT(*) = 4` (wrong total)

Now:

*   Customer buys A, B, C → distinct = 3
*   Condition: `3 != 4` → incorrect result ❌

***

# ✅ Fix 1: Use DISTINCT in Products

```sql
SELECT customer_id
FROM purchases
GROUP BY customer_id
HAVING COUNT(DISTINCT product_id) = (
    SELECT COUNT(DISTINCT product_id) FROM products
);
```

✅ Always safer

***

# ✅ Best Practice Solution (Relational Division)

This is the **most robust and interview-preferred approach**:

```sql
SELECT c.customer_id
FROM purchases c
WHERE NOT EXISTS (
    SELECT p.product_id
    FROM products p
    WHERE NOT EXISTS (
        SELECT 1
        FROM purchases p2
        WHERE p2.customer_id = c.customer_id
        AND p2.product_id = p.product_id
    )
)
GROUP BY c.customer_id;
```

***

### 🔍 Why this is better:

*   Ensures **customer has every product**
*   Not dependent on counts
*   Handles:
    *   duplicates ✅
    *   missing products ✅
    *   dirty data ✅

***

# ✅ Summary

| Scenario                 | Works with your query?      |
| ------------------------ | --------------------------- |
| Duplicate purchases      | ✅ YES (DISTINCT handles it) |
| Missing product          | ✅ YES                       |
| Duplicate products table | ❌ Needs fix                 |
| Fully robust solution    | ✅ Use `NOT EXISTS`          |

***

# 🚀 Interview Tip

When asked this question, give:

1.  ✅ Basic solution (COUNT DISTINCT)
2.  ✅ Improved version (DISTINCT in products)
3.  ✅ Advanced solution (NOT EXISTS)

This shows **deep SQL understanding** 💯

***

Awesome ✅ — let’s take this to **interview mastery level**.

I’ll give you:

1.  ✅ **5 Amazon-style variations**
2.  ✅ **Progressive difficulty versions (easy → hard)**
3.  ✅ **Visual intuition / diagrams (very important for interviews)**

***

# ✅ 🔥 1. Amazon-Style Variations (VERY COMMON)

## ✅ Variation 1: Customers who bought ALL products in a category

```sql
SELECT customer_id
FROM purchases p
JOIN products pr ON p.product_id = pr.product_id
WHERE pr.category = 'Electronics'
GROUP BY customer_id
HAVING COUNT(DISTINCT p.product_id) = (
    SELECT COUNT(DISTINCT product_id)
    FROM products
    WHERE category = 'Electronics'
);
```

👉 Tests filtering + division logic

***

## ✅ Variation 2: Customers who bought ALL products BUT only in last 30 days

```sql
SELECT customer_id
FROM purchases
WHERE purchase_date >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY customer_id
HAVING COUNT(DISTINCT product_id) = (
    SELECT COUNT(DISTINCT product_id) FROM products
);
```

👉 Adds time constraint (very common in Amazon interviews)

***

## ✅ Variation 3: Customers who bought AT LEAST all products (allow extra)

👉 Same as base problem ✅  
👉 Trick: “at least” doesn’t change logic

***

## ✅ Variation 4: Customers who bought ALL EXCEPT 1 product

```sql
SELECT customer_id
FROM purchases
GROUP BY customer_id
HAVING COUNT(DISTINCT product_id) = (
    SELECT COUNT(DISTINCT product_id) - 1 FROM products
);
```

👉 Tests careful thinking

***

## ✅ Variation 5: Products NOT purchased by a customer (reverse logic)

```sql
SELECT p.product_id
FROM products p
WHERE NOT EXISTS (
    SELECT 1
    FROM purchases pu
    WHERE pu.customer_id = 101
    AND pu.product_id = p.product_id
);
```

👉 This is the **core logic behind the advanced solution**

***

# ✅ 🚀 2. Progressive Difficulty (What Interviewers Expect)

***

## 🟢 Level 1 (Easy)

👉 Basic aggregation

```sql
SELECT customer_id, COUNT(DISTINCT product_id)
FROM purchases
GROUP BY customer_id;
```

***

## 🟡 Level 2 (Intermediate)

👉 Compare with total count

```sql
HAVING COUNT(DISTINCT product_id) = (SELECT COUNT(*) FROM products);
```

***

## 🟠 Level 3 (Data Quality Safe)

👉 Fix duplicates in products

```sql
HAVING COUNT(DISTINCT product_id) = (
    SELECT COUNT(DISTINCT product_id) FROM products
);
```

***

## 🔴 Level 4 (Advanced – Preferred in FAANG)

👉 Relational Division (NOT EXISTS)

```sql
SELECT DISTINCT p1.customer_id
FROM purchases p1
WHERE NOT EXISTS (
    SELECT 1
    FROM products p
    WHERE NOT EXISTS (
        SELECT 1
        FROM purchases p2
        WHERE p2.customer_id = p1.customer_id
        AND p2.product_id = p.product_id
    )
);
```

***

## 🔴🔥 Level 5 (Hard Variant – Optimized Thinking)

👉 Using LEFT JOIN anti-pattern

```sql
SELECT c.customer_id
FROM (SELECT DISTINCT customer_id FROM purchases) c
LEFT JOIN products p
ON NOT EXISTS (
    SELECT 1
    FROM purchases pu
    WHERE pu.customer_id = c.customer_id
    AND pu.product_id = p.product_id
)
WHERE p.product_id IS NULL;
```

***

# ✅ 🧠 3. Visual Explanation (Most Important)

***

## 🧩 Think of it like a set problem

### Products (Universe):

    {A, B, C}

***

### Customer 1:

    {A, B, C} ✅ VALID

### Customer 2:

    {A, A, B} ❌ Missing C

### Customer 3:

    {A, B, C, C} ✅ VALID (duplicates ignored)

***

## 🔍 What SQL is doing:

### COUNT DISTINCT approach

    | Customer | Distinct Products | Match? |
    |----------|------------------|--------|
    | 1        | 3                | ✅     |
    | 2        | 2                | ❌     |
    | 3        | 3                | ✅     |

***

## 🔥 NOT EXISTS approach (deep logic)

👉 For each customer:

*   Loop all products
*   Check if ANY product is missing

<!---->

    IF no missing product → ✅ include
    IF even one missing → ❌ exclude

***

### Mental Model:

    FOR EACH customer:
        FOR EACH product:
            CHECK purchase exists

    IF ALL checks pass → valid customer

***

# ✅ 🧾 Interview Answer Template (Use This 💯)

When asked this question, say:

> “We can solve this using aggregation with COUNT DISTINCT, but that relies on clean data. A more robust solution is using relational division with NOT EXISTS to ensure no product is missing for the customer.”

Then write:

```sql
SELECT DISTINCT p1.customer_id
FROM purchases p1
WHERE NOT EXISTS (
    SELECT 1 FROM products p
    WHERE NOT EXISTS (
        SELECT 1 FROM purchases p2
        WHERE p2.customer_id = p1.customer_id
        AND p2.product_id = p.product_id
    )
);
```

***

# ✅ 🔥 Final Takeaways

*   ✅ `COUNT(DISTINCT)` handles duplicate purchases
*   ✅ Always validate product table (use DISTINCT)
*   ✅ **NOT EXISTS = gold standard (FAANG expected)**
*   ✅ Think in **sets, not rows**

***
