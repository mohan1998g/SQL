Absolutely! Here are **50 interview-style regex practice questions** organized by topic.  
Assume **PCRE/JavaScript-style** syntax unless noted (i.e., `\d`, `\w`, `\s`, `^`, `$`, `()`, `[]`, `+`, `*`, `?`, `{m,n}`, `|`, `(?=...)`, `(?<=...)`, etc.).  
At the end, you’ll find a complete **answer key** with sample patterns.

***

## 🧪 A. Basics & Character Classes (1–10)

1.  Match the word **“cat”** only if it appears as a whole word (not part of “concatenate”).
2.  Match any **3-digit** number.
3.  Match a **hex color code**: `#RGB` or `#RRGGBB` (case-insensitive).
4.  Match strings containing **only lowercase letters** (a–z).
5.  Match a **valid variable name**: starts with letter or underscore, followed by letters, digits, or underscores.
6.  Match a **US ZIP code**: `12345` or `12345-6789`.
7.  Match a **date** in `YYYY-MM-DD` (basic structural validation only).
8.  Match a **floating-point number** (allow optional sign, decimals, or scientific notation like `-1.23e+10`).
9.  Match a **credit card-like** 16-digit number with optional spaces or hyphens (format-only check).
10. Match an **IPv4 address** structurally (four octets separated by dots, 0–255 loosely).

***

## 🧲 B. Anchors, Quantifiers & Alternation (11–20)

11. Match a string that **starts with “Hello”** and ends with an exclamation mark.
12. Match **one or more** consecutive whitespace characters.
13. Match **either “color” or “colour”** (UK/US spelling).
14. Match **repeated words** like `hello hello` (exact duplicate next to each other).
15. Match strings that **do not contain digits** (entire string).
16. Match **files with extensions** `.png`, `.jpg`, `.jpeg`, `.gif` (case-insensitive).
17. Match **3 to 6** lowercase letters only.
18. Match **a word of length 8–20** that must contain at least one **digit** and one **uppercase** letter (use lookarounds).
19. Match **MAC addresses** like `AA:BB:CC:DD:EE:FF` or `aa-bb-cc-dd-ee-ff`.
20. Match **HTML tags**: capture the tag name from `<div>...</div>` (simple non-nested).

***

## 🧩 C. Groups, Backreferences & Capture (21–30)

21. Match and **capture the domain** from an email `user@domain.com`.
22. Match **pairs of quotes** with the **same delimiter** (`"..."` or `'...'`) using backreferences.
23. Match a **palindrome of length 4** (e.g., `abba`, `1221`).
24. Match **duplicated words** anywhere in a text (e.g., “this is is fine”).
25. Match a number with **thousands separators** like `1,234`, `12,345,678` (no leading zeros unless number is 0).
26. Extract the **username** from a GitHub URL like `https://github.com/mohan`.
27. Extract the **file extension** from `report.final.v2.pdf`.
28. Match **balanced parentheses** with **one level** only (e.g., `(abc)` but not `(a(b)c)`).
29. Match a **US phone number** in formats: `(123) 456-7890`, `123-456-7890`, `123.456.7890`, `1234567890`.
30. Match **“word” boundaries** around `cat` without using `\b` (use lookarounds).

***

## 🔎 D. Lookarounds (31–40)

31. Match digits that are **followed by** the word `kg` (don’t include `kg` in the match).
32. Match words that are **not followed by** a comma (negative lookahead).
33. Match `apple` only if it is **preceded by** `green` (whitespace optional).
34. Match `foo` only if **not preceded by** `bar`.
35. Replace every comma **that is not inside quotes** in a CSV-like line (write regex to match such commas).
36. Match words that contain **at least two vowels** using lookaheads.
37. Match `https` URLs, but **exclude** `http` (assert the `s`).
38. Match a price like `$12.99` only if the line also contains the word `TOTAL` (two-step or lookahead across line).
39. Match **the last occurrence** of a word in a line (using a tempered dot or lookarounds).
40. Match a number only if it is **between parentheses** like `(123)`.

***

