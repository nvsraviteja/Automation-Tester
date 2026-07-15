# Sprint 5 — Story 6: WebElements Cheatsheet

---

## What is a WebElement?

A `WebElement` is the object Selenium returns when it finds an HTML element on a page.
Every interaction (click, type, read, check) is performed through a `WebElement`.

```python
element = driver.find_element(By.ID, "username")   # returns a WebElement
element.send_keys("Admin")                          # interact with it
```

---

## WebElement Interactions

### Input / Text Fields

| Method | Purpose |
|---|---|
| `send_keys("text")` | Type text into a field |
| `clear()` | Clear existing text from a field |
| `send_keys(Keys.RETURN)` | Press Enter key |
| `send_keys(Keys.TAB)` | Press Tab key |
| `send_keys(Keys.BACKSPACE)` | Press Backspace |

```python
from selenium.webdriver.common.keys import Keys

field = driver.find_element(By.ID, "username")
field.clear()
field.send_keys("Admin")
field.send_keys(Keys.RETURN)   # submit with Enter
```

---

### Buttons & Clickable Elements

| Method | Purpose |
|---|---|
| `click()` | Click the element |

```python
btn = driver.find_element(By.XPATH, "//button[@type='submit']")
btn.click()
```

---

### Reading Element Data

| Method / Property | Returns | Use for |
|---|---|---|
| `.text` | Inner visible text | Labels, headings, paragraphs, error messages |
| `.get_attribute("value")` | Input field content | What is typed into a field |
| `.get_attribute("href")` | Link URL | Anchor tag URLs |
| `.get_attribute("placeholder")` | Placeholder text | Form field hints |
| `.get_attribute("type")` | Input type | `text`, `password`, `checkbox` |
| `.get_attribute("class")` | Class attribute value | CSS class names |
| `.get_attribute("id")` | ID attribute value | Element ID |

```python
# Visible text
msg = driver.find_element(By.ID, "error-msg")
print(msg.text)   # "Invalid credentials"

# Input field value
field = driver.find_element(By.NAME, "username")
print(field.get_attribute("value"))         # "Admin"
print(field.get_attribute("placeholder"))   # "Username"
```

---

### Checking Element State

| Method | Returns | Checks |
|---|---|---|
| `is_displayed()` | `True` / `False` | Is the element visible on screen? |
| `is_enabled()` | `True` / `False` | Is the element interactable (not disabled)? |
| `is_selected()` | `True` / `False` | Is checkbox / radio selected? |

```python
submit_btn = driver.find_element(By.ID, "loginBtn")

print(submit_btn.is_displayed())   # True
print(submit_btn.is_enabled())     # True

checkbox = driver.find_element(By.ID, "rememberMe")
print(checkbox.is_selected())      # False
```

---

## Dropdown — `Select`

```python
from selenium.webdriver.support.ui import Select

dropdown = Select(driver.find_element(By.ID, "country"))

dropdown.select_by_visible_text("India")   # select by text
dropdown.select_by_value("IN")             # select by value attribute
dropdown.select_by_index(2)               # select by position (0-based)

print(dropdown.first_selected_option.text)   # currently selected option
```

---

## Checkbox & Radio Button

```python
checkbox = driver.find_element(By.ID, "rememberMe")

# Check if already selected before clicking
if not checkbox.is_selected():
    checkbox.click()   # check it

# Uncheck
if checkbox.is_selected():
    checkbox.click()   # uncheck it
```

---

## Common WebElement Types & How to Handle Them

| Element | HTML Tag | How to interact |
|---|---|---|
| Text input | `<input type="text">` | `send_keys()`, `clear()` |
| Password field | `<input type="password">` | `send_keys()` |
| Button | `<button>` | `click()` |
| Link | `<a>` | `click()` or `.get_attribute("href")` |
| Checkbox | `<input type="checkbox">` | `click()`, `is_selected()` |
| Radio button | `<input type="radio">` | `click()`, `is_selected()` |
| Dropdown | `<select>` | Use `Select` class |
| Text area | `<textarea>` | `send_keys()`, `clear()` |
| Label / heading | `<label>`, `<h1>` | `.text` |
| Image | `<img>` | `.get_attribute("src")` |

---

## Getting Element Location & Size

```python
element = driver.find_element(By.ID, "username")

print(element.location)   # {'x': 300, 'y': 150}  — position on page
print(element.size)       # {'height': 40, 'width': 200}  — dimensions
```

---

## Summary — Most Used Methods

```python
element.click()                        # click
element.send_keys("text")             # type
element.clear()                        # clear field
element.text                           # get visible text
element.get_attribute("value")        # get attribute value
element.is_displayed()                 # visible?
element.is_enabled()                   # enabled?
element.is_selected()                  # selected? (checkbox/radio)
element.location                       # x, y position
element.size                           # height, width
```
