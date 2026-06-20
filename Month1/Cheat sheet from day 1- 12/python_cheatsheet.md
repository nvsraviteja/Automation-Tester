# Python Cheat Sheet — Days 1 to 12

---

## Variables & Data Types

```python
name = "Ravi"        # String
age = 25             # Integer
height = 5.9         # Float
is_active = True     # Boolean
```

- Variable names cannot start with a number or contain a hyphen
- Python uses the most recently assigned value

---

## User Input

```python
a = input("Enter your age: ")   # always returns a string
print(type(a))                  # <class 'str'>
```

---

## Type Conversion

| Function | Converts to |
|----------|-------------|
| `int()` | Integer |
| `float()` | Float |
| `str()` | String |
| `bool()` | Boolean |

```python
age = int(input("Enter your age: "))
```

> `int()` removes the decimal part, it does not round.

---

## String Formatting

```python
name = "Ravi"
age = 25

# Using commas
print("My name is", name, "and I am", age, "years old.")

# Using f-strings (recommended)
print(f"My name is {name} and I am {age} years old.")
```

---

## Operators

### Arithmetic

| Operator | Operation | Example |
|----------|-----------|---------|
| `+` | Addition | `5 + 3 = 8` |
| `-` | Subtraction | `5 - 3 = 2` |
| `*` | Multiplication | `5 * 3 = 15` |
| `/` | Division | `9 / 2 = 4.5` |
| `%` | Modulus (remainder) | `9 % 2 = 1` |

### Comparison

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

> Comparison operators return `True` or `False`. They do not change any value.

### Assignment

| Operator | Meaning | Example |
|----------|---------|---------|
| `=` | Assign | `x = 10` |
| `+=` | Add and assign | `x += 3` → `x = x + 3` |
| `-=` | Subtract and assign | `x -= 3` → `x = x - 3` |
| `*=` | Multiply and assign | `x *= 2` → `x = x * 2` |
| `/=` | Divide and assign | `x /= 2` → `x = x / 2` |

### Logical

| Operator | Behaviour |
|----------|-----------|
| `and` | Both conditions must be `True` |
| `or` | At least one condition must be `True` |
| `not` | Reverses the result |

### Membership

| Operator | Behaviour |
|----------|-----------|
| `in` | Returns `True` if value is found |
| `not in` | Returns `True` if value is not found |

---

## Conditional Statements

```python
# if
if condition:
    action

# if-else
if condition:
    true_action
else:
    false_action

# elif
if condition1:
    action
elif condition2:
    action
else:
    action

# Nested if
if condition1:
    if condition2:
        action
```

> Python executes only the first `True` branch, not all of them.
> The colon `:` and indentation are mandatory.

---

## Loops

### While Loop

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

| Part | Purpose |
|------|---------|
| Initialization | Sets the starting value |
| Condition | Keeps loop running while `True` |
| Update | Moves toward stopping |

### For Loop

```python
for i in range(1, 6):
    print(i)
```

### range()

| Syntax | Behaviour |
|--------|-----------|
| `range(stop)` | Starts at `0`, increments by `1` |
| `range(start, stop)` | Increments by `1` |
| `range(start, stop, step)` | Custom step |

> `start` is included. `stop` is excluded.

### Loop Through String / List

```python
for char in "Ravi":
    print(char)

for test in tests:
    print(test)
```

### Loop Control

| Statement | Behaviour |
|-----------|-----------|
| `break` | Exits the loop immediately |
| `continue` | Skips current iteration, moves to next |

---

## For vs While

| Use `for` when | Use `while` when |
|----------------|------------------|
| Number of iterations is known | Loop continues until a condition changes |

---

## Strings

```python
name = "QA Automation"

# Indexing
name[0]       # Q  (positive)
name[-1]      # n  (negative)

# Length
len(name)     # 13

# Slicing
name[0:2]     # QA
name[:2]      # QA  (start defaults to 0)
name[3:]      # Automation (end defaults to last)
name[:]       # QA Automation (whole string)
name[::2]     # every 2nd character
name[::-1]    # reverse
```

### String Methods

| Method | What it does |
|--------|--------------|
| `.upper()` | Converts to uppercase |
| `.lower()` | Converts to lowercase |
| `.strip()` | Removes leading and trailing spaces |
| `.replace(old, new)` | Replaces a value with a new one |

---

## Lists

```python
tests = ["Ad-hoc", "Regression", "Performance"]

# Indexing
tests[0]      # Ad-hoc
tests[-1]     # Performance

# Length
len(tests)    # 3

# Mutability — change a value
tests[1] = "Compatibility"

# Add item
tests.append("Smoke")

# Remove item
tests.remove("Smoke")

# Loop through
for test in tests:
    print(test)
```

---

## Common Error Messages

| Error | Cause |
|-------|-------|
| `NameError` | Variable or function not defined or mistyped |
| `ValueError` | Correct type but incompatible value (e.g. `int("hey")`) |
| `SyntaxError` | Code is incomplete or unreadable by Python |
| `IndentationError` | Incorrect spacing inside a code block |
| `IndexError` | Index is out of the valid range |

---

## Loop Patterns

### Counter Pattern

```python
count = 0
for item in something:
    if condition:
        count += 1
```

### Validator Pattern

```python
found = False
for item in something:
    if condition:
        found = True
```

| Pattern | Question it answers |
|---------|---------------------|
| Counter | How many exist? |
| Validator | Does at least one exist? |
