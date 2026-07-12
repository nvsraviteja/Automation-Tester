# Sprint 5 — Story 3: XPath Axes Cheatsheet

---

## What is an XPath Axis?

An XPath axis defines the **direction and relationship** to navigate from the current node (element) to find another element in the HTML tree.

```python
driver.find_element(By.XPATH, "//div/child::input")
```

---

## HTML Tree Reference

```html
<form id="loginForm">
  <div class="row">
    <label>Username</label>
    <input id="username" type="text" />
  </div>
  <div class="row">
    <label>Password</label>
    <input id="password" type="password" />
  </div>
  <button type="submit">Login</button>
</form>
```

---

## XPath Axes

### `child`
Selects **direct children** of the current node.

```xpath
//form/child::input
//div/child::label
```
```python
driver.find_element(By.XPATH, "//form/child::button")
```

---

### `parent`
Selects the **direct parent** of the current node.

```xpath
//input[@id='username']/parent::div
```
```python
driver.find_element(By.XPATH, "//input[@id='username']/parent::div")
```

> Useful when you know the child but need to act on its container.

---

### `following`
Selects **all nodes that appear after** the current node in the document (not just siblings).

```xpath
//label[text()='Username']/following::input
```
```python
driver.find_element(By.XPATH, "//label[text()='Username']/following::input")
```

---

### `preceding`
Selects **all nodes that appear before** the current node in the document.

```xpath
//button[@type='submit']/preceding::input
```
```python
driver.find_elements(By.XPATH, "//button[@type='submit']/preceding::input")
```

---

### `following-sibling`
Selects **siblings that come after** the current node (same parent level only).

```xpath
//label[text()='Username']/following-sibling::input
```
```python
driver.find_element(By.XPATH, "//label[text()='Username']/following-sibling::input")
```

> More precise than `following` — stays on the same level.

---

### `preceding-sibling`
Selects **siblings that come before** the current node (same parent level only).

```xpath
//input[@id='password']/preceding-sibling::label
```
```python
driver.find_element(By.XPATH, "//input[@id='password']/preceding-sibling::label")
```

---

### `ancestor`
Selects **all parents, grandparents, and above** of the current node.

```xpath
//input[@id='username']/ancestor::form
```
```python
driver.find_element(By.XPATH, "//input[@id='username']/ancestor::form")
```

> Useful for navigating up multiple levels to a known container.

---

### `descendant`
Selects **all children, grandchildren, and below** of the current node.

```xpath
//form/descendant::input
```
```python
driver.find_elements(By.XPATH, "//form/descendant::input")
# Returns all input elements anywhere inside the form
```

---

## Axes Summary Table

| Axis | Direction | Scope | Example use case |
|---|---|---|---|
| `child` | Down | Direct children only | Find input inside a div |
| `parent` | Up | Direct parent only | Find container of an input |
| `following` | Forward | All nodes after (whole doc) | Find any element after current |
| `preceding` | Backward | All nodes before (whole doc) | Find any element before current |
| `following-sibling` | Forward | Same-level siblings after | Find sibling input after a label |
| `preceding-sibling` | Backward | Same-level siblings before | Find sibling label before an input |
| `ancestor` | Up | All parents up the tree | Find the parent form of an input |
| `descendant` | Down | All children down the tree | Find all inputs inside a form |

---

## `following` vs `following-sibling`

| | `following` | `following-sibling` |
|---|---|---|
| Scope | Everything after in the entire document | Siblings only (same parent) |
| More precise? | No | Yes |
| Use when | Target could be anywhere below | Target is at the same level |

---

## Syntax Pattern

```
//currentNode/axis::targetNode
//currentNode/axis::targetNode[@attribute='value']
```

```xpath
//label[text()='Username']/following-sibling::input[@type='text']
//input[@id='username']/ancestor::form[@id='loginForm']
//form[@id='loginForm']/descendant::input[@type='password']
```

---

## Quick Decision Guide

```
Need a child element?          → child::
Need the parent container?     → parent::
Need a sibling after?          → following-sibling::
Need a sibling before?         → preceding-sibling::
Need anything after (any level)? → following::
Need anything before (any level)? → preceding::
Need any ancestor up the tree? → ancestor::
Need any nested element?       → descendant::
```
