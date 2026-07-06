# Sprint 3 — Story 3: Postman & Practical API Testing Cheatsheet

---

## Module 1 — Introduction to Postman

| Topic | Summary |
|---|---|
| Why Postman | Test APIs without writing code — send requests and inspect responses visually |
| Before UI dev | Test and validate backend APIs before the frontend is built |
| Interface | URL bar + method selector + headers/body tabs + response panel |
| Request lifecycle | Build request → Send → Server processes → Response returned → Validate |

---

## Module 2 — HTTP Requests

### GET vs POST
| | GET | POST |
|---|---|---|
| Purpose | Retrieve data | Create / send data |
| Body | No body | JSON body required |
| URL params | Query params in URL | Data in body |
| Success code | `200 OK` | `201 Created` |

### Key Parts
| Part | Description |
|---|---|
| Request URL | The endpoint being called |
| Request Body | JSON payload sent with POST / PUT / PATCH |
| Response Body | JSON data returned by the server |

---

## Module 3 — Parameters

### Path vs Query Parameters
| | Path Parameter | Query Parameter |
|---|---|---|
| Location | Inside the URL | After `?` in the URL |
| Purpose | Identifies a specific resource | Filters, sorts, or paginates |
| Example | `/users/42` | `/users?role=admin&status=active` |
| Required? | Yes | Usually optional |

```
/users/42              → path param  → which user
/users?role=admin      → query param → filter users by role
/users/42/orders?page=2 → both
```

---

## Module 4 — Headers

| Header | Purpose | Example |
|---|---|---|
| `Content-Type` | Format of the request body | `application/json` |
| `Accept` | Format the client wants back | `application/json` |
| `Authorization` | Proves who the caller is | `Bearer <token>` |
| `User-Agent` | Identifies the client app/tool | `PostmanRuntime/7.x` |
| `API Key` | Alternate auth method | `x-api-key: abc123` |
| Custom Headers | App-specific metadata | `x-request-id: xyz` |

### Authentication vs Authorization Headers
| | Authentication | Authorization |
|---|---|---|
| Question | Who are you? | What can you do? |
| Header | `Authorization: Bearer <token>` | Enforced server-side by role/permission |
| Fails with | `401 Unauthorized` | `403 Forbidden` |

---

## Module 5 — API Validation

| Validation Type | What to check |
|---|---|
| Status Code | Correct code returned (200, 201, 400, 404…) |
| Response Body | Body contains expected data |
| Required Fields | All required fields are present and not null |
| Data Validation | Correct types (string, int, boolean) and formats |
| Business Rule | Rules are enforced (e.g. duplicate email → 409) |
| Contract | Response matches the agreed API spec/schema |

### Test Case Types
| Type | Example |
|---|---|
| Positive | Valid login → 200 + token returned |
| Negative | Wrong password → 401 + error message |
| Boundary | Username at min length → accepted; one below → rejected |

---

## Module 6 — Collections

| Topic | Summary |
|---|---|
| Why collections | Group related requests — avoid recreating them each time |
| Folder structure | Organise by module (Auth, Users, Orders…) |
| Business modules | One folder per feature area |
| Sharing | Share via link or exported file |
| Export / Import | Save as `.json` → share with team → import in Postman |

### Example Structure
```
📁 Collection: E-Commerce API
  📂 Auth
    → POST /login
    → POST /register
  📂 Users
    → GET  /users
    → GET  /users/:id
  📂 Orders
    → POST /orders
    → GET  /orders/:id
```

---

## Module 7 — Environments & Variables

### Variable Types
| Type | Scope | Use case |
|---|---|---|
| Global | All collections, all environments | Rarely used — truly shared values |
| Environment | One environment (DEV / QA / UAT / PROD) | Base URL, tokens per env |
| Collection | One collection | Shared values across requests in that collection |

### Common Variables
| Variable | Value example |
|---|---|
| `base_url` | `https://api.dev.example.com` |
| `token` | `eyJhbGciOiJIUzI1NiIs...` |
| `user_id` | `42` |

### Usage in Postman
```
{{base_url}}/users/{{user_id}}
Authorization: Bearer {{token}}
```

### Switching Environments
```
DEV  → https://api.dev.example.com
QA   → https://api.qa.example.com
UAT  → https://api.uat.example.com
PROD → https://api.example.com
```
Switch environments in Postman → same requests, different values automatically.

---

## Module 8 — Postman Tests

Tests are written in JavaScript inside the **Tests** tab of a request.

### Common Assertions

**Status Code**
```javascript
pm.test("Status is 200", () => {
    pm.response.to.have.status(200);
});
```

**Response Body — property value**
```javascript
pm.test("Name is Alice", () => {
    const body = pm.response.json();
    pm.expect(body.name).to.eql("Alice");
});
```

**Required field present**
```javascript
pm.test("Token exists", () => {
    const body = pm.response.json();
    pm.expect(body.token).to.exist;
});
```

**Data type check**
```javascript
pm.test("ID is a number", () => {
    const body = pm.response.json();
    pm.expect(body.id).to.be.a("number");
});
```

**Array length**
```javascript
pm.test("Returns at least 1 user", () => {
    const body = pm.response.json();
    pm.expect(body.users.length).to.be.above(0);
});
```

**Response time**
```javascript
pm.test("Response under 2s", () => {
    pm.expect(pm.response.responseTime).to.be.below(2000);
});
```

### Quick Reference
| Assertion | Method |
|---|---|
| Status code | `pm.response.to.have.status(200)` |
| Body value | `pm.expect(body.field).to.eql("value")` |
| Field exists | `pm.expect(body.field).to.exist` |
| Data type | `pm.expect(body.field).to.be.a("string")` |
| Array length | `pm.expect(body.arr.length).to.be.above(0)` |
| Response time | `pm.expect(pm.response.responseTime).to.be.below(2000)` |
