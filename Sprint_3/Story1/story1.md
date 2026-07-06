# Sprint 3 — Story 1: API Fundamentals Cheatsheet

---

## What is an API?
A middleman between client and server that protects the database and centralizes business logic.

---

## Why APIs Exist
| Reason | What it does |
|---|---|
| Security | Database is never directly exposed |
| Centralized logic | Business rules live in one place |
| DB protection | Validates & sanitizes inputs |
| Auth layer | Checks who you are and what you can do |

---

## Client vs Server
| Role | Description |
|---|---|
| Client | Makes the request (browser, app, test script) |
| Server | Receives, processes, and responds |

---

## API Request Flow
```
Client → API Endpoint → Business Logic → Database → Response → Client
```

---

## HTTP Request Components
| Part | Purpose |
|---|---|
| URL | Identifies the resource |
| Method | The action (GET, POST…) |
| Headers | Auth token, content type |
| Body | Data payload (POST / PUT / PATCH only) |

---

## HTTP Methods
| Method | Action | Changes State? | Has Body? |
|---|---|---|---|
| `GET` | Read / retrieve | No | No |
| `POST` | Create | Yes | Yes |
| `PUT` | Replace entire resource | Yes | Yes |
| `PATCH` | Update specific fields | Yes | Yes |
| `DELETE` | Remove resource | Yes | No |

---

## Key Comparisons
| vs | Difference |
|---|---|
| GET vs POST | Read (no change) vs Create (changes state) |
| PUT vs PATCH | Full replace vs partial update |
| PATCH vs DELETE | Modify vs remove |
| Soft vs Hard delete | Flag as deleted vs actually removed |

---

## RESTful URL Design — Same URL, Different Methods
```
GET    /users/42   → Read user 42
POST   /users      → Create new user
PUT    /users/42   → Replace user 42 entirely
PATCH  /users/42   → Update specific fields
DELETE /users/42   → Delete user 42
```

---

## Test Scenario Types
| Type | What to test |
|---|---|
| Positive | Valid input → correct success response |
| Negative | Invalid input → correct error + status code |
| Edge cases | Min/max boundaries, special chars, duplicates |

---

## Requirement Gathering — Ask Before Testing
- Min / max username and password length?
- Allowed characters (special, unicode)?
- Case-sensitive passwords?
- Max failed login attempts before lockout?
- Does lockout expire or need manual reset?
- Can the same email register twice?

---

## QA Thinking Order
```
1. Understand requirements
2. Ask clarification questions
3. Design test scenarios
4. Then automate
```

> Every business rule = a test case.
> Missing requirements = gaps = future bugs.


