# Sprint 5 — Story 4: `find_element` vs `find_elements` Cheatsheet

---

## Core Difference

| | `find_element` | `find_elements` |
|---|---|---|
| Returns | Single `WebElement` | `List` of `WebElement` objects |
| Match count | First matching element only | All matching elements |
| If nothing found | Raises `NoSuchElementException` | Returns empty list `[]` |
| Use when | You expect exactly one match | You expect multiple matches |

---

## `find_element` — Single Element

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

# Returns the FIRST matching element
element = driver.find_element(By.ID, "username")
element.send_keys("Admin")
```

- Stops searching after the **first match**
- Throws `NoSuchElementException` if no match is found

---

## `find_elements` — Multiple Elements

```python
# Returns a LIST of all matching elements
elements = driver.find_elements(By.TAG_NAME, "input")

print(len(elements))   # number of input fields on the page

for element in elements:
    print(element.get_attribute("type"))
```

- Returns **all** matching elements as a list
- Returns **empty list `[]`** if nothing found — no exception

---

## Practical Examples

### Count items in a list
```python
items = driver.find_elements(By.CLASS_NAME, "menu-item")
print(f"Total menu items: {len(items)}")
```

### Check if an element exists (without crashing)
```python
results = driver.find_elements(By.ID, "error-message")
if len(results) == 0:
    print("No error message — test passed")
else:
    print(f"Error found: {results[0].text}")
```

### Click the Nth element in a list
```python
rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
rows[2].click()   # click the 3rd row (index starts at 0)
```

### Get text from all elements
```python
links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print(link.text)
```

---

## What Happens When Nothing is Found

```python
# find_element — CRASHES with exception
driver.find_element(By.ID, "nonexistent")
# NoSuchElementException: no such element: Unable to locate element

# find_elements — returns empty list, NO crash
result = driver.find_elements(By.ID, "nonexistent")
print(result)   # []
```

> Use `find_elements` when you're not sure if the element exists — safer for conditional checks.

---

## Summary

```
One element expected   → find_element()   → returns WebElement
Many elements expected → find_elements()  → returns List[WebElement]
Checking existence     → find_elements()  → check if list is empty
```

| Scenario | Method to use |
|---|---|
| Login button (unique) | `find_element` |
| All rows in a table | `find_elements` |
| All input fields on a form | `find_elements` |
| Check if error message appears | `find_elements` + check `len()` |
| First link on the page | `find_element` |
| Click the 3rd item in a menu | `find_elements` + index `[2]` |
