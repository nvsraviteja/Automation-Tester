# Sprint 3 — Story 2: HTTP Request & Response Cheatsheet

---

## HTTP Request Components
| Part | Purpose | Example |
|---|---|---|
| URL | Identifies the resource | `https://api.example.com/users/42` |
| Method | The action to perform | `GET`, `POST`, `PATCH`… |
| Headers | Metadata about the request | Auth token, content type |
| Body | Data payload | JSON object (POST / PUT / PATCH) |

---

## URL & Query Parameters
```
https://api.example.com/users?role=admin&status=active
│                        │     └─ query parameters (filter / sort / paginate)
│                        └─ resource / endpoint
└─ base URL
```
- Query params start with `?` and are separated by `&`
- Used to pass extra info without changing the endpoint

---

## Common Request Headers
| Header | Purpose | Example |
|---|---|---|
| `Content-Type` | Format of the body being sent | `application/json` |
| `Authorization` | Proves who the caller is | `Bearer <token>` |

---

## Request Body
- Only used with `POST`, `PUT`, `PATCH`
- Usually sent as JSON

```json
{
  "username": "alice",
  "password": "secret123"
}
```

---

## HTTP Response Components
| Part | Purpose |
|---|---|
| Status Code | 3-digit number telling you what happened |
| Headers | Metadata about the response (content type, etc.) |
| Body | The returned data (usually JSON) |

---

## Request vs Response
| | Request | Response |
|---|---|---|
| Sent by | Client | Server |
| Contains | Method + URL + Headers + Body | Status code + Headers + Body |
| Purpose | Ask the server to do something | Tell the client what happened |

---

## Authentication vs Authorization
| Concept | Question it answers | Example |
|---|---|---|
| Authentication | Who are you? | Login — verify identity |
| Authorization | What are you allowed to do? | Role check — can this user delete? |

> You can be authenticated but still unauthorized (403).

---

## Bearer Token
- Sent in the `Authorization` header
- Proves the caller is logged in

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

## Content-Type: application/json
- Tells the server the body is in JSON format
- Always required when sending a JSON body

```
Content-Type: application/json
```

---

## Status Codes
| Code | Name | Meaning |
|---|---|---|
| `200` | OK | Request succeeded, data returned |
| `201` | Created | New resource created successfully |
| `400` | Bad Request | Client sent invalid data |
| `401` | Unauthorized | Not logged in / missing or invalid token |
| `403` | Forbidden | Logged in but not allowed to do this |
| `404` | Not Found | Resource doesn't exist |
| `409` | Conflict | Duplicate — resource already exists |
| `500` | Internal Server Error | Something broke on the server |

---

## Key Differences
| vs | Difference |
|---|---|
| `200` vs `201` | 200 = retrieved, 201 = newly created |
| `400` vs `404` | 400 = bad input, 404 = resource doesn't exist |
| `401` vs `403` | 401 = not logged in, 403 = logged in but no permission |

---

## Client-side Errors (4xx) vs Server-side Errors (5xx)
| Category | Who's responsible | Fix |
|---|---|---|
| 4xx | Client sent a bad request | Fix the request (wrong data, missing token, wrong URL) |
| 5xx | Server failed to process it | Server-side bug — not the client's fault |

---

## Validating Error Responses
A correct API should always return:
- The right **status code** for the situation
- A meaningful **error message** in the body

```json
{
  "error": "Invalid credentials",
  "status": 401
}
```
> Don't just check if the request failed — check that it failed **with the right code and message**.

---

## Reading JSON Responses
```json
{
  "id": 42,
  "name": "Alice",
  "role": "admin",
  "token": "eyJhbGc..."
}
```
- Access values by key: `response["name"]` → `"Alice"`
- Nested objects: `response["address"]["city"]`
- Arrays: `response["skills"][0]`

---

## QA Thinking
| Scenario | QA Action |
|---|---|
| Got a `4xx` error | Client is responsible — check request data, headers, URL |
| Got a `5xx` error | Server is responsible — investigate before raising a defect |
| Status code is wrong | Bug — API returned 200 but should be 201, or 200 but should be 400 |
| Error message is vague | Bug — response body should describe what went wrong |
| Response body is missing fields | Bug — contract is broken |

### Before Raising a Defect on a 500
1. Check if the request body is valid
2. Check if required headers are present
3. Check if the endpoint/URL is correct
4. If all are correct → server-side bug → raise defect

### Predict Before You Execute
- Before running a test, state what status code and response body you expect
- If actual ≠ expected → investigate why
- This habit catches incorrect assumptions early
