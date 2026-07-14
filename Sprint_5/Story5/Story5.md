# Sprint 5 — Story 5: Wait Commands Cheatsheet

---

## Why Waits Are Needed

Web pages load dynamically — elements may not be immediately available when a script runs.
Without waits, Selenium tries to interact with elements that don't exist yet → `NoSuchElementException`.

```
Page loads → Script runs → Element not ready yet → CRASH ❌
Page loads → Script waits → Element appears → Interaction ✅
```

---

## 3 Types of Waits

| Type | Method | Scope | Best for |
|---|---|---|---|
| Implicit Wait | `driver.implicitly_wait(seconds)` | All elements, globally | General fallback wait |
| Explicit Wait | `WebDriverWait(driver, timeout).until(condition)` | One specific element + condition | Precise, reliable waits |
| Python Pause | `time.sleep(seconds)` | Everything — fixed pause | Debugging only |

---

## 1. Implicit Wait

Set **once** — applies automatically to every `find_element` call for the rest of the session.
Selenium will keep retrying to find the element until the timeout is reached.

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)   # waits up to 10 seconds for any element

driver.get("https://example.com")
driver.find_element(By.ID, "username")   # will wait up to 10s if not immediately found
```

### Key Points
| Point | Detail |
|---|---|
| Set once | Only needs to be called once after launching the browser |
| Global | Applies to ALL `find_element` / `find_elements` calls |
| Polling | Keeps retrying until element found or timeout reached |
| On timeout | Raises `NoSuchElementException` |
| Does NOT wait for | Visibility, clickability, or specific states — only presence in DOM |

---

## 2. Explicit Wait

Waits for a **specific condition** on a **specific element** before proceeding.
More precise and reliable than implicit wait.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

wait = WebDriverWait(driver, 10)   # max wait = 10 seconds

# Wait until element is visible
element = wait.until(EC.visibility_of_element_located((By.ID, "username")))
element.send_keys("Admin")
```

### Common Expected Conditions (`EC`)

| Condition | Use when |
|---|---|
| `EC.visibility_of_element_located(locator)` | Element must be visible on screen |
| `EC.presence_of_element_located(locator)` | Element exists in DOM (may not be visible) |
| `EC.element_to_be_clickable(locator)` | Element is visible AND enabled |
| `EC.text_to_be_present_in_element(locator, text)` | Element contains specific text |
| `EC.invisibility_of_element_located(locator)` | Element is hidden / removed |
| `EC.title_is("text")` | Page title matches exactly |
| `EC.url_contains("text")` | URL contains expected string |
| `EC.alert_is_present()` | A browser alert has appeared |

### Examples

```python
wait = WebDriverWait(driver, 10)

# Wait for element to be clickable before clicking
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_btn.click()

# Wait for success message to appear
message = wait.until(EC.visibility_of_element_located((By.ID, "success-msg")))
print(message.text)

# Wait for URL to change after login
wait.until(EC.url_contains("/dashboard"))

# Wait for loading spinner to disappear
wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading-spinner")))
```

---

## 3. Python Pause (`time.sleep`)

Forces the script to **stop completely** for a fixed number of seconds — regardless of whether the element is ready or not.

```python
import time

time.sleep(2)   # pauses for exactly 2 seconds
```

### ⚠️ When to Use / Avoid

| | Detail |
|---|---|
| ✅ Use for | Debugging — temporarily slow down a script to see what's happening |
| ❌ Avoid in | Real test suites — wastes time even when the element is already ready |
| ❌ Problem | If page takes 3s but sleep is 2s → test still fails |
| ❌ Problem | If page takes 0.5s but sleep is 3s → wastes 2.5s every test |

---

## Comparison

| | Implicit | Explicit | `time.sleep` |
|---|---|---|---|
| Scope | All elements globally | One element + one condition | Everything (fixed) |
| Condition-aware | No — waits for DOM presence only | Yes — waits for specific state | No |
| Flexible | Moderate | High | None |
| Reliable | Moderate | Best | Least |
| Use in production | As fallback | ✅ Preferred | ❌ Avoid |
| Timeout behaviour | `NoSuchElementException` | `TimeoutException` | No exception |

---

## Mixing Implicit + Explicit (Be Careful)

Mixing both can cause unpredictable timing behaviour.
**Best practice:** Use explicit waits throughout — set implicit wait only as a low-level fallback.

```python
driver.implicitly_wait(3)                        # low fallback
wait = WebDriverWait(driver, 10)                 # explicit for critical elements
element = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
```

---

## Full Example — Using Explicit Wait in a Login Test

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

wait = WebDriverWait(driver, 10)

# Wait for username field before typing
username = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
username.send_keys("Admin")

# Wait for password field
password = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
password.send_keys("admin123")

# Wait for login button to be clickable before clicking
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_btn.click()

# Wait for dashboard to load
wait.until(EC.url_contains("/dashboard"))
print("Login successful:", driver.current_url)

driver.quit()
```

---

## Quick Reference

```python
# Implicit — set once after launching browser
driver.implicitly_wait(10)

# Explicit — wait for specific condition
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.ID, "element_id")))
wait.until(EC.element_to_be_clickable((By.ID, "button_id")))
wait.until(EC.url_contains("/dashboard"))

# Python pause — debugging only
import time
time.sleep(2)
```
