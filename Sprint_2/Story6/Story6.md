# Sprint 2 — Story 6: Logging

## Topics Covered
1. What is Logging
2. Why Logging is Needed
3. Problems with `print()`
4. Importing the Logging Module
5. Basic Logging Statements
6. Log Levels & Severity Order
7. Choosing the Correct Log Level
8. Configuring Logging
9. Controlling Visible Logs
10. File Logging
11. Logging Output Formatting
12. Logging vs `print()`
13. QA Automation Use Cases
14. Logging in Real Frameworks
15. Best Practices
16. Logging in QA Framework Usage

---

## 1. What is Logging

**Logging** is the practice of recording messages about what your program is doing as it runs — capturing events, status updates, warnings, and errors into a structured, configurable output stream (the terminal, a file, or both).

Python's built-in `logging` module provides a fully featured system for this, far more powerful and flexible than simply using `print()`.

```python
import logging

logging.warning("This is a warning message")
# WARNING:root:This is a warning message
```

---

## 2. Why Logging is Needed

### Better than `print()`
`print()` dumps raw text with no context — no timestamp, no severity, no easy way to turn it on or off without deleting code. The `logging` module gives every message a **level**, **timestamp**, and **source** automatically, and lets you control what gets shown with a single configuration line.

### Useful for Debugging
Logs create a detailed trail of what your program did, in what order, and what it encountered. When something breaks (especially in automation that runs overnight or in CI/CD), you can read the log to understand exactly what happened — without having to re-run and watch in real time.

### Tracks Execution Flow
In large QA frameworks, logs let you trace the full sequence of events:
- Which test ran first
- Which page was navigated to
- Which API endpoint was hit
- Where exactly a failure occurred

This visibility is impossible to get from `print()` at any meaningful scale.

---

## 3. Problems with `print()`

| Problem | Why It Matters |
|---|---|
| **No severity level** | You can't distinguish between debug noise, informational messages, and real errors — everything looks the same |
| **No timestamps** | You can't tell when an event happened or how long something took |
| **Hard to disable** | To silence debug output, you have to manually find and delete (or comment out) `print()` calls across the entire codebase |
| **No file output** | `print()` only writes to the terminal — you can't easily redirect it to a log file for CI/CD |
| **Hard to debug large frameworks** | In a framework with dozens of files and hundreds of test steps, a wall of undifferentiated `print()` output is nearly impossible to parse |

```python
# What print() gives you:
print("clicking login button")

# What logging gives you:
# 2025-07-01 10:23:45 - INFO - clicking login button
```

---

## 4. Importing the Logging Module

The `logging` module is part of Python's standard library — no `pip install` required.

```python
import logging
```

That's all it takes to gain access to the full logging system.

---

## 5. Basic Logging Statements

The `logging` module provides five functions for recording messages, each corresponding to a **severity level**:

```python
import logging

logging.debug("Detailed diagnostic information — very granular")
logging.info("General information — something happened as expected")
logging.warning("Something unexpected, but the program continues")
logging.error("A real problem occurred — something failed")
logging.critical("A severe error — the program may not be able to continue")
```

---

## 6. Log Levels

Every log message has a **level** (also called severity) that indicates how important or serious the message is.

| Level | Numeric Value | Meaning |
|---|---|---|
| `DEBUG` | 10 | Highly detailed diagnostic info — used during development/troubleshooting |
| `INFO` | 20 | General operational messages — confirms things are working as expected |
| `WARNING` | 30 | Something unexpected happened but didn't cause a failure — worth noting |
| `ERROR` | 40 | A real error occurred — a function/test step failed |
| `CRITICAL` | 50 | A severe error — the system or framework may be unable to continue |

### Severity Order

```
DEBUG < INFO < WARNING < ERROR < CRITICAL
  10  <  20  <   30    <  40   <   50
```

This order controls **filtering** — when you set a minimum log level, Python shows only messages at that level **and above**.

---

## 7. Choosing the Correct Log Level

