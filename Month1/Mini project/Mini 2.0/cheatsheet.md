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

