# Sprint 5 — Story 2: Selenium Locators Cheatsheet

---

## What is a Locator?

A locator tells Selenium **how to find an element** on a web page.
Every interaction (click, type, read) requires finding the element first.

```python
driver.find_element(By.ID, "username")       # find one element
driver.find_elements(By.CLASS_NAME, "item")  # find all matching elements (returns list)
```

---

## Types of Locators

### ID
- Fastest and most reliable locator
- Should be unique on the page

```python
driver.find_element(By.ID, "username")
```
```html
<input id="username" type="text" />
```

---

### Name
- Targets the `name` attribute of an element

```python
driver.find_element(By.NAME, "password")
```
```html
<input name="password" type="password" />
```

---

### Link Text
- Targets `<a>` tags by their **exact** visible text

```python
driver.find_element(By.LINK_TEXT, "Forgot Password?")
```
```html
<a href="/reset">Forgot Password?</a>
```

---

### Partial Link Text
- Targets `<a>` tags by **part** of their visible text
- Useful when the link text is long or dynamic

```python
driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot")
```
```html
<a href="/reset">Forgot Password?</a>
```

---

### Class Name
- Targets elements by their `class` attribute
- If the element has multiple classes, use just one of them

```python
driver.find_element(By.CLASS_NAME, "oxd-input")
```
```html
<input class="oxd-input oxd-input--active" />
```

> ⚠️ If multiple elements share the same class, `find_element` returns the first match.
> Use `find_elements` to get all of them.

---

### Tag Name
- Targets elements by their HTML tag
- Rarely used alone — usually returns too many elements

```python
driver.find_element(By.TAG_NAME, "h1")
driver.find_elements(By.TAG_NAME, "input")  # returns all input fields
```
```html
<h1>Welcome to OrangeHRM</h1>
```

---

## Locator Summary Table

| Locator | `By` constant | Targets | Best when |
|---|---|---|---|
| ID | `By.ID` | `id` attribute | Element has a unique ID |
| Name | `By.NAME` | `name` attribute | Form fields with name attribute |
| Link Text | `By.LINK_TEXT` | Exact anchor text | Short, stable link text |
| Partial Link Text | `By.PARTIAL_LINK_TEXT` | Partial anchor text | Long or dynamic link text |
| Class Name | `By.CLASS_NAME` | `class` attribute | Element has a unique class |
| Tag Name | `By.TAG_NAME` | HTML tag | Finding all elements of a type |
| CSS Selector | `By.CSS_SELECTOR` | CSS pattern | Flexible, powerful targeting |
| XPath | `By.XPATH` | XML path expression | Complex or deeply nested elements |

---

## Customised Locators — CSS Selector

CSS Selectors are powerful and flexible — they can target elements by **tag, ID, class, attribute, or combinations** of these.

### Syntax Patterns

| Pattern | Syntax | Example |
|---|---|---|
| By tag | `tag` | `input` |
| By ID | `#id` | `#username` |
| By class | `.class` | `.oxd-input` |
| By tag + ID | `tag#id` | `input#username` |
| By tag + class | `tag.class` | `input.oxd-input` |
| By attribute | `[attr='value']` | `[type='submit']` |
| By tag + attribute | `tag[attr='value']` | `input[name='username']` |
| Child element | `parent > child` | `form > input` |
| Descendant | `ancestor descendant` | `div input` |
| Multiple classes | `.class1.class2` | `.btn.btn-primary` |

### Examples

```python
# By ID
driver.find_element(By.CSS_SELECTOR, "#username")

# By class
driver.find_element(By.CSS_SELECTOR, ".oxd-input")

# By tag + class
driver.find_element(By.CSS_SELECTOR, "input.oxd-input")

# By attribute
driver.find_element(By.CSS_SELECTOR, "input[name='username']")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

# Tag + attribute
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']")

# Child — input directly inside a form
driver.find_element(By.CSS_SELECTOR, "form > input")

# Descendant — any input inside a div
driver.find_element(By.CSS_SELECTOR, "div input")
```

---

## `find_element` vs `find_elements`

| | `find_element` | `find_elements` |
|---|---|---|
| Returns | Single `WebElement` | `List` of `WebElement` |
| If not found | Raises `NoSuchElementException` | Returns empty list `[]` |
| Use when | You expect one match | You expect multiple matches |

```python
# Single element
login_btn = driver.find_element(By.ID, "loginBtn")

# Multiple elements
all_inputs = driver.find_elements(By.TAG_NAME, "input")
print(len(all_inputs))  # number of input fields on the page
```

---

## Choosing the Right Locator

```
Has a unique ID?          → Use ID          ← always prefer this
Has a name attribute?     → Use Name
It's a link?              → Use Link Text / Partial Link Text
Has a unique class?       → Use Class Name
Need flexible targeting?  → Use CSS Selector
Deeply nested or complex? → Use XPath (covered in next story)
```