## 🌐 E. Validation Patterns (41–50)

41. Validate a **strong password**: min 8 chars, at least one uppercase, one lowercase, one digit, and one special (`!@#$%^&*`).
42. Validate an **email** (practical interview-level, not RFC-perfect).
43. Validate an **Indian mobile number**: 10 digits, first digit 6–9; allow optional `+91` with spaces/hyphens.
44. Validate **ISO-8601 time** `HH:MM:SS` (00–23 for hour).
45. Validate **UUID v4** like `xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx` (case-insensitive).
46. Validate **E.164 international phone number** (up to 15 digits, leading `+`).
47. Validate **URL** (http/https), optional `www`, domain, optional path/query (reasonable, not perfect).
48. Validate **PAN (India)**: 5 letters, 4 digits, 1 letter (e.g., `ABCDE1234F`).
49. Validate **GSTIN (India)**: 15-character alphanumeric with structure (simplified).
50. Validate **YYYY-MM-DD** ensuring **valid months (01–12)** and **days (01–31)** (no leap-day logic).

***

## ✅ Answer Key (Sample Regex Solutions)

> ⚠️ Note: There are many valid regex solutions. These aim for **clarity** and **interview suitability** rather than RFC completeness. Adjust for your flavor (PCRE/JS) and flags (`i`, `m`, `s`, `g`) as needed.

1.  Whole word “cat”:
    ```regex
    \bcat\b
    ```

2.  Three digits:
    ```regex
    \b\d{3}\b
    ```