| Situation | Correct Level | Example |
|---|---|---|
| Detailed debug/diagnostic info during development | `DEBUG` | Variable values, step-by-step flow, intermediate states |
| Normal progress / expected events | `INFO` | "Test started", "Login successful", "Browser launched" |
| Something unexpected but non-fatal | `WARNING` | "Response slower than expected", "Retrying request (attempt 2 of 3)" |
| A specific operation/test step failed | `ERROR` | "Login failed: invalid credentials", "Element not found" |
| A crash or severe system-level failure | `CRITICAL` | "WebDriver process died unexpectedly", "Database connection lost" |

**Rule of thumb:**
- Use `DEBUG` for information you only want to see while actively troubleshooting — it's too noisy for routine runs.
- Use `INFO` for things you'd want in a normal test run log.
- Use `WARNING` when something is off but didn't break the flow.
- Use `ERROR` when a test step or function fails.
- Use `CRITICAL` sparingly — for failures that compromise the entire framework, not just one test.

---

## 8. Configuring Logging

By default, Python's logging module only shows `WARNING` and above. To control behavior globally, use `logging.basicConfig()` — call it **once**, near the start of your program, before any log messages are written.

### `logging.basicConfig(level=logging.INFO)`

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.debug("This won't show — DEBUG is below INFO")
logging.info("This will show")
logging.warning("This will show")
logging.error("This will show")
```

**Output:**
```
INFO:root:This will show
WARNING:root:This will show
ERROR:root:This will show
```

---

## 9. Controlling Visible Logs

The `level` parameter in `basicConfig()` acts as a **filter** — only messages at or above the set level are displayed.

### Showing INFO and Above

```python
logging.basicConfig(level=logging.INFO)
# Shows: INFO, WARNING, ERROR, CRITICAL
# Hides: DEBUG
```

### Hiding DEBUG (the default behaviour)

```python
logging.basicConfig(level=logging.WARNING)
# Shows: WARNING, ERROR, CRITICAL
# Hides: DEBUG, INFO
```

### Showing Everything (including DEBUG)

```python
logging.basicConfig(level=logging.DEBUG)
# Shows: DEBUG, INFO, WARNING, ERROR, CRITICAL
```

This makes switching between verbose (development) and quiet (production/CI) output as simple as changing **one line**.

---

## 10. File Logging

Instead of (or in addition to) printing to the console, you can direct log output to a **file** — essential for CI/CD pipelines and overnight test runs where you can't watch the terminal in real time.

### Store Logs in a File — `filename="test.log"`

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="test.log"
)

logging.info("Test run started")
logging.error("Login test failed")
logging.info("Test run complete")
```

**Resulting `test.log`:**
```
INFO:root:Test run started
ERROR:root:Login test failed
INFO:root:Test run complete
```

### Logging to Both File and Console

By default, `filename` redirects output **only** to the file (not the console). To log to both simultaneously, use **handlers**:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("test.log"),
        logging.StreamHandler()           # prints to console
    ]
)

logging.info("This appears in both the file and the terminal")
```

---

## 11. Logging Output Formatting

The default format (`INFO:root:message`) is functional but minimal. You can customize it using the `format` parameter.

### Common Format Placeholders

| Placeholder | Meaning |
|---|---|
| `%(levelname)s` | The severity level (DEBUG, INFO, WARNING, etc.) |
| `%(message)s` | The actual log message |
| `%(asctime)s` | Timestamp of when the message was logged |
| `%(name)s` | Logger name (default: `root`) |
| `%(filename)s` | Name of the Python file that logged the message |
| `%(lineno)d` | Line number in the source file |

### Severity in Output (Without Timestamp)

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

logging.info("Login page loaded")
logging.warning("Slow response detected")
```

**Output:**
```
INFO - Login page loaded
WARNING - Slow response detected
```

