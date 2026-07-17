# Sprint5 Story7
### Topics: Checkbox | Links (Internal / External / Broken) | Dropdown

Language: **Python + Selenium WebDriver**

---

## 0. Locators Used in This Sheet

| Locator | Example |
|---|---|
| `By.ID` | `driver.find_element(By.ID, "sunday")` |
| `By.NAME` | `driver.find_elements(By.NAME, "weekday")` |
| `By.LINK_TEXT` | `driver.find_element(By.LINK_TEXT, "Home")` |
| `By.TAG_NAME` | `driver.find_elements(By.TAG_NAME, "a")` |
| `By.CSS_SELECTOR` | `driver.find_elements(By.CSS_SELECTOR, ".dropdown-menu li")` |
| `By.XPATH` | `driver.find_element(By.XPATH, "//input[@name='q']")` |

Setup used across examples:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
```

---

## 1. Checkbox Handling in Selenium

Checkboxes map to `<input type="checkbox">`. Selenium treats them as normal `WebElement` objects — there's no separate "Checkbox" class.

**Selenium methods used:**
- `.click()` → toggles the checkbox (checks if unchecked, unchecks if checked)
- `.is_selected()` → returns `True`/`False` for current state
- `.is_enabled()` → is the checkbox interactable
- `.is_displayed()` → is it visible on the page

```python
checkbox = driver.find_element(By.ID, "sunday")

if not checkbox.is_selected():
    checkbox.click()          # check it

print("Selected:", checkbox.is_selected())
print("Enabled:", checkbox.is_enabled())
print("Displayed:", checkbox.is_displayed())

# Handling multiple checkboxes together
checkbox_list = driver.find_elements(By.NAME, "weekday")
for cb in checkbox_list:
    if not cb.is_selected():
        cb.click()
```

**Selenium interview point:**
> `.click()` on a checkbox is a *toggle* action in Selenium — there's no built-in `check()`/`uncheck()` method, so always verify `.is_selected()` first to avoid accidentally flipping the state.

---

## 2. Links in Selenium

All links (`<a>` tags) are handled as `WebElement`s using `By.TAG_NAME`, `By.LINK_TEXT`, or `By.PARTIAL_LINK_TEXT`. The `.get_attribute("href")` method retrieves the target URL.

### a) Internal Link (same domain navigation)

```python
internal_link = driver.find_element(By.LINK_TEXT, "Home")
print("Internal link URL:", internal_link.get_attribute("href"))
internal_link.click()
```

### b) External Link (different domain)

```python
external_link = driver.find_element(By.LINK_TEXT, "Facebook")
ext_url = external_link.get_attribute("href")
print("External link URL:", ext_url)
```

### c) Broken Link Detection

Selenium **cannot** directly tell you if a link is broken — it only locates/clicks elements. Broken-link detection is done by combining Selenium (to collect all `<a>` elements) with Python's `requests` library (to check the HTTP status code).

```python
import requests

links = driver.find_elements(By.TAG_NAME, "a")
print("Total links:", len(links))

for link in links:
    url = link.get_attribute("href")

    if not url:
        print("Skipping - no href")
        continue

    try:
        response = requests.head(url, timeout=5)
        if response.status_code >= 400:
            print(f"{url} -> BROKEN ({response.status_code})")
        else:
            print(f"{url} -> OK ({response.status_code})")
    except Exception as e:
        print(f"{url} -> ERROR: {e}")
```

**Selenium interview point:**
> Selenium only automates the browser — it has no HTTP status API. Broken link validation is a *hybrid approach*: Selenium finds the elements, the `requests` library validates the response code (≥ 400 = broken).

---

## 3. Dropdown Handling in Selenium

### a) Select Class (for `<select>` tags only)

Selenium provides a dedicated `Select` class (`selenium.webdriver.support.ui.Select`) specifically for HTML `<select>` dropdowns.

```python
from selenium.webdriver.support.ui import Select

dropdown_el = driver.find_element(By.ID, "dropdown-class-example")
select = Select(dropdown_el)

select.select_by_visible_text("Option 2")   # by visible text
select.select_by_index(1)                   # by index (0-based)
select.select_by_value("option2")            # by value attribute

# Get all options
options = select.options
for opt in options:
    print(opt.text)

print("Is multi-select:", select.is_multiple)
print("Currently selected:", select.first_selected_option.text)

select.deselect_all()  # only valid for multi-select dropdowns
```

### b) Non-Select (Custom/Bootstrap) Dropdown

If the dropdown is built with `<div>`/`<ul>`/`<li>` (no `<select>` tag), the `Select` class **will throw**:
`UnexpectedTagNameException: Select only works on <select> elements, not on <div>`.
Handle these with normal element interactions:

```python
custom_dropdown = driver.find_element(By.ID, "custom-dropdown")
custom_dropdown.click()  # opens dropdown

custom_options = driver.find_elements(By.CSS_SELECTOR, ".dropdown-menu li")
for opt in custom_options:
    if opt.text == "Desired Option":
        opt.click()
        break
```

**Selenium interview point:**
> Always confirm the tag is `<select>` before using the `Select` class. If it's a JavaScript-rendered dropdown, treat it like any other clickable `WebElement`, often paired with `WebDriverWait` for visibility.

---

## Assignment (Selenium Practice)

Practice checkbox, link, and dropdown handling on:

- 🔗 https://testautomationpractice.blogspot.com/
- 🔗 https://itera-qa.azurewebsites.net/home/automation

### Dynamic XPath Practice

Write **dynamic XPath** (using `contains()`, `starts-with()`, `text()`, or axes) instead of static/absolute XPath, since attributes on search engines can change per session:

**Google Search**
```
//textarea[contains(@name,'q')]
//input[contains(@name,'btnK')]
```

**Bing Search**
```
//input[contains(@id,'sb_form_q')]
//input[contains(@id,'search_icon')]
```

**Selenium interview point:**
> Dynamic XPath is preferred over absolute XPath because it's resilient to minor DOM/attribute changes — using `contains()`/`starts-with()` on stable partial attribute values keeps locators from breaking across builds.
