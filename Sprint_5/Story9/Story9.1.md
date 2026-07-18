# Selenium WebDriver — Sprint 5, Story 9.1 Cheat Sheet
### Topic: Date Picker (Standard & Non-Standard/Customized)

Language: **Python + Selenium WebDriver**

---

## 0. What is a Date Picker?

A date picker is a UI widget for selecting dates. In Selenium there's no dedicated "DatePicker" class — you handle it either by:
1. Directly sending text to an `<input>` field (if allowed), or
2. Interacting with the calendar UI (clicking day/month/year controls) when direct typing isn't supported.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
```

---

## 1. Standard Date Picker

A **standard** date picker is usually a native HTML5 `<input type="date">` element, or a simple widget where you can directly type/send the date value. Browser renders its own default calendar icon/control.

### a) Native HTML5 `<input type="date">`

```python
date_field = driver.find_element(By.ID, "datepicker")

# Format required: yyyy-MM-dd (HTML5 date input standard)
date_field.send_keys("2026-07-18")
```

### b) Using JavaScript Executor (bypasses native picker UI restrictions)

```python
date_field = driver.find_element(By.ID, "datepicker")
driver.execute_script("arguments[0].value = '2026-07-18';", date_field)
```

### c) Standard jQuery UI datepicker (click-based)

Many "standard" jQuery datepickers open a calendar on click, but let you type directly too:

```python
date_field = driver.find_element(By.ID, "datepicker")
date_field.click()
date_field.clear()
date_field.send_keys("07/18/2026")
```

**Key points**
- Always check the **expected date format** (`yyyy-MM-dd`, `MM/dd/yyyy`, etc.) — sending the wrong format silently fails or throws.
- `send_keys()` works only if the field isn't `readonly`. If it's read-only, you must click through the calendar UI instead (see Non-Standard section) or use `execute_script()`.

---

## 2. Non-Standard (Customized) Date Picker

A **non-standard/customized** date picker is a JS-built widget (e.g., jQuery UI, React calendar, Bootstrap datepicker) where the input is `readonly` — direct typing isn't allowed. You must **click through month navigation and day cells**.

### Example: jQuery UI style calendar

```python
# Click to open the calendar
date_input = driver.find_element(By.ID, "datepicker")
date_input.click()

# Select Month from dropdown (jQuery UI renders month/year as <select>)
month_dropdown = Select(driver.find_element(By.CLASS_NAME, "ui-datepicker-month"))
month_dropdown.select_by_visible_text("July")

# Select Year from dropdown
year_dropdown = Select(driver.find_element(By.CLASS_NAME, "ui-datepicker-year"))
year_dropdown.select_by_visible_text("2026")

# Click the specific day (usually rendered as <a> inside <td>)
days = driver.find_elements(By.XPATH, "//a[@class='ui-state-default']")
for day in days:
    if day.text == "18":
        day.click()
        break
```

### Example: Navigating month-by-month using "Next" arrow (no year dropdown)

```python
target_month = "July"
target_year = "2026"

while True:
    header = driver.find_element(By.CLASS_NAME, "ui-datepicker-title").text
    if target_month in header and target_year in header:
        break
    driver.find_element(By.CLASS_NAME, "ui-datepicker-next").click()
    time.sleep(0.3)  # small wait for calendar re-render; prefer WebDriverWait in real scripts

# Now click the day
days = driver.find_elements(By.XPATH, "//a[@class='ui-state-default']")
for day in days:
    if day.text == "18":
        day.click()
        break
```

### Example: Handling calendar with month/year as plain text (not a `<select>`)

```python
# Some custom widgets show "July 2026" as a header with Next/Prev arrows only
next_btn = driver.find_element(By.CLASS_NAME, "next")
prev_btn = driver.find_element(By.CLASS_NAME, "prev")

while "July 2026" not in driver.find_element(By.CLASS_NAME, "calendar-header").text:
    next_btn.click()

driver.find_element(By.XPATH, "//td[text()='18']").click()
```

**Key points**
- Inspect the DOM first: is month/year a `<select>` (use `Select` class) or plain text with Next/Prev arrows (loop-click until target month/year is reached)?
- Day cells are usually `<a>` or `<td>` — locate by exact visible text (`"18"`), but watch out for matching disabled/greyed-out dates from adjacent months.
- Prefer `WebDriverWait` with `expected_conditions` (e.g., `element_to_be_clickable`) over `time.sleep()` for calendar re-renders after clicking Next/Prev.
- If direct `send_keys()` throws `ElementNotInteractableException`, that's usually the signal the field is `readonly` → switch to the click-through approach.

---

## Standard vs Non-Standard — Quick Comparison

| Aspect | Standard | Non-Standard (Customized) |
|---|---|---|
| Input field | Editable, accepts `send_keys()` | Usually `readonly` |
| Interaction | Type the date directly | Click through calendar UI |
| Month/Year selection | N/A or simple | `<select>` dropdown OR Next/Prev click loop |
| Day selection | N/A (typed) | Click matching `<a>`/`<td>` element |
| Common tech | HTML5 `<input type="date">` | jQuery UI, Bootstrap Datepicker, React calendars |

---

## Assignment / Practice

Practice both standard and non-standard date pickers on:

- 🔗 https://testautomationpractice.blogspot.com/ (has a datepicker section — try typing the date directly first, then try disabling that and clicking through the calendar UI)
