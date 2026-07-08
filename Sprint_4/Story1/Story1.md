# Sprint 4 — Story 1: Python `requests` Library Cheatsheet

---

## Setup

```bash
pip install requests
```
```python
import requests
```

---

## Response Object Properties

| Property | Returns | Use for |
|---|---|---|
| `response.status_code` | `int` — e.g. `200`, `404` | Validate the outcome |
| `response.text` | `str` — raw response as string | Plain text or HTML responses |
| `response.json()` | `dict` / `list` — parsed JSON | JSON API responses |
| `response.content` | `bytes` — raw bytes | Files, images, binary data |
| `response.headers` | `dict` — response headers | Check `Content-Type`, auth headers |
| `response.elapsed` | `timedelta` — response time | Performance / timeout validation |

### `.text` vs `.json()` vs `.content`
| | `.text` | `.json()` | `.content` |
|---|---|---|---|
| Type | `str` | `dict` / `list` | `bytes` |
| Use when | Reading raw text | API JSON response | Binary / file download |

---

## GET Requests

```python
# Basic GET
response = requests.get("https://api.example.com/users/42")

# With query parameters
response = requests.get("https://api.example.com/users", params={"role": "admin"})

# With timeout
response = requests.get("https://api.example.com/users/42", timeout=5)
```

### Reusable Function
```python
def get_user(user_id):
    try:
        response = requests.get(
            f"https://api.example.com/users/{user_id}",
            timeout=5
        )
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
```

---

## POST Requests

```python
# Basic POST with JSON payload
payload = {"username": "alice", "email": "alice@example.com"}
response = requests.post("https://api.example.com/users", json=payload)

# Expected: 201 Created
```

### Reusable Function
```python
def create_user(username, email):
    payload = {"username": username, "email": email}
    response = requests.post(
        "https://api.example.com/users",
        json=payload,
        timeout=5
    )
    return response
```

---

## PUT, PATCH & DELETE

```python
# PUT — replace entire resource
response = requests.put(
    "https://api.example.com/users/42",
    json={"username": "alice_new", "email": "new@example.com"}
)

# PATCH — update specific fields only
response = requests.patch(
    "https://api.example.com/users/42",
    json={"email": "updated@example.com"}
)

# DELETE — remove resource
response = requests.delete("https://api.example.com/users/42")
# Expected: 204 No Content (empty body — don't call .json())
```

### Handling Empty Responses (204)
```python
if response.status_code == 204:
    return None   # no body to parse
return response.json()
```

### PUT vs PATCH
| | PUT | PATCH |
|---|---|---|
| Scope | Replaces entire resource | Updates specific fields |
| Required fields | All fields | Only changed fields |

---

## Headers & Authentication

```python
# Building reusable headers
def get_headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

# Using headers in a request
headers = get_headers("my_token_here")
response = requests.get("https://api.example.com/profile", headers=headers)
```

### Common Headers
| Header | Purpose | Example |
|---|---|---|
| `Authorization` | Prove identity | `Bearer <token>` |
| `Content-Type` | Format of request body | `application/json` |
| `Accept` | Format client wants back | `application/json` |

### Auth Status Codes
| Code | Meaning |
|---|---|
| `401` | Not authenticated — missing or invalid token |
| `403` | Authenticated but not authorized for this action |

---

## Sessions

```python
# Create a session
session = requests.Session()

# Set persistent headers (applied to every request)
session.headers.update({
    "Authorization": "Bearer my_token",
    "Content-Type": "application/json"
})

# Requests reuse headers and cookies automatically
response = session.get("https://api.example.com/users")
response = session.post("https://api.example.com/orders", json={"item": "book"})

# Update a header mid-session
session.headers.update({"Authorization": "Bearer new_token"})
```

### Why Use Sessions?
| Benefit | Detail |
|---|---|
| Persistent headers | Set once — applied to all requests |
| Persistent cookies | Cookies carried across requests automatically |
| Connection reuse | Faster — no reconnecting for every request |
| Session-based auth | Ideal for flows where you login once and send many requests |

---

## Exception Handling

```python
import requests

def safe_get(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()   # raises HTTPError for 4xx / 5xx
        return response
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.ConnectionError:
        print("Connection failed")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Unexpected error: {e}")
    return None
```

### Exception Types
| Exception | When it triggers |
|---|---|
| `Timeout` | Request exceeded the timeout limit |
| `ConnectionError` | Network unreachable / DNS failure |
| `HTTPError` | 4xx or 5xx — raised by `raise_for_status()` |
| `RequestException` | Base class — catches all `requests` errors |

### `raise_for_status()`
- Automatically raises `HTTPError` for any `4xx` or `5xx` response
- Call it right after the request if you want to fail fast on bad status codes

---

## Professional Coding Practices

| Practice | Why |
|---|---|
| Reusable functions | Write once, call anywhere — no duplication |
| No hardcoded values | Use variables for URLs, tokens, timeouts |
| Dynamic URLs | `f"https://api.example.com/users/{user_id}"` |
| Dynamic payloads | Build dict from parameters, not hardcoded strings |
| Return responses | Return the object — let the caller decide what to assert |
| Separation of concerns | One function = one job (SRP) |
| Framework-oriented thinking | Write code that fits into a larger test framework |

### ✅ Do This
```python
BASE_URL = "https://api.example.com"

def get_user(user_id, token):
    headers = get_headers(token)
    response = requests.get(f"{BASE_URL}/users/{user_id}", headers=headers, timeout=5)
    return response
```

### ❌ Not This
```python
def get_user():
    response = requests.get("https://api.example.com/users/42")
    print(response.json())   # hardcoded ID + prints instead of returning
```

---

## QA Concepts Reinforced

| Concept | How it maps to `requests` |
|---|---|
| Status code validation | `assert response.status_code == 200` |
| Response body validation | `assert response.json()["name"] == "Alice"` |
| Header validation | `assert "application/json" in response.headers["Content-Type"]` |
| Response time | `assert response.elapsed.total_seconds() < 2` |
| Authentication testing | Send request without token → assert `401` |
| Authorization testing | Send request with wrong-role token → assert `403` |
| Positive testing | Valid inputs → correct success response |
| Negative testing | Invalid inputs → correct error + code |
| Security testing | Tampered token / wrong user ID → `401` / `403` |
| Business logic | Duplicate email → `409`, deleted user → `404` |

---

## Quick Reference — All HTTP Methods

```python
requests.get(url, params={}, headers={}, timeout=5)
requests.post(url, json={}, headers={}, timeout=5)
requests.put(url, json={}, headers={}, timeout=5)
requests.patch(url, json={}, headers={}, timeout=5)
requests.delete(url, headers={}, timeout=5)
```
