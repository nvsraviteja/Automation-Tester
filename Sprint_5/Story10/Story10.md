# Selenium WebDriver — Sprint 5, Story 10 
### Topic: Mouse Operations (ActionChains) & Scrolling

Language: **Python + Selenium WebDriver**

---

## 0. What is ActionChains?

`ActionChains` is a Selenium class used to perform **complex/low-level user interactions** — mouse movements, clicks, drag-and-drop, keyboard combos — that a simple `.click()` can't handle.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

actions = ActionChains(driver)
```

All actions are **queued** first, then executed together with `.perform()`.

---

## 1. Mouse Hover

Simulates hovering the mouse over an element (commonly used to reveal dropdown/sub-menus).

```python
element = driver.find_element(By.ID, "menu-item")

actions.move_to_element(element).perform()
```

**Key points**
- `move_to_element(element)` moves the mouse pointer to the center of the element.
- Often needed before clicking a sub-menu item that only appears on hover:
```python
menu = driver.find_element(By.ID, "main-menu")
sub_menu = driver.find_element(By.ID, "sub-menu-item")

actions.move_to_element(menu).move_to_element(sub_menu).click().perform()
```

---

## 2. Right Click (Context Click)

Simulates a right-click, opening the browser's context menu (or a custom right-click menu on the page).

```python
element = driver.find_element(By.ID, "context-menu-area")

actions.context_click(element).perform()
```

**Key points**
- `context_click(element)` → right-clicks on the given element.
- If the page shows a **custom** context menu (not the OS-native one), you can then locate and click menu options normally with `find_element`.

---

## 3. Double Click

Simulates a double-click.

```python
element = driver.find_element(By.ID, "double-click-btn")

actions.double_click(element).perform()
```

**Key points**
- `double_click(element)` → performs a double-click on the element.
- Common use: text that gets selected/edited on double-click, or buttons whose action only triggers on double-click.

---

## 4. Drag and Drop

Simulates dragging an element from a source location and dropping it on a target element.

```python
source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

actions.drag_and_drop(source, target).perform()
```

**Key points**
- `drag_and_drop(source, target)` → picks up `source` and drops it exactly on `target`.
- Some modern JS-based drag-and-drop widgets don't respond correctly to this and may need a manual click-hold-move-release sequence:
```python
actions.click_and_hold(source).move_to_element(target).release().perform()
```

---

## 5. Slider (Drag by Offset)

Used for slider controls where you drag a handle by a specific pixel distance rather than to a fixed target element.

```python
slider = driver.find_element(By.ID, "slider-handle")

# Move the slider element by X pixels horizontally, Y pixels vertically
actions.drag_and_drop_by_offset(slider, 50, 0).perform()
```

**Key points**
- `drag_and_drop_by_offset(element, xoffset, yoffset)` → drags `element` by a relative pixel offset instead of dropping onto another element.
- `xoffset` → horizontal movement (positive = right, negative = left)
- `yoffset` → vertical movement (positive = down, negative = up)
- Useful for range sliders, volume controls, or resize handles where there's no separate "drop target" element.

---

## 6. Scrolling the Page

Selenium's `ActionChains` doesn't have a dedicated scroll method by default in older versions — the most common/reliable way is via **JavaScript Executor**. Selenium 4.2+ also added native `scroll_to_element` / `scroll_by_amount` on `ActionChains`.

### a) Scroll using JavaScript Executor (most common, cross-version)

```python
# Scroll down by pixels
driver.execute_script("window.scrollBy(0, 500);")

# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Scroll a specific element into view
element = driver.find_element(By.ID, "footer")
driver.execute_script("arguments[0].scrollIntoView(true);", element)
```

### b) Scroll using ActionChains (Selenium 4.2+)

```python
element = driver.find_element(By.ID, "footer")

# Scroll until the element is in view
actions.scroll_to_element(element).perform()

# Scroll by a given pixel amount from current position
actions.scroll_by_amount(0, 500).perform()
```

**Key points**
- `scrollIntoView(true)` aligns the element to the top of the viewport; `scrollIntoView(false)` aligns to the bottom.
- Scrolling is often needed before interacting with elements that are outside the current viewport, since Selenium can throw `ElementNotInteractableException` on off-screen elements in some cases.

---

## Quick Reference Table

| Action | Method |
|---|---|
| Mouse hover | `actions.move_to_element(element)` |
| Right click | `actions.context_click(element)` |
| Double click | `actions.double_click(element)` |
| Drag and drop (to target) | `actions.drag_and_drop(source, target)` |
| Drag by offset (slider) | `actions.drag_and_drop_by_offset(element, x, y)` |
| Click and hold | `actions.click_and_hold(element)` |
| Release | `actions.release()` |
| Scroll (JS) | `driver.execute_script("window.scrollBy(0, 500);")` |
| Scroll to element (JS) | `driver.execute_script("arguments[0].scrollIntoView(true);", element)` |
| Scroll to element (Selenium 4.2+) | `actions.scroll_to_element(element)` |

---

## Assignment / Practice

Practice mouse hover, right click, double click, drag-and-drop, slider, and scrolling on:

- 🔗 https://testautomationpractice.blogspot.com/ (has drag-and-drop, slider, and scroll sections to practice against)
