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
---

## 4. Common Exception Types

| Exception | When It Occurs | Example |
|---|---|---|
| `ValueError` | A function receives an argument of the right type but an invalid value | `int("abc")` |
| `TypeError` | An operation is performed on an incompatible data type | `"5" + 5` |
| `KeyError` | Trying to access a dictionary key that doesn't exist | `data["missing_key"]` |
| `IndexError` | Trying to access a list/tuple index that's out of range | `my_list[10]` on a 3-item list |
| `ZeroDivisionError` | Dividing a number by zero | `10 / 0` |
| `FileNotFoundError` | Trying to open a file that doesn't exist | `open("missing.txt")` |
| `NameError` | Using a variable that hasn't been defined | `print(undefined_var)` |
| `ModuleNotFoundError` | Trying to import a module that doesn't exist/isn't installed | `import non_existent_module` |
| `AssertionError` | An `assert` statement evaluates to `False` | `assert 1 == 2` |
| `TimeoutError` | An operation exceeds its allotted time (common in network calls, waits) | Waiting too long for a page element to load |

### Quick Examples

```python
# ValueError
int("abc")  # ValueError: invalid literal for int() with base 10: 'abc'

# TypeError
"5" + 5  # TypeError: can only concatenate str (not "int") to str

# KeyError
data = {"name": "Alice"}
data["age"]  # KeyError: 'age'

# IndexError
my_list = [1, 2, 3]
my_list[10]  # IndexError: list index out of range

# ZeroDivisionError
10 / 0  # ZeroDivisionError: division by zero

# FileNotFoundError
open("missing_file.txt", "r")  # FileNotFoundError

# NameError
print(undefined_variable)  # NameError: name 'undefined_variable' is not defined

# ModuleNotFoundError
import non_existent_module  # ModuleNotFoundError

# AssertionError
assert 1 == 2, "1 is not equal to 2"  # AssertionError: 1 is not equal to 2

# TimeoutError
# Example: waiting for a web element that never appears within the timeout limit
```

---

## 5. Handling Multiple Exceptions

### Multiple `except` Blocks
A single `try` block can be followed by **multiple `except` blocks**, each handling a different exception type. Python checks them in order and runs the first one that matches.

```python
try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print(result)
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
```

### Handling Multiple Exception Types in One Block
If you want the **same** handling logic for multiple exception types, group them in a tuple:

```python
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except (ValueError, ZeroDivisionError) as e:
    print(f"Invalid input or operation: {e}")
```

### Order Matters
Always put **more specific** exceptions before more **general** ones. If a general exception (like `Exception`) is listed first, it will catch everything, and the more specific blocks below it will never run.

```python
try:
    risky_operation()
except Exception:        # too broad — placed first, catches everything
    print("Generic error")
except ValueError:        # this will NEVER run
    print("Value error")
```

---
