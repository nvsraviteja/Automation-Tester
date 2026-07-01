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

## 6. Catching Generic Exceptions

### `except Exception as e`
Sometimes you want a **safety net** to catch any unexpected exception that you didn't specifically plan for — without hiding what actually went wrong. The `as e` part lets you access the actual exception object, including its error message.

```python
try:
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")
```

**Output:**
```
An error occurred: division by zero
```

### Combining Specific + Generic Handling

```python
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("You can't divide by zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

This pattern handles the errors you **expect** specifically, and still safely catches anything **unexpected** — while telling you what it actually was, instead of silently failing.

> **Note:** `Exception` catches almost all errors but not things like `SystemExit` or `KeyboardInterrupt`, which inherit directly from `BaseException`. This is intentional — you generally don't want to accidentally swallow a user's `Ctrl+C` interrupt.

---

## 7. `finally` Block

The `finally` block contains code that **always runs**, whether or not an exception occurred — and even if the exception was never caught.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This always runs, no matter what")
```

**Output:**
```
Cannot divide by zero
This always runs, no matter what
```

### Even Without an Exception

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This always runs")
```

**Output:**
```
This always runs
```

### Even If the Exception Isn't Caught

```python
try:
    result = 10 / 0
except ValueError:  # doesn't match ZeroDivisionError
    print("Value error")
finally:
    print("Finally block still runs")
# Then the program crashes with the uncaught ZeroDivisionError,
# but "Finally block still runs" prints first.
```

**Why this matters:** `finally` is the right place for **cleanup code** — things that absolutely must happen regardless of success or failure (closing files, closing browser sessions, releasing resources).

---

## 8. Cleanup with `finally` in QA

In test automation, certain resources (browsers, files, database connections) **must be closed properly** even if a test fails or throws an error. `finally` guarantees this cleanup happens.

### Browser Cleanup

```python
from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("https://example.com")
    element = driver.find_element("id", "nonexistent-element")  # might raise an error
    element.click()
except Exception as e:
    print(f"Test failed: {e}")
finally:
    driver.quit()  # browser ALWAYS closes, pass or fail
```

Without `finally`, if `find_element` fails, `driver.quit()` might never run — leaving browser processes open and consuming memory/resources across test runs.

### File Cleanup

```python
file = open("test_log.txt", "a")

try:
    file.write("Test started\n")
    result = 10 / 0  # error occurs
    file.write("Test passed\n")
except ZeroDivisionError:
    file.write("Test failed: division by zero\n")
finally:
    file.close()  # file ALWAYS closes properly
```

> **Note:** Using `with open(...)` already handles file closing automatically (as covered in Story 3), so `finally` is more commonly used for things like browser sessions, database connections, or external resources that don't have a built-in context manager.

---

## 9. Raising Exceptions Manually

### `raise`
The `raise` keyword lets you **manually trigger** an exception — even if Python itself wouldn't normally raise one at that point. This is useful for enforcing rules in your own code.

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(f"Age set to {age}")

set_age(-5)
```

**Output:**
```
ValueError: Age cannot be negative
```

### Raising and Catching Your Own Exception

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero in this function")
    return a / b

try:
    divide(10, 0)
except ZeroDivisionError as e:
    print(f"Caught an error: {e}")
```

### Re-raising an Exception
Sometimes you want to handle part of an error (e.g., log it) but still let it propagate up:

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Logging error: {e}")
    raise  # re-raises the same exception after logging it
```

---

## 10. Validation Using `raise`

A very common, practical use of `raise` is **input/data validation** — making sure data meets certain rules **before** your program proceeds, rather than letting it fail later in a confusing way.

```python
def create_user(username, age):
    if not username:
        raise ValueError("Username cannot be empty")
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 18:
        raise ValueError("User must be at least 18 years old")

    print(f"User '{username}' created successfully, age {age}")

try:
    create_user("Alice", 16)
except (ValueError, TypeError) as e:
    print(f"Validation failed: {e}")
```

**Output:**
```
Validation failed: User must be at least 18 years old
```

### Why Validate with `raise` Instead of Just Returning `None` or `False`?
- **Forces the caller to handle the problem** — they can't accidentally ignore a failed validation the way they might ignore a returned `False`.
- **Clear, descriptive error messages** make debugging much faster.
- **Fails fast** — catches bad data immediately, instead of letting it cause confusing errors deep inside your program later.

---

## 11. Exception Handling in QA Framework Usage

Exception handling is essential throughout a QA automation framework — at the **page object** level, the **test** level, and the **framework/utility** level — to keep test suites stable, informative, and resilient to individual failures.

### Example: Page Object Level

```python
# pages/login_page.py
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        try:
            self.driver.find_element("id", "username").send_keys(username)
            self.driver.find_element("id", "password").send_keys(password)
            self.driver.find_element("id", "login-btn").click()
        except Exception as e:
            raise RuntimeError(f"Login action failed: {e}")
```

Here, the page object catches low-level Selenium exceptions and **re-raises** a clearer, more meaningful error for whoever calls `login()`.

### Example: Test Level

```python
# tests/test_login.py
from pages.login_page import LoginPage

def test_login_with_invalid_credentials(driver):
    login_page = LoginPage(driver)
    try:
        login_page.login("baduser", "wrongpass")
    except RuntimeError as e:
        print(f"Expected failure occurred: {e}")
    finally:
        driver.quit()  # cleanup always happens
```

### Example: Utility Level — Reading Test Data Safely

```python
# utils/data_reader.py
import json

def load_test_data(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Test data file not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Test data file is not valid JSON: {file_path}")
```

This gives **clear, specific error messages** if test data is missing or malformed — instead of a cryptic crash deep inside the test run.

### Example: Validating Test Data Before Running Tests

```python
def validate_credentials(cred):
    if "username" not in cred or "password" not in cred:
        raise KeyError("Test data missing 'username' or 'password' field")
    return True

for cred in credentials:
    try:
        validate_credentials(cred)
        login_page.login(cred["username"], cred["password"])
    except KeyError as e:
        print(f"Skipping invalid test data: {e}")
        continue
```

### Why This Matters for QA
- **Isolates failures** — one bad test or one piece of bad data doesn't crash the entire suite; other tests still run.
- **Better reporting** — clear exception messages make it obvious *why* a test failed (bad data vs. broken UI vs. timeout) instead of a generic crash.
- **Guaranteed cleanup** — `finally` ensures browsers, files, and connections close properly after every test, pass or fail, preventing resource leaks across long test runs.
- **Fail-fast validation** — `raise` on bad test data catches problems immediately, rather than letting them cause confusing failures several steps later.

---

## Summary Table

| Concept | Purpose |
|---|---|
| `try` / `except` | Catch and handle errors instead of crashing |
| Specific exceptions | Catch only expected error types; keeps debugging clear |
| Broad `except` | Catches everything — use sparingly, can hide bugs |
| Common exception types | `ValueError`, `TypeError`, `KeyError`, `IndexError`, `ZeroDivisionError`, `FileNotFoundError`, `NameError`, `ModuleNotFoundError`, `AssertionError`, `TimeoutError` |
| Multiple `except` blocks | Handle different error types differently, most specific first |
| `except Exception as e` | Generic safety net; still shows the actual error message |
| `finally` | Code that always runs — used for guaranteed cleanup |
| `raise` | Manually trigger an exception (custom rules, validation, re-raising) |
| Validation with `raise` | Fail fast with clear error messages on bad data/input |
| QA Framework Usage | Isolate failures, guarantee cleanup, and validate test data for stable automation |
