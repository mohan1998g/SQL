
# Regex Shorthand vs Explicit Classes Cheat Sheet

> **How to use:** Click **Details** under each section to reveal examples and test cases.

---

## 1. Digits
<details>
  <summary>\d vs [0-9]</summary>

**Shorthand:** `\d`  
**Explicit:** `[0-9]`  
**Meaning:** Matches any digit (0–9). In Unicode mode, `\d` may match non-ASCII digits too.

**Examples:**
```regex
\d{2}      # Two digits
[0-9]{2}    # Two digits (ASCII only)
```

**Test Cases:**
| Input      | Pattern    | Expected |
|------------|-----------|----------|
| `12`       | `\d{2}` | ✅       |
| `12`       | `[0-9]{2}`| ✅       |
| `१२` (Hindi digits) | `\d{2}` | ✅ (Unicode) |
| `१२`       | `[0-9]{2}`| ❌       |

</details>

## 2. Non-Digits
<details>
  <summary>\D vs [^0-9]</summary>

**Shorthand:** `\D`  
**Explicit:** `[^0-9]`  
**Meaning:** Matches any non-digit character.

**Examples:**
```regex
\D+       # One or more non-digits
[^0-9]+    # One or more non-digits
```

**Test Cases:**
| Input      | Pattern    | Expected |
|------------|-----------|----------|
| `abc`      | `\D+`   | ✅       |
| `123`      | `\D+`   | ❌       |

</details>

## 3. Word Characters
<details>
  <summary>\w vs [A-Za-z0-9_]</summary>

**Shorthand:** `\w`  
**Explicit:** `[A-Za-z0-9_]`  
**Meaning:** Matches letters, digits, underscore.

**Examples:**
```regex
\w+       # One or more word chars
[A-Za-z0-9_]+ # Same explicitly
```

**Test Cases:**
| Input      | Pattern    | Expected |
|------------|-----------|----------|
| `hello_123`| `\w+`   | ✅       |
| `@#$`      | `\w+`   | ❌       |

</details>

## 4. Non-Word Characters
<details>
  <summary>\W vs [^A-Za-z0-9_]</summary>

**Shorthand:** `\W`  
**Explicit:** `[^A-Za-z0-9_]`  
**Meaning:** Matches any character that is not a letter, digit, or underscore.

**Examples:**
```regex
\W+       # One or more non-word chars
[^A-Za-z0-9_]+ # Same explicitly
```

**Test Cases:**
| Input      | Pattern    | Expected |
|------------|-----------|----------|
| `@#$`      | `\W+`   | ✅       |
| `abc`      | `\W+`   | ❌       |

</details>

## 5. Whitespace
<details>
  <summary>\s vs [ 	
]</summary>

**Shorthand:** `\s`  
**Explicit:** `[ 	
]`  
**Meaning:** Matches spaces, tabs, newlines, etc.

**Examples:**
```regex
\s+       # One or more whitespace chars
[ 	
]+ # Same explicitly
```

**Test Cases:**
| Input      | Pattern    | Expected |
|------------|-----------|----------|
| ` 	`      | `\s+`   | ✅       |
| `abc`      | `\s+`   | ❌       |

</details>

## 6. Non-Whitespace
<details>
  <summary>\S vs [^ 	
]</summary>

**Shorthand:** `\S`  
**Explicit:** `[^ 	
]`  
**Meaning:** Matches any non-whitespace character.

**Examples:**
```regex
\S+       # One or more non-whitespace chars
[^ 	
]+ # Same explicitly
```

**Test Cases:**
| Input      | Pattern    | Expected |
|------------|-----------|----------|
| `abc`      | `\S+`   | ✅       |
| ` 	`      | `\S+`   | ❌       |

</details>

---

## Anchors & Boundaries
<details>
  <summary>^, $, , \B</summary>

| Symbol | Meaning | Example |
|--------|---------|---------|
| `^`    | Start of string | `^Hello` matches `Hello world` |
| `$`    | End of string | `world$` matches `Hello world` |
| `\b` | Word boundary | `\bcat\b` matches `cat` but not `concatenate` |
| `\B` | Non-word boundary | `\Bcat\B` matches inside `concatenate` |

</details>

---

## Quantifiers
<details>
  <summary>* + ? {n} {n,} {n,m}</summary>

| Quantifier | Meaning | Example |
|------------|---------|---------|
| `*`        | 0 or more | `a*` matches ``, `a`, `aaa` |
| `+`        | 1 or more | `a+` matches `a`, `aaa` |
| `?`        | 0 or 1 | `a?` matches ``, `a` |
| `{n}`      | Exactly n | `\d{3}` matches `123` |
| `{n,}`     | n or more | `\d{2,}` matches `12`, `1234` |
| `{n,m}`    | Between n and m | `\d{2,4}` matches `12`, `1234` |

</details>

---

**Tip:** Use `[0-9]` for strict ASCII digits; use `\d` for convenience or Unicode digits.

