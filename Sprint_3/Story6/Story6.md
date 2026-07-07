# Sprint 3 — Story 6: API Testing Strategy & Security Cheatsheet

---

## Module 1 — Positive Testing

### What It Is
Validates the API works correctly with **valid inputs** — the happy path.

### Key Points
| Topic | Summary |
|---|---|
| Valid inputs | All required fields present, correct types, within allowed values |
| Happy path | The most common, expected user journey |
| Requirement-based | Every requirement = at least one positive test |

### Positive Test Case Design
| Test | Expected |
|---|---|
| All required fields valid | `200` or `201` + correct response body |
| Optional fields included | Accepted and reflected in response |
| Min valid input | Accepted |
| Max valid input | Accepted |

---

## Module 2 — Negative Testing

### What It Is
Validates the API **rejects invalid input** with the correct error code and message.

### Test Categories
| Category | Example | Expected |
|---|---|---|
| Invalid input | Letters in a numeric field | `400 Bad Request` |
| Missing mandatory field | POST body without required field | `400 Bad Request` |
| Wrong data type | `age: "twenty"` instead of `age: 20` | `400 Bad Request` |
| Invalid authentication | Wrong or missing token | `401 Unauthorized` |
| Invalid HTTP method | `DELETE` on a read-only endpoint | `405 Method Not Allowed` |

---

## Module 3 — Boundary Value Analysis (BVA)

### What It Is
Tests values **at and around boundaries** — where bugs most commonly hide.

### BVA Formula
| Point | Description | Example (min=8, max=20) |
|---|---|---|
| `Min - 1` | Just below minimum | 7 characters — should **fail** |
| `Min` | Exact minimum | 8 characters — should **pass** |
| `Min + 1` | Just above minimum | 9 characters — should **pass** |
| `Max - 1` | Just below maximum | 19 characters — should **pass** |
| `Max` | Exact maximum | 20 characters — should **pass** |
| `Max + 1` | Just above maximum | 21 characters — should **fail** |

### Why Boundary Bugs Occur
- Developers use `>` instead of `>=` (off-by-one errors)
- Boundary conditions are often not explicitly specified

### BVA Applied to APIs
```
Password min=8, max=64
Test: 7, 8, 9, 63, 64, 65 characters
```

---

## Module 4 — Equivalence Partitioning (EP)

### What It Is
Divides inputs into **partitions** — test one value per partition instead of every possible value.

### Partitions
| Partition | Description | Example (age field, valid: 18–65) |
|---|---|---|
| Valid partition | Values the API should accept | `25`, `18`, `65` |
| Invalid partition | Values the API should reject | `-1`, `0`, `17`, `66`, `"abc"` |

### BVA vs EP
| | BVA | EP |
|---|---|---|
| Focus | Exact boundary values | Representative value from each group |
| Test count | 6 per boundary | 1–2 per partition |
| Use together? | Yes — EP finds the groups, BVA tests the edges |

---

## Module 5 — Error Guessing

### What It Is
Experience-based testing — thinking like an attacker or a user who does unexpected things.

### Common Inputs to Try
| Input Type | Examples |
|---|---|
| Special characters | `!@#$%^&*()` in name or email fields |
| Unicode & emoji | `"Ünïcödé"`, `"😀"` in text fields |
| SQL injection | `' OR '1'='1`, `; DROP TABLE users;--` |
| Overflow inputs | 10,000-character string in a name field |
| Null / empty | `""`, `null`, `" "` (whitespace only) |
| Negative numbers | `-1` for quantity or age |
| Zero | `0` for price or count |

### Error Guessing Test Design
| Test | Expected |
|---|---|
| SQL injection in login | Auth should fail — not bypass |
| Emoji in username | Accepted or clear `400` — no crash |
| Extremely long string | `400 Bad Request` — no crash or timeout |
| Null in required field | `400 Bad Request` |

---

## Module 6 — Response Validation

| Validation Type | What to Check |
|---|---|
| Status code | Correct code for the scenario (200, 201, 400…) |
| Response body | Fields exist and have correct values |
| Required fields | All expected fields present — none missing or null |
| Data type | `id` is int, `name` is string, `active` is boolean |
| Header validation | `Content-Type: application/json` returned |
| Response time | Within acceptable threshold (e.g. < 2000ms) |
| Business logic | Rules enforced (e.g. duplicate email → 409) |

### Full Validation Checklist per Request
```
✅ Status code is correct
✅ Response body is valid JSON
✅ All required fields are present
✅ Data types are correct
✅ Values match expected output
✅ Headers are correct
✅ Response time is acceptable
✅ Business rule is enforced
```

---

## Module 7 — Swagger / OpenAPI

### What It Is
Swagger (OpenAPI) is interactive API documentation — defines every endpoint, parameter, and response the API supports.

### What Swagger Tells You
| Section | What to read |
|---|---|
| Endpoints | All available URLs (e.g. `GET /users`, `POST /login`) |
| HTTP methods | Which methods each endpoint supports |
| Parameters | Path params, query params, their types and if required |
| Request body | Required fields, data types, example values |
| Response structure | What a success/error response looks like |
| Auth requirements | Which endpoints need a token |
| Status codes | All documented response codes per endpoint |

### Designing Test Cases from Swagger
```
1. Read the endpoint spec
2. Identify required vs optional fields
3. Check data types and constraints
4. Write positive test → valid inputs per spec
5. Write negative tests → missing fields, wrong types
6. Apply BVA to any min/max constraints listed
7. Check all documented status codes are reachable
```

---

## Module 8 — API Security Testing

### Core Principle
> **Never trust the client.** Every input must be validated server-side.

### Security Threats
| Threat | Description | Test |
|---|---|---|
| Parameter tampering | Modifying URL/body params to access unauthorized data | Change `userId=42` to `userId=43` — should get `403` |
| SQL injection | Injecting SQL via input fields | `' OR '1'='1` in login — should not bypass auth |
| JWT tampering | Modifying JWT payload to escalate role | Change `"role":"user"` to `"role":"admin"` — should get `401` |
| BFLA (Broken Function Level Auth) | Calling admin-level endpoints as a regular user | `DELETE /admin/users` with user token — should get `403` |
| Mass assignment | Sending extra fields hoping the server accepts them | `POST /users` with `{ "role": "admin" }` — should be ignored |

### Security Test Case Design
| Test | Expected |
|---|---|
| Tampered JWT | `401 Unauthorized` — signature invalid |
| User accessing another user's data | `403 Forbidden` |
| Regular user calling admin endpoint | `403 Forbidden` |
| SQL injection in any input field | Auth fails — no data leaked |
| Mass assignment of protected fields | Fields ignored or `400` returned |
| Request without token | `401 Unauthorized` |

### Authentication vs Authorization — Final Review
| | Authentication | Authorization |
|---|---|---|
| Checks | Is the token valid? | Does this user have permission? |
| Fails with | `401` | `403` |
| Security test focus | Missing / expired / tampered tokens | RBAC, BOLA, BFLA violations |

---

## Quick Reference — Testing Strategy Summary

| Strategy | Best For |
|---|---|
| Positive testing | Verify happy path works |
| Negative testing | Verify invalid inputs are rejected |
| BVA | Catch off-by-one bugs at boundaries |
| EP | Efficient coverage — one test per input group |
| Error guessing | Catch edge cases from experience |
| Response validation | Verify every part of the response |
| Swagger review | Derive tests directly from the spec |
| Security testing | Catch auth flaws, injections, privilege escalation |
