# Sprint 2 — Story 4: Exception Handling

## Topics Covered
1. Why Exception Handling Matters
2. Basic Exception Structure (`try`, `except`)
3. Broad `except` vs Specific Exceptions
4. Common Exception Types
5. Handling Multiple Exceptions
6. Catching Generic Exceptions (`except Exception as e`)
7. `finally` Block
8. Cleanup with `finally` in QA
9. Raising Exceptions Manually (`raise`)
10. Validation Using `raise`
11. Exception Handling in QA Framework Usage

---

## 1. Why Exception Handling Matters

An **exception** is an error that occurs while a program is running, which — if left unhandled — causes the program to **crash immediately**.

```python
print("Start")
result = 10 / 0  # ZeroDivisionError — program crashes here
print("End")     # this line never runs
```

```
Start
ZeroDivisionError: division by zero
```

**Exception handling** lets you anticipate these errors and respond gracefully instead of letting the entire program stop.

### Why it matters
- **Prevents crashes** — your program keeps running even when something unexpected happens.
- **Better user/tester experience** — instead of a cryptic crash, you can show a clear, helpful message.
- **Critical for QA/automation** — a single failed test step (e.g., an element not found) shouldn't crash your entire test suite; it should fail gracefully, log the issue, and let other tests continue.
- **Allows cleanup** — closing files, browsers, or database connections properly even when something goes wrong.

---

## 2. Basic Exception Structure

### `try`
The `try` block contains code that **might** raise an exception. Python attempts to run this code normally.

### `except`
The `except` block contains code that runs **only if** an exception occurs inside the `try` block. It "catches" the error instead of letting it crash the program.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Program continues running...")
```

**Output:**
```
You can't divide by zero!
Program continues running...
```

Without the `try`/`except`, the program would have crashed at the division and never printed the last line.

---

## 3. Broad `except` vs Specific Exceptions

You can write an `except` block that catches **any and all** exceptions, or one that catches only a **specific** type of exception.

### Broad `except` (catches everything)

```python
try:
    result = 10 / 0
except:
    print("Something went wrong")
```

### Specific Exception (catches only that type)

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
```

### Why Specific Is Better

| Broad `except` | Specific `except` |
|---|---|
| Catches every possible error, even ones you didn't expect (typos, logic bugs) | Catches only the error type you're prepared to handle |
| Can **hide real bugs** — you might never realize something else is broken | Makes debugging easier — errors you didn't anticipate still surface |
| Hard to know what actually went wrong | Clear, predictable error handling |

**Best practice:** Always catch the **most specific exception** you can. Use broad exception handling only as a last-resort safety net (and even then, log/print the actual error — see `except Exception as e` below).

```python
# Avoid this:
try:
    risky_operation()
except:
    pass  # silently swallows ALL errors — very dangerous!

# Prefer this:
try:
    risky_operation()
except ValueError:
    print("Invalid value provided")
```

---