3.  Hex color (#RGB or #RRGGBB):
    ```regex
    ^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$
    ```

4.  Only lowercase:
    ```regex
    ^[a-z]+$
    ```

5.  Valid variable name:
    ```regex
    ^[A-Za-z_]\w*$
    ```

6.  US ZIP:
    ```regex
    ^\d{5}(?:-\d{4})?$
    ```

7.  Date YYYY-MM-DD:
    ```regex
    ^\d{4}-(\d{2})-(\d{2})$
    ```

8.  Float / scientific:
    ```regex
    ^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?$
    ```

9.  CC-like 16 digits with separators:
    ```regex
    ^(?:\d{4}[-\s]?){3}\d{4}$
    ```

10. IPv4 (structural):
    ```regex
    ^(?:\d{1,3}\.){3}\d{1,3}$
    ```
    > (For strict 0–255: use range checks or programmatic validation.)

11. Starts with “Hello”, ends with `!`:
    ```regex
    ^Hello.*!$
    ```

12. One or more whitespace:
    ```regex
    \s+
    ```

13. color/colour:
    ```regex
    colou?r
    ```

14. Repeated adjacent word:
    ```regex
    \b(\w+)\s+\1\b
    ```

15. String without digits:
    ```regex
    ^[^0-9]*$
    ```

16. Image extensions:
    ```regex
    (?i)^.+\.(?:png|jpg|jpeg|gif)$
    ```

17. 3 to 6 lowercase letters:
    ```regex
    ^[a-z]{3,6}$
    ```

18. 8–20 chars, at least one digit and uppercase:
    ```regex
    ^(?=.*\d)(?=.*[A-Z])[A-Za-z0-9]{8,20}$
    ```
    > Adjust allowed set to include symbols if needed.

19. MAC addresses (`:` or `-`):
    ```regex
    ^(?:[0-9A-Fa-f]{2}([-:]))(?:[0-9A-Fa-f]{2}\1){4}[0-9A-Fa-f]{2}$
    ```

20. Simple HTML tag capturing name:
    ```regex
    ^<([A-Za-z][A-Za-z0-9]*)\b[^>]*>.*?</\1>$
    ```
    > Not safe for arbitrary HTML; good for interview demonstration.

21. Capture domain from email:
    ```regex
    ^[^@\s]+@([^@\s]+\.[^@\s]+)$
    ```

22. Same-quote pairing:
    ```regex
    (["'])(.*?)\1
    ```

23. 4-char palindrome:
    ```regex
    ^(.)(.)\2\1$
    ```

24. Duplicated words anywhere:
    ```regex
    \b(\w+)\b(?:.*\b\1\b)+
    ```
    > Or adjacent duplicate: see #14.

25. Thousands separators:
    ```regex
    ^(?:0|[1-9]\d{0,2})(?:,\d{3})*$
    ```

26. GitHub username from URL:
    ```regex
    ^https?://github\.com/([A-Za-z0-9-]+)(?:/|$)
    ```

27. File extension from `report.final.v2.pdf`:
    ```regex
    ^.*\.([A-Za-z0-9]+)$
    ```

28. One-level parentheses only:
    ```regex
    ^\([^()]*\)$
    ```

29. US phone formats:
    ```regex
    ^(?:\(\d{3}\)\s?|\d{3}[-.]?)\d{3}[-.]?\d{4}$|^\d{10}$
    ```

30. Word boundaries around `cat` via lookarounds:
    ```regex
    (?<!\w)cat(?!\w)
    ```

31. Digits followed by `kg` (don’t include `kg`):
    ```regex
    \b\d+(?=\s?kg\b)
    ```

32. Words not followed by comma:
    ```regex
    \b\w+\b(?!\s*,)
    ```

33. `apple` preceded by `green` (optional space):
    ```regex
    (?<=\bgreen\s?)apple
    ```

34. `foo` not preceded by `bar`:
    ```regex
    (?<!bar)foo
    ```

35. Commas not inside quotes (CSV-like line):
    ```regex
    ,(?=(?:[^"]*"[^"]*")*[^"]*$)
    ```

36. Words with at least two vowels (a,e,i,o,u):
    ```regex
    \b(?=(?:[^aeiou]*[aeiou]){2,}[^aeiou]*\b)\w+\b
    ```

37. Only `https` URLs:
    ```regex
    ^https://[^\s]+$
    ```

38. Price `$12.99` only if line contains `TOTAL`:
    ```regex
    (?=.*\bTOTAL\b).*\$\d+(?:\.\d{2})?
    ```

39. Last occurrence of a word in a line:
    ```regex
    \b(\w+)\b(?!.*\b\1\b)
    ```

40. Numbers inside parentheses:
    ```regex
    (?<=\()\d+(?=\))
    ```

41. Strong password (min 8, upper, lower, digit, special):
    ```regex
    ^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$
    ```

42. Practical email (not RFC-perfect):
    ```regex
    ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$
    ```

43. Indian mobile (10 digits, 6–9; optional +91, spaces/hyphens):
    ```regex
    ^(?:\+91[\s-]?)?[6-9]\d{9}$
    ```

44. Time HH:MM:SS (24h):
    ```regex
    ^(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d$
    ```

45. UUID v4:
    ```regex
    ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-4[0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$
    ```

46. E.164 international phone:
    ```regex
    ^\+[1-9]\d{1,14}$
    ```

47. URL (reasonable):
    ```regex
    ^https?:\/\/(?:www\.)?[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:\/[^\s?#]*)?(?:\?[^\s#]*)?(?:#[^\s]*)?$
    ```

48. PAN (India):
    ```regex
    ^[A-Z]{5}\d{4}[A-Z]$
    ```

49. GSTIN (simplified):
    ```regex
    ^\d{2}[A-Z]{5}\d{4}[A-Z][A-Z1-9][Z][A-Z\d]$
    ```

50. Valid month/day ranges in `YYYY-MM-DD` (basic month/day validation):
    ```regex
    ^\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$
    ```

***

## Tips for Interviews

*   **State your assumptions** (regex flavor, flags, input normalization) before writing.
*   Prefer **readable** and **maintainable** patterns—use **non-capturing groups** `(?:...)` when you don’t need captures.
*   For complex validation (emails, IP ranges, HTML), note that regex has limits—offer **post-processing** or **library** validation.

***

If you want, I can turn these into a **quiz file** (Markdown/Word/PDF) or give you **solutions with test cases** you can run quickly. Would you like them in **JavaScript**, **Python**, or **.NET** flavor with sample code to test each pattern?
