Cheat Sheet — OOP Design Thinking (QA Focus)

## What is O2?
O2 is not about writing syntax.

O2 asks:
- Which class should exist?
- Which method belongs to which class?
- Who owns this responsibility?

Core goal:

```text
Think in objects, not functions
```

---

## Rule 1 — Classes are usually Nouns
Classes represent **entities / objects / components**.

Examples:

✅ Classes
- User
- Product
- Cart
- Payment
- Browser
- LoginPage
- Reporter

These are “things”.

Example:
```python
class User:
    pass
```

---

## Rule 2 — Methods are usually Verbs
Methods represent **actions / behaviors**.

Examples:

✅ Methods
- login()
- logout()
- add_product()
- remove_product()
- click()
- search()
- pay()

These are actions.

Example:
```python
class User:
    def login(self):
        pass
```
---

## Golden Rule
Ask:

```text
Who owns this action?
```

That object gets the method.

Example:

Action:
```python
login()
```

Question:
Who owns login?

Answer:
```text
User or LoginPage
```

Depends on system design.

---

## Rule 3 — Identify Nouns and Verbs from Requirement

Example requirement:

> User places order from restaurant using payment.

### Step 1 — Find nouns:
- User
- Order
- Restaurant
- Payment

Likely classes.

### Step 2 — Find verbs:
- places
- pays

Likely methods.

---

## Responsibility Mapping

| Action | Likely Class |
|---|---|
| login() | User / LoginPage |
| add_product() | Cart |
| remove_product() | Cart |
| pay() | Payment |
| refund() | Payment |
| check_stock() | Product |
| search_product() | ProductPage / SearchBar |
| take_screenshot() | Reporter / BasePage |
| click_login_button() | LoginPage |
| open_browser() | Browser / BasePage |

---


## Business App vs Automation Framework
Very important.

Always ask:

```text
Am I designing the application?
OR
Am I designing the automation framework?
```

---

### Application Design Example
E-commerce app classes:

- User
- Product
- Cart
- Order
- Payment

Methods:
```python
user.login()
cart.add_product()
payment.pay()
```

---

### Automation Framework Design Example
QA framework classes:

- Browser
- BasePage
- LoginPage
- ProductPage
- Reporter

Methods:
```python
browser.open()
login_page.login()
product_page.search_product()
reporter.take_screenshot()
```

Notice:

Same system.  
Different design.

---

## Rule 4 — Page Object Model (POM)
In automation, pages often become classes.

Example:

```text
pages/
 ├── base_page.py
 ├── login_page.py
 ├── product_page.py
```

---

### BasePage
Shared methods:
- click()
- wait()
- screenshot()
- scroll()

Example:
```python
class BasePage:
    def click(self):
        pass
```

---

### LoginPage
Page-specific methods:
- enter_username()
- enter_password()
- login()

Example:
```python
class LoginPage(BasePage):
    def login(self):
        pass
```

---

### ProductPage
Methods:
- search_product()
- add_to_cart()

Example:
```python
class ProductPage(BasePage):
    def add_to_cart(self):
        pass
```

---

## Rule 5 — Method Placement Test
Before placing a method, ask:

1. Who owns the data?
2. Who controls the action?
3. Who knows required details?

That class gets the method.

Example:

Method:
```python
search_product()
```

Question:
Who knows search bar locator?

Answer:
```text
ProductPage or SearchBar
```

Not User.

---

## Common Mistakes

### Mistake 1 — Thinking in features
❌
- signup
- login
- buy now

These are actions, not classes.

---

### Mistake 2 — Mixing app design and framework design
Requirement:
```text
QA automation framework
```

Wrong answer:
```text
Payment class
```

Problem:
Payment belongs to app design, not framework.

---

### Mistake 3 — Wrong responsibility assignment
❌ Product class
```python
add_to_cart()
```

Why wrong?

Product doesn’t manage cart.

Correct:

✅ Cart class
```python
add_product()
```

---

## Fast Mental Shortcut

### Step 1
```text
Find nouns → possible classes
```

### Step 2
```text
Find verbs → possible methods
```

### Step 3
```text
Ask who owns this responsibility
```

---

## Interview Trick
If interviewer asks:

> Design automation framework for login page.

Think:

### Classes
- Browser
- BasePage
- LoginPage
- Reporter

### Methods

#### Browser
- open()
- close()

#### LoginPage
- login()
- logout()

#### Reporter
- take_screenshot()
- generate_report()

---

# Final O2 Summary

O1 taught:
```text
How to write OOP
```

O2 taught:
```text
How to think in OOP
```

Big difference.

Goal:

```text
Stop thinking:
"What function should I write?"

Start thinking:
"Which object should own this behavior?"
```