### Custom Format with Timestamps

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Test started")
logging.error("Assertion failed")
```

**Output:**
```
2025-07-01 10:23:45,123 - INFO - Test started
2025-07-01 10:23:47,456 - ERROR - Assertion failed
```

Timestamps are especially valuable in test logs — they let you see exactly when each step happened and how long steps took, which is critical for identifying timeouts or performance regressions.

---

## 12. Logging vs `print()`

| | `print()` | `logging` |
|---|---|---|
| **Severity levels** | None — all output looks the same | Full levels: DEBUG, INFO, WARNING, ERROR, CRITICAL |
| **Timestamps** | Not included | Configurable — add with `%(asctime)s` |
| **Filtering** | Can't filter — comment out or delete manually | One config line changes what's shown |
| **File output** | Not built-in — requires manual redirection | Native — just add `filename=` or `FileHandler` |
| **Suitable for** | Quick checks, learning, interactive scripts | Production code, automation frameworks, CI/CD |
| **Disabling** | Delete or comment out code | Change log level — zero code changes needed |

### When to Use `print()`
- Quick, throwaway scripts
- Learning and experimenting
- Checking a value during interactive development
- Output that is **always meant to be visible** (e.g., a script's final result shown to a user)

### When to Use `logging`
- Any real automation framework
- Code running in CI/CD
- Code that others will maintain
- Any time you need to distinguish between severity levels, store output in a file, or toggle verbosity without editing code

---

## 13. QA Automation Use Cases

| Event | Log Level | Example Message |
|---|---|---|
| Test starting or ending | `INFO` | `"test_login_valid — STARTED"` |
| Browser launched | `INFO` | `"Chrome browser launched successfully"` |
| Navigation to a page | `INFO` | `"Navigated to https://example.com/login"` |
| Slow server response | `WARNING` | `"API response took 5.2s — above 3s threshold"` |
| Retrying a flaky step | `WARNING` | `"Element not found, retrying (attempt 2 of 3)"` |
| Assertion failure | `ERROR` | `"Expected: 'Welcome Alice', Got: 'Login failed'"` |
| Element not found | `ERROR` | `"NoSuchElementException: #submit-btn not found"` |
| API call failure | `ERROR` | `"POST /api/login returned 500 Internal Server Error"` |
| WebDriver crash | `CRITICAL` | `"WebDriver process died — aborting test suite"` |

---

## 14. Logging in Real Frameworks

### Console Logs
During local development, INFO-level logs in the terminal give a live view of what the test is doing step by step — what page was loaded, what action was taken, what response was received.

### CI/CD Debugging
When tests run on a build server (GitHub Actions, Jenkins, GitLab CI), you can't watch the terminal interactively. Logs written to a file are **saved as artifacts** after the run, so you can download and review them to diagnose failures — even for runs that finished hours ago.

### Failure Analysis
With well-structured logging, a failed test tells you **exactly** what went wrong:

```
2025-07-01 10:23:45 - INFO  - test_login_valid STARTED
2025-07-01 10:23:45 - INFO  - Navigated to https://example.com/login
2025-07-01 10:23:46 - INFO  - Entered username: test_user
2025-07-01 10:23:46 - INFO  - Entered password: ****
2025-07-01 10:23:47 - ERROR - Expected: 'Welcome test_user', Got: 'Invalid credentials'
2025-07-01 10:23:47 - INFO  - test_login_valid FAILED
```

Without logging, all you'd know is "the test failed." With logging, you know the failure was an assertion on the welcome message — and you can immediately investigate whether the credentials changed or the application broke.

---

## 15. Best Practices

- **Use `print()` for learning** — it's perfect for quick checks, beginner scripts, and interactive exploration.
- **Use `logging` for real projects** — any code that will run in a CI/CD pipeline, be shared with a team, or run without human supervision should use the logging module.
- **Configure once** — call `basicConfig()` in one central place (e.g., a `conftest.py` or a `logger_config.py` utility), not in every test file.
- **Don't log sensitive data** — never log passwords, API tokens, or personally identifiable information (PII).
- **Use named loggers** for larger frameworks instead of the root logger, so you can control log levels per module:

```python
import logging

