# Selenium WebDriver — Sprint 5, Story 12 Cheat Sheet
### Topic: Bootstrap Dropdowns | Screenshot Capture | Browser Tabs/Windows | Cookies | Headless Mode

Language: **Python + Selenium WebDriver**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
```

---

## 1. Bootstrap Dropdowns

Bootstrap dropdowns are **not** built on the HTML `<select>` tag — they're `<div>`/`<ul>`/`<li>` based, styled with Bootstrap CSS/JS. Selenium's `Select` class **won't work** on them; you handle them like any clickable element.

### Typical Bootstrap dropdown structure
```html
<div class="dropdown">
  <button class="btn dropdown-toggle" data-toggle="dropdown">Choose</button>
  <ul class="dropdown-menu">
    <li><a href="#">Option 1</a></li>
    <li><a href="#">Option 2</a></li>
  </ul>
</div>
```

### Handling it in Selenium

```python
# Step 1: Click the toggle button to open the dropdown
dropdown_toggle = driver.find_element(By.CLASS_NAME, "dropdown-toggle")
dropdown_toggle.click()

# Step 2: Locate all options and click the desired one
options = driver.find_elements(By.CSS_SELECTOR, ".dropdown-menu li a")
for option in options:
    if option.text == "Option 2":
        option.click()
        break
```

**Key points**
- Always **click to open** first — the options aren't interactable (sometimes not even present in DOM/visible) until the dropdown is expanded.
- Use `CSS_SELECTOR` or `XPATH` with `contains(@class,'dropdown-menu')` to scope to the right menu if there are multiple dropdowns on the page.
- Never use `Select()` here — it throws `UnexpectedTagNameException` since there's no `<select>` tag.

---

## 2. Capture Screenshot

Selenium supports capturing a screenshot of the **whole page/viewport** or a **specific element**.

### a) Full page/viewport screenshot

```python
driver.save_screenshot("screenshot.png")

# Alternative (returns True/False)
driver.get_screenshot_as_file("screenshot.png")

# Get as base64 string (useful for embedding in HTML reports)
base64_img = driver.get_screenshot_as_base64()
```

### b) Screenshot of a specific element

```python
element = driver.find_element(By.ID, "header")
element.screenshot("element_screenshot.png")
```

**Key points**
- `save_screenshot()` / `get_screenshot_as_file()` capture only the **visible viewport**, not the full scrollable page, unless the browser window is resized to fit content.
- Element-level `.screenshot()` is useful for capturing just a specific component (e.g., for visual comparison in reports).
- Commonly used in `try/except` blocks to capture failure evidence:
```python
try:
    driver.find_element(By.ID, "nonexistent").click()
except Exception as e:
    driver.save_screenshot("failure.png")
    print("Error occurred:", e)
```

---

## 3. Browser Tabs and Windows

Covered method names: `window_handles`, `current_window_handle`, `switch_to.window()`.

```python
main_window = driver.current_window_handle

# Open a new tab via JavaScript
driver.execute_script("window.open('https://www.google.com', '_blank');")

all_windows = driver.window_handles
for window in all_windows:
    if window != main_window:
        driver.switch_to.window(window)
        print("New tab title:", driver.title)
        driver.close()               # close the new tab

driver.switch_to.window(main_window)  # switch back to original tab
```

**Key points**
- `current_window_handle` → ID of the **currently active** window/tab.
- `window_handles` → list of **all** open window/tab IDs.
- `switch_to.window(handle)` → moves Selenium's focus to that specific tab.
- `driver.close()` closes only the active tab; `driver.quit()` closes the entire browser session.
- New tabs opened by clicking a link (`target="_blank"`) don't automatically shift Selenium's focus — you must switch manually.

---

## 4. Browser Cookies

Selenium can add, read, and delete cookies for the current domain via `driver.manage()`.

```python
# Add a cookie
driver.add_cookie({"name": "username", "value": "admin"})

# Get a specific cookie
cookie = driver.get_cookie("username")
print(cookie)

# Get all cookies
all_cookies = driver.get_cookies()
for c in all_cookies:
    print(c)

# Delete a specific cookie
driver.delete_cookie("username")

# Delete all cookies
driver.delete_all_cookies()
```

**Key points**
- Cookies are domain-specific — `driver.get(url)` must already be on the target domain before adding/reading cookies for it.
- Common use: injecting a saved session/auth cookie to skip UI login in tests.
- `get_cookies()` returns a list of dicts with keys like `name`, `value`, `domain`, `expiry`, `path`, `secure`.

---

## 5. Headless Mode

Headless mode runs the browser **without a visible UI** — faster and useful for CI/CD pipelines or servers without a display.

```python
chrome_options = Options()
chrome_options.add_argument("--headless=new")   # modern headless mode (Chrome 109+)
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-gpu")     # recommended on some OS/driver combos

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://testautomationpractice.blogspot.com/")
print(driver.title)

driver.quit()
```

**Key points**
- `--headless=new` is the current recommended flag (older `--headless` still works but is the legacy implementation).
- Always set `--window-size` explicitly in headless mode — without a real window, default viewport size can cause elements to be "not visible"/off-screen.
- Screenshots still work in headless mode — useful for debugging CI failures where you can't see the browser live.
- Headless runs are typically faster and use less memory, making them the default for pipelines (Jenkins, GitHub Actions, etc.).

---

## Quick Reference Table

| Topic | Key Method(s) |
|---|---|
| Bootstrap dropdown | Click toggle → `find_elements` on `.dropdown-menu li` → click matching option |
| Screenshot (page) | `driver.save_screenshot("file.png")` |
| Screenshot (element) | `element.screenshot("file.png")` |
| New tab/window | `driver.execute_script("window.open()")`, `window_handles`, `switch_to.window()` |
| Cookies | `add_cookie()`, `get_cookie()`, `get_cookies()`, `delete_cookie()`, `delete_all_cookies()` |
| Headless mode | `Options().add_argument("--headless=new")` |

---

## Assignment / Practice

Practice all the above on:

- 🔗 https://testautomationpractice.blogspot.com/ (has a Bootstrap dropdown to practice; combine with screenshot capture, new tab handling, cookies, and running the whole script in headless mode)
