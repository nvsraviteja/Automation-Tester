# Sprint 5 — Story 4.2: WebDriver Commands Cheatsheet

---

## 1. Application Commands

| Command | Purpose | Example |
|---|---|---|
| `driver.get(url)` | Open a URL in the browser | `driver.get("https://example.com")` |
| `driver.title` | Get the title of the current page | `print(driver.title)` |
| `driver.current_url` | Get the current page URL | `print(driver.current_url)` |
| `driver.page_source` | Get full HTML source of the page | `print(driver.page_source)` |

```python
driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.title)        # OrangeHRM
print(driver.current_url)  # https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
print(driver.page_source)  # full HTML of the page
```

---

## 2. Conditional Commands

Used to check the **state** of an element before interacting with it.

| Command | Returns | Checks |
|---|---|---|
| `element.is_displayed()` | `True` / `False` | Is the element visible on the page? |
| `element.is_enabled()` | `True` / `False` | Is the element interactable (not disabled)? |
| `element.is_selected()` | `True` / `False` | Is a checkbox / radio button selected? |

```python
username_field = driver.find_element(By.ID, "username")

print(username_field.is_displayed())   # True — visible on page
print(username_field.is_enabled())     # True — not disabled
print(username_field.is_selected())    # False — not a checkbox/radio
```

### When to Use Each
| Command | Use case |
|---|---|
| `is_displayed()` | Verify an error message appeared / a section is visible |
| `is_enabled()` | Verify a button is clickable before clicking |
| `is_selected()` | Verify a checkbox is checked or a radio is selected |

---

## 3. Browser Commands

| Command | Purpose |
|---|---|
| `driver.close()` | Close the **current tab** only (driver stays active) |
| `driver.quit()` | Close **all browser windows** and kill the WebDriver process |

```python
driver.close()   # closes current tab — use mid-test when handling multiple tabs
driver.quit()    # closes everything — use at end of test in teardown / finally block
```

### `close()` vs `quit()`
| | `close()` | `quit()` |
|---|---|---|
| Closes | Current tab only | All tabs + all windows |
| Ends session? | No | Yes |
| Use when | Managing multiple tabs | End of test cleanup |

---

## 4. Navigational Commands

| Command | Purpose |
|---|---|
| `driver.back()` | Go to the previous page (browser back button) |
| `driver.forward()` | Go to the next page (browser forward button) |
| `driver.refresh()` | Reload the current page |

```python
driver.get("https://example.com/page1")
driver.get("https://example.com/page2")

driver.back()     # goes back to page1
driver.forward()  # goes forward to page2
driver.refresh()  # reloads page2
```

---

## 5. Wait Commands

| Type | Method | When to use |
|---|---|---|
| Implicit wait | `driver.implicitly_wait(seconds)` | Set once — applies to all `find_element` calls |
| Explicit wait | `WebDriverWait(driver, timeout).until(condition)` | Wait for a specific condition on a specific element |
| Forced wait | `time.sleep(seconds)` | Fixed pause — avoid in production tests |

```python
# Implicit wait — set once globally
driver.implicitly_wait(10)   # waits up to 10 seconds for elements to appear

# Explicit wait — wait for a specific element condition
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.ID, "username")))

# Forced wait — use only when necessary
import time
time.sleep(2)
```

---

## 6. `find_element` vs `find_elements`

| | `find_element` | `find_elements` |
|---|---|---|
| Returns | Single `WebElement` | `List` of `WebElement` |
| If not found | Raises `NoSuchElementException` | Returns empty list `[]` |
| Use when | Expecting one match | Expecting multiple matches |

```python
# Single element
driver.find_element(By.ID, "username")

# All matching elements
driver.find_elements(By.TAG_NAME, "input")
```

---

## 7. `.text` vs `.get_attribute('value')`

### Key Difference
| | `.text` | `.get_attribute('value')` |
|---|---|---|
| Returns | Inner text (visible text between tags) | Value of any HTML attribute |
| Use for | Labels, headings, paragraphs, error messages | Input field values, placeholders, href, type |

### Example HTML
```html
<input id="123" name="xyz" value="admin@example.com" placeholder="Email" />
<p id="msg">Login Successful</p>
```

```python
# .text — gets visible text between opening and closing tags
message = driver.find_element(By.ID, "msg")
print(message.text)   # Login Successful

# .get_attribute() — gets an HTML attribute value
input_field = driver.find_element(By.ID, "123")
print(input_field.get_attribute("value"))        # admin@example.com
print(input_field.get_attribute("placeholder"))  # Email
print(input_field.get_attribute("name"))         # xyz
```

### When to Use Each
| Scenario | Use |
|---|---|
| Get visible text of a label / paragraph / error | `.text` |
| Get what's typed inside an input field | `.get_attribute("value")` |
| Get placeholder text | `.get_attribute("placeholder")` |
| Get href of a link | `.get_attribute("href")` |
| Get type of an input | `.get_attribute("type")` |

---

## Quick Reference

```python
# Application
driver.get(url)
driver.title
driver.current_url
driver.page_source

# Conditional
element.is_displayed()
element.is_enabled()
element.is_selected()

# Browser
driver.close()   # current tab
driver.quit()    # all tabs + end session

# Navigation
driver.back()
driver.forward()
driver.refresh()

# Text
element.text                          # inner visible text
element.get_attribute("value")        # input field content
element.get_attribute("placeholder")  # placeholder text
element.get_attribute("href")         # link URL
```
