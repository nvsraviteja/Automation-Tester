# Day 11 - Loop Patterns

## 1. Loop Through a String

A `for` loop can iterate through the characters of a string directly, not just numbers.

```python
for char in "Ravi":
    print(char)
```

**Output:**
```
R
a
v
i
```

**Before today:**
```python
for i in range(...)
```

**From today:**
```python
for char in string
```

---

## 2. Counter Pattern

Used to count how many times a condition is met inside a loop.

```python
count = 0

for item in something:
    if condition:
        count += 1
```

**Examples:**

| String | Count target | Answer |
|--------|--------------|--------|
| `banana` | Count `"a"` | 3 |
| `google` | Count `"o"` | 2 |
| `education` | Count vowels | 5 |

---

## 3. Validator Pattern

Used to check whether something exists in a sequence. Instead of counting, it just checks if at least one match is found.

```python
found = False

for item in something:
    if condition:
        found = True
```

**Examples of what it can check:**
- Does the string have a digit?
- Does the string have an uppercase letter?
- Does the string contain a banned word?

**Counter vs Validator:**

| Pattern | Question it answers |
|---------|---------------------|
| Counter | How many exist? |
| Validator | Does at least one exist? |

---

## 4. Password Validation Logic

Using the validator pattern, we can enforce password rules.

**Rules — a password must contain:**
- At least one digit
- At least one uppercase letter
- At least one special symbol

**Example of a valid password:** `Ravi@123`

| Rule | Met by |
|------|--------|
| Uppercase | `R` |
| Digit | `1`, `2`, `3` |
| Special symbol | `@` |
