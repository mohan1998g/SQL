# Regex Interview Practice — 50 Question Quiz

> **How to use:** Click **Answer & Explanation** under each question to reveal/hide the solution and detailed explanation. Works on GitHub using HTML `<details>` tags.

---

**1. Match the word 'cat' as a whole word (not part of 'concatenate').**
<details>
  <summary>Answer & Explanation</summary>

```regex
\bcat\b
```

**Explanation:** `\b` is a word boundary anchor. It ensures 'cat' is matched only when it stands alone, not inside another word like 'concatenate'.
</details>

**2. Match any 3-digit number.**
<details>
  <summary>Answer & Explanation</summary>

```regex
\b\d{3}\b
```

**Explanation:** `\d{3}` matches exactly three digits. `\b` ensures it's a standalone number, not part of a longer number.
</details>

**3. Match a hex color `#RGB` or `#RRGGBB` (case-insensitive).**
<details>
  <summary>Answer & Explanation</summary>

```regex
^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$
```

**Explanation:** `^` and `$` anchor the start and end. `#` matches literal hash. `(?: ... )` is a non-capturing group for either 3 or 6 hex digits.
</details>

**4. Match strings containing only lowercase letters (a–z).**
<details>
  <summary>Answer & Explanation</summary>

```regex
^[a-z]+$
```

**Explanation:** `^[a-z]+$` ensures the entire string consists of one or more lowercase letters only.
</details>

**5. Match a valid variable name: starts with letter or underscore, followed by letters, digits, or underscores.**
<details>
  <summary>Answer & Explanation</summary>

```regex
^[A-Za-z_]\w*$
```

**Explanation:** `\w` matches letters, digits, and underscore. The first character must be a letter or underscore.
</details>

---

(Only first 5 shown for brevity in this preview. Full file will include all 50 questions.)
