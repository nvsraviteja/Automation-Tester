# Sprint 5 — Story 1: Selenium WebDriver Cheatsheet

---

## What is WebDriver?

| Topic | Summary |
|---|---|
| WebDriver | A component and module inside the `selenium` package |
| Purpose | Controls browsers programmatically |
| Type | API (Application Programming Interface) |

### Browser → Driver Mapping
| Browser | WebDriver Class |
|---|---|
| Chrome | `Chrome()` |
| Firefox | `Firefox()` |
| Edge | `Edge()` |

---

## Architecture

### Selenium 3
```
Selenium Language Bindings → JSON Wire Protocol → Browser Driver → (W3C) → Browser
```

### Selenium 4
```
Selenium Language Bindings → W3C → Browser Driver → W3C → Browser
```

> Selenium 4 removed the JSON Wire Protocol — communicates directly using W3C standard.

---

## Setup & Configuration

### Step 1 — Download Browser Drivers
| Browser | Download Link |
|---|---|
| Chrome | https://chromedriver.chromium.org/downloads |
| Edge | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ |
| Firefox | https://github.com/mozilla/geckodriver/releases |

> Download → Extract `.zip` → Get the `.exe` driver file

### Step 2 — Install Selenium

```bash
# Approach 1 — via pip (recommended)
pip install selenium

# Specific version
pip install selenium==4.0.0

# Approach 2 — via PyCharm
# Settings → Project → Python Interpreter → + → search "selenium" → Install
```

---

## First Test Case

### Scenario
```
1. Open Chrome browser
2. Navigate to https://opensource-demo.orangehrmlive.com/
3. Enter username: Admin
4. Enter password: admin123
5. Click Login
6. Get the page title (Actual)
7. Verify title == "OrangeHRM" (Expected)
8. Close the browser
```

### Code
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1 — Open browser
driver = webdriver.Chrome()

# Step 2 — Open URL
driver.get("https://opensource-demo.orangehrmlive.com/")

# Step 3 — Enter username
driver.find_element(By.NAME, "username").send_keys("Admin")

# Step 4 — Enter password
driver.find_element(By.NAME, "password").send_keys("admin123")

# Step 5 — Click login
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Step 6 — Capture actual title
actual_title = driver.title
print("Actual Title:", actual_title)

# Step 7 — Verify title
expected_title = "OrangeHRM"
assert actual_title == expected_title, f"Expected '{expected_title}', got '{actual_title}'"

# Step 8 — Close browser
driver.quit()
```

---

## Key WebDriver Methods

| Method | Purpose |
|---|---|
| `webdriver.Chrome()` | Launch Chrome browser |
| `driver.get(url)` | Navigate to a URL |
| `driver.title` | Get the page title |
| `driver.current_url` | Get the current URL |
| `driver.find_element(By, value)` | Find a single element |
| `element.send_keys("text")` | Type into a field |
| `element.click()` | Click an element |
| `driver.quit()` | Close browser + end session |
| `driver.close()` | Close current tab only |

---

## Locator Strategies (`By`)

```python
from selenium.webdriver.common.by import By
```

| Locator | Example |
|---|---|
| `By.ID` | `driver.find_element(By.ID, "username")` |
| `By.NAME` | `driver.find_element(By.NAME, "username")` |
| `By.CLASS_NAME` | `driver.find_element(By.CLASS_NAME, "btn-login")` |
| `By.XPATH` | `driver.find_element(By.XPATH, "//button[@type='submit']")` |
| `By.CSS_SELECTOR` | `driver.find_element(By.CSS_SELECTOR, "input#username")` |
| `By.LINK_TEXT` | `driver.find_element(By.LINK_TEXT, "Forgot Password?")` |

---

## `driver.quit()` vs `driver.close()`

| | `quit()` | `close()` |
|---|---|---|
| Closes | All browser windows + ends WebDriver session | Current tab only |
| Use when | End of test | Closing a specific tab mid-test |

---

## Quick Reference — Import & Launch

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()    # or Firefox() or Edge()
driver.get("https://example.com")
driver.quit()
```
