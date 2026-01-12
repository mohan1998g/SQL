
# Regex Interview Practice — 50 Question Quiz

> **How to use:** Click **Answer** under each question to reveal/hide the solution. Works on GitHub using HTML `<details>` tags.
>
> **Flavor assumed:** PCRE/JavaScript-style (`\d`, `\w`, `^`, `$`, groups, lookarounds). Adjust for your engine as needed.

---

## A. Basics & Character Classes (1–10)

**1. Match the word “cat” as a whole word (not part of “concatenate”).**
<details>
  <summary>Answer</summary>

```regex
\bcat\b
```
</details>

**2. Match any 3-digit number.**
<details>
  <summary>Answer</summary>

```regex
\b\d{3}\b
```
</details>

**3. Match a hex color `#RGB` or `#RRGGBB` (case-insensitive).**
<details>
  <summary>Answer</summary>

```regex
^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$
```
</details>

**4. Match strings containing only lowercase letters (a–z).**
<details>
  <summary>Answer</summary>

```regex
^[a-z]+$
```
</details>

**5. Match a valid variable name: starts with letter or underscore, followed by letters, digits, or underscores.**
<details>
  <summary>Answer</summary>

```regex
^[A-Za-z_]\w*$
```
</details>

**6. Match a US ZIP code: `12345` or `12345-6789`.**
<details>
  <summary>Answer</summary>

```regex
^\d{5}(?:-\d{4})?$ 
```
</details>

**7. Match a date in `YYYY-MM-DD` (structural only).**
<details>
  <summary>Answer</summary>

```regex
^\d{4}-(\d{2})-(\d{2})$
```
</details>

**8. Match a floating-point number (optional sign/decimals/scientific notation).**
<details>
  <summary>Answer</summary>

```regex
^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?$
```
</details>

**9. Match a 16-digit credit-card-like number with optional spaces/hyphens.**
<details>
  <summary>Answer</summary>

```regex
^(?:\d{4}[-\s]?){3}\d{4}$
```
</details>

**10. Match an IPv4 address structurally (four octets, dot-separated).**
<details>
  <summary>Answer</summary>

```regex
^(?:\d{1,3}\.){3}\d{1,3}$
```
> Note: Not strict 0–255; use extra checks programmatically for full validation.
</details>

---

## B. Anchors, Quantifiers & Alternation (11–20)

**11. Match a string that starts with “Hello” and ends with `!`.**
<details>
  <summary>Answer</summary>

```regex
^Hello.*!$
```
</details>

**12. Match one or more consecutive whitespace characters.**
<details>
  <summary>Answer</summary>

```regex
\s+
```
</details>

**13. Match either “color” or “colour”.**
<details>
  <summary>Answer</summary>

```regex
colou?r
```
</details>

**14. Match repeated adjacent words like `hello hello` (exact duplicate).**
<details>
  <summary>Answer</summary>

```regex
\b(\w+)\s+\1\b
```
</details>

**15. Match strings that do not contain digits (entire string).**
<details>
  <summary>Answer</summary>

```regex
^[^0-9]*$
```
</details>

**16. Match files with extensions `.png`, `.jpg`, `.jpeg`, `.gif` (case-insensitive).**
<details>
  <summary>Answer</summary>

```regex
(?i)^.+\.(?:png|jpg|jpeg|gif)$
```
</details>

**17. Match 3 to 6 lowercase letters only.**
<details>
  <summary>Answer</summary>

```regex
^[a-z]{3,6}$
```
</details>

**18. Match a word of length 8–20 that contains at least one digit and one uppercase letter.**
<details>
  <summary>Answer</summary>

```regex
^(?=.*\d)(?=.*[A-Z])[A-Za-z0-9]{8,20}$
```
</details>

**19. Match MAC addresses like `AA:BB:CC:DD:EE:FF` or `aa-bb-cc-dd-ee-ff`.**
<details>
  <summary>Answer</summary>

```regex
^(?:[0-9A-Fa-f]{2}([-:]))(?:[0-9A-Fa-f]{2}\1){4}[0-9A-Fa-f]{2}$
```
</details>

**20. Match HTML tags and capture the tag name from `<div>...</div>` (simple case).**
<details>
  <summary>Answer</summary>

```regex
^<([A-Za-z][A-Za-z0-9]*)\b[^>]*>.*?</\1>$
```
> Note: Not robust for nested/invalid HTML; demo use only.
</details>

---

## C. Groups, Backreferences & Capture (21–30)

**21. Capture the domain from an email `user@domain.com`.**
<details>
  <summary>Answer</summary>

```regex
^[^@\s]+@([^@\s]+\.[^@\s]+)$
```
</details>

**22. Match pairs of quotes with the same delimiter (`"..."` or `'...'`).**
<details>
  <summary>Answer</summary>

```regex
(["'])(.*?)\1
```
</details>

**23. Match a palindrome of length 4 (e.g., `abba`, `1221`).**
<details>
  <summary>Answer</summary>

```regex
^(.)(.)\2\1$
```
</details>

**24. Match duplicated words anywhere in a text (not necessarily adjacent).**
<details>
  <summary>Answer</summary>

```regex
\b(\w+)\b(?:.*\b\1\b)+
```
</details>

**25. Match numbers with thousands separators like `1,234`, `12,345,678` (no leading zeros unless 0).**
<details>
  <summary>Answer</summary>

