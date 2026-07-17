# Selenium WebDriver — Day 18 Cheat Sheet
### Topics: Alerts/Popups | Authentication Popup | Frames/Iframes | Browser Windows

Language: **Python + Selenium WebDriver**

---

## 1. Alerts / Popups

JavaScript alerts (`alert()`, `confirm()`, `prompt()`) are **not** normal DOM elements — they can't be located with `find_element`. Selenium handles them via `switch_to.alert`.

```python
my_alert = driver.switch_to.alert

print(my_alert.text)     # read alert message
my_alert.accept()        # click OK
# my_alert.dismiss()     # click Cancel

# For prompt() alerts that accept text input:
# my_alert.send_keys("some text")
# my_alert.accept()
```

**Key points**
- `switch_to.alert` gives you a handle to the currently open alert.
- `.text` → reads the alert's message.
- `.accept()` → clicks OK / Yes.
- `.dismiss()` → clicks Cancel / No.
- `.send_keys()` → types into a `prompt()` alert's input box (only works for prompt-type alerts).
- If no alert is present when you call `switch_to.alert`, Selenium throws `NoAlertPresentException`.

---

## 2. Authentication Popup

Browser-native basic-auth popups (username/password dialog) also **cannot** be handled with `find_element` or `switch_to.alert`. The common workaround is to embed credentials directly in the URL.

**Syntax:**
```
http://username:password@domain.com
```

**Example:**
```python
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
```

Practice site: http://the-internet.herokuapp.com/basic_auth

**Key points**
- This bypasses the OS-level auth dialog entirely by passing credentials in the URL itself.
- Only works for **Basic Authentication** popups (not custom login forms, and not NTLM auth in all browsers).
- Some browsers/versions may still show a security warning — this method works reliably on Chrome for basic auth.

---

## 3. Frames / Iframes

A frame/iframe embeds another HTML document inside the current page. Elements inside a frame are **not accessible** until you switch context into that frame.

```python
# Selenium 3 (older, deprecated)
# driver.switch_to_frame("frame_name")

# Selenium 4 (current syntax)
driver.switch_to.frame("frame_name")     # by name attribute
driver.switch_to.frame("frame_id")       # by id attribute
driver.switch_to.frame(0)                # by index (0 = first frame on page)

frame_element = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(frame_element)    # by WebElement

# Come back out to the main page
driver.switch_to.default_content()
```

**Key points**
- `<frame>` and `<iframe>` — `<iframe>` is the modern HTML5 standard, `<frame>` is legacy (used inside a `<frameset>`, not inside a normal `<body>`).
- A page can have a `<form>` inside a frame, and frames can be **nested (inner frames)** — you must switch into the outer frame first, then into the inner one.
- `switch_to.default_content()` → exits **all** frames and returns to the main page.
- `switch_to.parent_frame()` → exits only **one level up** (useful with nested/inner frames), unlike `default_content()` which jumps straight to the top-level document.
- Trying to `find_element` on something inside a frame *without switching* raises `NoSuchElementException`, even though the element is visible on screen.

---

## 4. Browser Windows / Tabs

When a new tab/window opens (e.g., clicking a link with `target="_blank"`), Selenium's `driver` stays focused on the **original** window until you explicitly switch.

```python
main_window = driver.current_window_handle   # ID of the current single window

# Click something that opens a new window/tab
# driver.find_element(By.LINK_TEXT, "open new tab").click()

all_windows = driver.window_handles           # list of ALL open window IDs

for window in all_windows:
    if window != main_window:
        driver.switch_to.window(window)      # switch to the new window
        print(driver.title)
        # do actions on the new window
        driver.close()                        # close this window

driver.switch_to.window(main_window)          # go back to original window
```

**Key points**
- `current_window_handle` → returns the ID of the **single** window currently in focus.
- `window_handles` → returns a **list** of IDs for **all** open windows/tabs.
- `switch_to.window(id)` → moves Selenium's control to a specific window.
- `driver.close()` closes only the currently focused window; `driver.quit()` closes the entire browser (all windows) and ends the session.
- Always switch back to the correct handle before continuing, especially after closing a popped-up window.

---

## Assignment (Selenium Practice)

Practice alerts, authentication popup, frames, and window handling on:

- 🔗 https://testautomationpractice.blogspot.com/
