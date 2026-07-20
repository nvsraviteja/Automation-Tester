# Selenium WebDriver — Sprint 5, Story 11 Cheat Sheet
### Topic: Keyboard Actions | Download File | Upload File

Language: **Python + Selenium WebDriver**

---

## 1. Keyboard Actions

Keyboard interactions are handled via `send_keys()` on an element (simple key presses/text) or `ActionChains` + `Keys` class (key combinations, modifier keys, holding keys).

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

actions = ActionChains(driver)
```

### a) Simple key press using `send_keys()`

```python
search_box = driver.find_element(By.ID, "search")
search_box.send_keys("Selenium")
search_box.send_keys(Keys.ENTER)          # press Enter
search_box.send_keys(Keys.TAB)            # press Tab
```

### b) Key combinations using `ActionChains`

```python
element = driver.find_element(By.ID, "textbox")

# Ctrl + A (select all)
actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

# Ctrl + C (copy)
actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

# Ctrl + V (paste)
actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
```

### c) Common `Keys` constants

```python
Keys.ENTER
Keys.TAB
Keys.ESCAPE
Keys.SPACE
Keys.BACKSPACE
Keys.DELETE
Keys.ARROW_DOWN / Keys.ARROW_UP / Keys.ARROW_LEFT / Keys.ARROW_RIGHT
Keys.SHIFT
Keys.CONTROL
Keys.ALT
Keys.F5
```

**Key points**
- `send_keys()` on a `WebElement` → simplest way to type text or send a single special key.
- `ActionChains.key_down()` / `.key_up()` → needed for **modifier key combos** (Ctrl, Shift, Alt) since `send_keys()` alone can't hold a key while pressing another.
- Always call `.perform()` to actually execute a queued `ActionChains` sequence.

---

## 2. File Download

Selenium itself doesn't have a built-in "download" method — clicking a download link triggers the **browser's** native download behavior, which Selenium doesn't directly control. The common approach: configure Chrome options to auto-download files to a known folder, then verify the file exists using Python's `os` module.

### a) Configure Chrome to auto-download without a save-as prompt

```python
from selenium.webdriver.chrome.options import Options
import os

download_dir = os.path.join(os.getcwd(), "downloads")
os.makedirs(download_dir, exist_ok=True)

chrome_options = Options()
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://testautomationpractice.blogspot.com/")
```

### b) Trigger download and verify file

```python
import time

download_link = driver.find_element(By.LINK_TEXT, "Download File")
download_link.click()

time.sleep(3)  # wait for download to complete; prefer polling over a fixed sleep

expected_file = os.path.join(download_dir, "filename.pdf")
if os.path.exists(expected_file):
    print("File downloaded successfully!")
else:
    print("File not found - download failed")
```

**Key points**
- The download path/behavior is configured through **Chrome options**, not Selenium's API directly.
- Verification happens outside Selenium — using Python's `os.path.exists()` to check the downloads folder.
- Better than a fixed `time.sleep()`: poll in a loop checking for the file's existence up to a timeout, since download time varies.

---

## 3. File Upload

Most file upload fields are `<input type="file">`, which Selenium can handle directly with `send_keys()` — passing the **absolute file path** as if typing it into the OS file-picker.

```python
upload_element = driver.find_element(By.ID, "uploadfile")
upload_element.send_keys("/full/path/to/your/file.txt")
```

**Key points**
- No need to click and interact with the native OS "Choose File" dialog — Selenium bypasses it entirely by sending the path directly to the `<input type="file">` element.
- The path must be an **absolute path** (not relative), and must exist on the machine running the browser.
- This only works if the upload field is a real `<input type="file">` in the DOM. If the site uses a **custom JS upload widget** that hides the real input, you may need to locate the hidden input directly (often with `display:none`, still reachable via `send_keys()`).
- For multiple file uploads (if the input supports `multiple`), separate paths with `\n`:
```python
upload_element.send_keys("/path/file1.txt\n/path/file2.txt")
```

---

## Quick Reference Table

| Action | Method |
|---|---|
| Type text | `element.send_keys("text")` |
| Press Enter/Tab/Escape | `element.send_keys(Keys.ENTER)` |
| Key combo (Ctrl+A, etc.) | `ActionChains.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()` |
| Configure download folder | `chrome_options` with `prefs["download.default_directory"]` |
| Verify downloaded file | `os.path.exists(file_path)` |
| Upload file | `element.send_keys("/absolute/path/to/file")` |

---

## Assignment / Practice

Practice keyboard actions, file download, and file upload on:

- 🔗 https://testautomationpractice.blogspot.com/ (has file upload and download sections to practice against)