```regex
^(?:0|[1-9]\d{0,2})(?:,\d{3})*$
```
</details>

**26. Extract the username from a GitHub URL like `https://github.com/mohan`.**
<details>
  <summary>Answer</summary>

```regex
^https?://github\.com/([A-Za-z0-9-]+)(?:/|$)
```
</details>

**27. Extract the file extension from `report.final.v2.pdf`.**
<details>
  <summary>Answer</summary>

```regex
^.*\.([A-Za-z0-9]+)$
```
</details>

**28. Match balanced parentheses with one level only (e.g., `(abc)`, not `(a(b)c)`).**
<details>
  <summary>Answer</summary>

```regex
^\([^()]*\)$
```
</details>

**29. Match a US phone number in common formats.**
<details>
  <summary>Answer</summary>

```regex
^(?:\(\d{3}\)\s?|\d{3}[-.]?)\d{3}[-.]?\d{4}$|^\d{10}$
```
</details>

**30. Match “word” boundaries around `cat` without using `\b` (use lookarounds).**
<details>
  <summary>Answer</summary>

```regex
(?<!\w)cat(?!\w)
```
</details>

---

## D. Lookarounds (31–40)

**31. Match digits that are followed by `kg` (don’t include `kg`).**
<details>
  <summary>Answer</summary>

```regex
\b\d+(?=\s?kg\b)
```
</details>

**32. Match words that are not followed by a comma (negative lookahead).**
<details>
  <summary>Answer</summary>

```regex
\b\w+\b(?!\s*,)
```
</details>

**33. Match `apple` only if preceded by `green` (whitespace optional).**
<details>
  <summary>Answer</summary>

```regex
(?<=\bgreen\s?)apple
```
</details>

**34. Match `foo` only if not preceded by `bar`.**
<details>
  <summary>Answer</summary>

```regex
(?<!bar)foo
```
</details>

**35. Match commas that are not inside quotes in a CSV line.**
<details>
  <summary>Answer</summary>

```regex
,(?=(?:[^"]*"[^"]*")*[^"]*$)
```
</details>

**36. Match words that contain at least two vowels (a,e,i,o,u) using lookaheads.**
<details>
  <summary>Answer</summary>

```regex
\b(?=(?:[^aeiou]*[aeiou]){2,}[^aeiou]*\b)\w+\b
```
</details>

**37. Match `https` URLs, excluding `http`.**
<details>
  <summary>Answer</summary>

```regex
^https://[^\s]+$
```
</details>

**38. Match a price like `$12.99` only if the line also contains `TOTAL`.**
<details>
  <summary>Answer</summary>

```regex
(?=.*\bTOTAL\b).*\$\d+(?:\.\d{2})?
```
</details>

**39. Match the last occurrence of a word in a line.**
<details>
  <summary>Answer</summary>

```regex
\b(\w+)\b(?!.*\b\1\b)
```
</details>

**40. Match a number only if it is between parentheses like `(123)`.**
<details>
  <summary>Answer</summary>

```regex
(?<=\()\d+(?=\))
```
</details>

---

## E. Validation Patterns (41–50)

**41. Strong password: min 8 chars, at least one uppercase, one lowercase, one digit, one special `!@#$%^&*`.**
<details>
  <summary>Answer</summary>

```regex
^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$
```
</details>

**42. Practical email (interview-level, not RFC-perfect).**
<details>
  <summary>Answer</summary>

```regex
^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$
```
</details>

**43. Indian mobile: 10 digits, first digit 6–9; optional `+91` with spaces/hyphens.**
<details>
  <summary>Answer</summary>

```regex
^(?:\+91[\s-]?)?[6-9]\d{9}$
```
</details>

**44. ISO-8601 time `HH:MM:SS` (00–23 hour).**
<details>
  <summary>Answer</summary>

```regex
^(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d$
```
</details>

**45. UUID v4 (case-insensitive).**
<details>
  <summary>Answer</summary>

```regex
^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-4[0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$
```
</details>

**46. E.164 international phone number (up to 15 digits, leading `+`).**
<details>
  <summary>Answer</summary>

```regex
^\+[1-9]\d{1,14}$
```
</details>

**47. URL (http/https), optional `www`, domain, optional path/query (reasonable).**
<details>
  <summary>Answer</summary>

```regex
^https?:\/\/(?:www\.)?[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:\/[^
\s?#]*)?(?:\?[^
\s#]*)?(?:#[^\s]*)?$
```
</details>

**48. PAN (India): 5 letters, 4 digits, 1 letter (e.g., `ABCDE1234F`).**
<details>
  <summary>Answer</summary>

```regex
^[A-Z]{5}\d{4}[A-Z]$
```
</details>

**49. GSTIN (simplified structure).**
<details>
  <summary>Answer</summary>

```regex
^\d{2}[A-Z]{5}\d{4}[A-Z][A-Z1-9][Z][A-Z\d]$
```
</details>

**50. Valid month/day ranges in `YYYY-MM-DD` (basic month/day validation).**
<details>
  <summary>Answer</summary>

```regex
^\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$
```
</details>

---

## Tips
- Use non-capturing groups `(?:...)` when you don’t need backreferences.
- State your regex flavor & flags (`i`, `m`, `s`, `g`) in interviews.
- For complex validation (emails, IP strict ranges, HTML), note regex limits and consider post-validation logic.

