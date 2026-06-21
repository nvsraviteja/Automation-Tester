# Day 15 - Dictionaries

## 1. What is a Dictionary?

A dictionary stores data as key-value pairs. Instead of accessing data by position like a list, you access it by a named key.

**Real-world analogy:**

```
Name → Ravi
Age  → 24
Role → QA
```

Each key points directly to its value, making data easy to find and read.

---

## 2. Dictionary Syntax

Dictionaries use curly braces `{}`. Each entry is a key-value pair separated by a colon `:`, and pairs are separated by commas.

```python
user = {
    "name": "Ravi",
    "age": 24
}
```

---

## 3. Accessing Values

To get a value, pass its key inside square brackets.

```python
user["name"]  # Output: Ravi
```

---

## 4. Add / Update Values

The same syntax is used to both add a new key and update an existing one.

```python
# Add a new key
user["role"] = "QA"

# Update an existing key
user["age"] = 25
```

- If the key does not exist → it gets added
- If the key already exists → its value gets updated

---

## 5. Dictionary Methods

| Method | What it returns |
|--------|-----------------|
| `.keys()` | All keys in the dictionary |
| `.values()` | All values in the dictionary |
| `.items()` | All key-value pairs as tuples |

```python
user.keys()    # dict_keys(["name", "age", "role"])
user.values()  # dict_values(["Ravi", 24, "QA"])
user.items()   # dict_items([("name", "Ravi"), ("age", 24), ("role", "QA")])
```

These methods become essential when working with automation and looping through API responses.

---

## 6. JSON Mindset

This is an important concept for API testing.

A JSON response and a Python dictionary look almost identical:

**JSON (API response):**
```json
{
  "status": 200,
  "message": "success"
}
```

**Python dictionary:**
```python
{
    "status": 200,
    "message": "success"
}
```

> **Key idea:** JSON ≈ Python Dictionary. When Python receives an API response, it converts the JSON into a dictionary automatically — which means everything you learned about dictionaries applies directly to API testing.

---

## 7. QA Use Cases

Dictionaries allow QA engineers to validate real API responses.

**Status code validation:**
```python
response["status"]  # Expected: 200
```

**Message validation:**
```python
response["message"]  # Expected: "success"
```

**User data validation:**
```python
response["id"]
response["name"]
response["email"]
```

Instead of manually checking each field, Python can access and validate any value instantly using its key.