logger = logging.getLogger(__name__)  # logger named after the current module
logger.info("Logger named after this module")
```

- **Add timestamps always** in file logs — they're invaluable for diagnosing timing-related failures.
- **Archive log files per test run** — include a timestamp in the filename so old logs aren't overwritten:

```python
import logging
from datetime import datetime

log_filename = f"logs/test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(filename=log_filename, level=logging.INFO)
```

---

## 16. Logging in QA Framework Usage

In a real QA framework, logging is centralized in a utility module and shared across the entire framework — page objects, test files, and utility functions all use the same configured logger.

### Project Structure

```
qa_framework/
│
├── utils/
│   └── logger.py          # central logging configuration
│
├── pages/
│   └── login_page.py
│
├── tests/
│   └── test_login.py
│
└── logs/
    └── test_run_20250701_102345.log
```

### `utils/logger.py` — Centralized Logger

```python
import logging
from datetime import datetime

def get_logger(name=__name__):
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        # Format
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)

        # File handler — new file per run
        log_filename = f"logs/test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        file_handler = logging.FileHandler(log_filename)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
```

### `pages/login_page.py` — Using the Logger

```python
from utils.logger import get_logger

logger = get_logger(__name__)

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        logger.info(f"Attempting login with username: {username}")
        try:
            self.driver.find_element("id", "username").send_keys(username)
            self.driver.find_element("id", "password").send_keys(password)
            self.driver.find_element("id", "login-btn").click()
            logger.info("Login button clicked successfully")
        except Exception as e:
            logger.error(f"Login action failed: {e}")
            raise
```

### `tests/test_login.py` — Using the Logger in Tests

```python
from pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger(__name__)

def test_valid_login(driver):
    logger.info("test_valid_login — STARTED")
    try:
        login_page = LoginPage(driver)
        login_page.login("test_user", "test_pass")
        assert driver.current_url == "https://example.com/dashboard"
        logger.info("test_valid_login — PASSED")
    except AssertionError as e:
        logger.error(f"test_valid_login — FAILED: {e}")
        raise
    finally:
        driver.quit()
        logger.info("Browser closed")
```

**Sample Log Output:**
```
2025-07-01 10:23:45 - tests.test_login    - INFO  - test_valid_login — STARTED
2025-07-01 10:23:45 - pages.login_page   - INFO  - Attempting login with username: test_user
2025-07-01 10:23:46 - pages.login_page   - INFO  - Login button clicked successfully
2025-07-01 10:23:47 - tests.test_login    - INFO  - test_valid_login — PASSED
2025-07-01 10:23:47 - tests.test_login    - INFO  - Browser closed
```

### Why This Pattern Works in QA
- **One logger config, used everywhere** — change the format or level in one file and it updates across the entire framework.
- **Named loggers (`__name__`)** — each log line shows exactly which file/module it came from, making large suite logs easy to navigate.
- **Dual output** — INFO and above goes to the console (visible during local runs); DEBUG and above goes to the file (full detail for post-run analysis).
- **Timestamped log files** — each test run produces its own log file; nothing ever gets overwritten.
- **Combined with `finally`** (Story 4) — cleanup and closing messages always make it into the log, even when a test crashes.

---

## Summary Table

| Concept | Purpose |
|---|---|
| `logging` module | Python's built-in structured logging system |
| `logging.debug/info/warning/error/critical()` | Log messages at different severity levels |
| Severity order | `DEBUG < INFO < WARNING < ERROR < CRITICAL` |
| `basicConfig(level=...)` | Sets minimum visible log level — one config change filters all output |
| `filename="test.log"` | Redirects log output to a file |
| `format=` | Customizes log output — add severity, timestamps, module name |
| `logging` vs `print()` | Use `print()` for learning; `logging` for all real/production projects |
| Named loggers (`__name__`) | Identify which module produced each log line in large frameworks |
| Centralized logger utility | One config shared across pages, tests, and utilities for consistent logging |
