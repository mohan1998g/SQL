#!/usr/bin/env python3
import re, json, sys

with open("regex_testcases.json", "r", encoding="utf-8") as f:
    data = json.load(f)

failures = []

for case in data["cases"]:
    pat = case["pattern"]
    try:
        rx = re.compile(pat)
    except re.error as e:
        failures.append({"id": case["id"], "error": f"CompileError: {e}", "pattern": pat})
        continue
    for t in case["tests"]:
        s = t["input"]
        m = rx.search(s) is not None
        if m != t["shouldMatch"]:
            failures.append({"id": case["id"], "pattern": pat, "input": s, "expected": t["shouldMatch"], "actual": m})

print(f"Total cases: {len(data['cases'])}")
print(f"Failures: {len(failures)}")
if failures:
    for f in failures[:50]:  # cap output
        print("- Case #{id}: {err} pattern={pattern} input={input} expected={expected} actual={actual}".format(
            id=f.get("id"), err=f.get("error", ""), pattern=f.get("pattern"), input=f.get("input"), expected=f.get("expected"), actual=f.get("actual")
        ))
    sys.exit(1)
