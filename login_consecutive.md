Great — this is a **classic FAANG-level SQL pattern** (consecutive days problem). Let’s break it step by step so you fully understand the logic ✅

***

# ✅ 🔍 Query

```sql
SELECT user_id
FROM (
    SELECT 
        user_id, 
        login_date, 
        login_date - ROW_NUMBER() OVER(
            PARTITION BY user_id 
            ORDER BY login_date
        ) AS grp
    FROM logins
) t
GROUP BY user_id, grp
HAVING COUNT(*) >= 3;
```

***

# ✅ 🎯 What This Query Does

👉 Finds users who have logged in for **at least 3 consecutive days**

***

# ✅ 🧠 Core Trick (IMPORTANT)

The key idea is:

> 👉 Convert consecutive dates into the same “group” using `ROW_NUMBER`

***

# ✅ 📊 Example Dataset

| user\_id | login\_date |
| -------- | ----------- |
| 1        | 2025-01-01  |
| 1        | 2025-01-02  |
| 1        | 2025-01-03  |
| 1        | 2025-01-05  |
| 2        | 2025-01-01  |
| 2        | 2025-01-03  |
| 2        | 2025-01-04  |

***

# ✅ 🔹 Step 1: Apply ROW\_NUMBER

```sql
ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date)
```

| user\_id | login\_date | row\_number |
| -------- | ----------- | ----------- |
| 1        | 2025-01-01  | 1           |
| 1        | 2025-01-02  | 2           |
| 1        | 2025-01-03  | 3           |
| 1        | 2025-01-05  | 4           |

***

# ✅ 🔹 Step 2: Create Group Key

```sql
login_date - row_number
```

| user\_id | login\_date | row\_number | grp (calculated) |
| -------- | ----------- | ----------- | ---------------- |
| 1        | 2025-01-01  | 1           | 2024-12-31       |
| 1        | 2025-01-02  | 2           | 2024-12-31       |
| 1        | 2025-01-03  | 3           | 2024-12-31       |
| 1        | 2025-01-05  | 4           | 2025-01-01       |

***

# ✅ 🔥 Why This Works

👉 For **consecutive dates**:

    date increases by 1
    row_number increases by 1

👉 So difference stays constant:

    (date - row_number) = SAME VALUE → same group

***

# ✅ 📦 Groups Formed

| grp        | dates                    |
| ---------- | ------------------------ |
| 2024-12-31 | 01, 02, 03 ✅ consecutive |
| 2025-01-01 | 05 ❌ break               |

***

# ✅ 🔹 Step 3: GROUP BY

```sql
GROUP BY user_id, grp
```

👉 Groups consecutive sequences

***

# ✅ 🔹 Step 4: Filter

```sql
HAVING COUNT(*) >= 3
```

👉 Only keep sequences of **length ≥ 3**

***

# ✅ ✅ Final Output

| user\_id |
| -------- |
| 1        |

👉 User 1 has 3 consecutive logins  
👉 User 2 does NOT

***

# ✅ 🧩 Visual Intuition

    User 1 timeline:
    1 → 2 → 3 ✅ (consecutive)
          gap
    5 ❌

    User 2 timeline:
    1
       gap
    3 → 4 ❌ (only 2 days)

***

# ✅ 🧠 Mental Model (Golden Rule)

    grp = date - row_number

👉 Converts:

*   consecutive rows → same group
*   broken sequence → new group

***

# ✅ 🔥 Why This Is Powerful

This pattern works for:

*   ✅ Consecutive login days
*   ✅ Consecutive order IDs
*   ✅ Streak analysis
*   ✅ Session detection

***

# ✅ 🚀 Interview Tip

Say this:

> “We normalize consecutive sequences using `date - ROW_NUMBER()` so that continuous sequences collapse into the same group.”

🔥 This is a **high-level FAANG explanation**

***

# ✅ 🔥 Final Summary

*   `ROW_NUMBER()` → assigns sequence
*   `date - row_number` → groups consecutive rows
*   `GROUP BY grp` → isolates streaks
*   `HAVING COUNT >= N` → filters streak length

***
