# Sprint 3 — Story 5: Advanced REST APIs Cheatsheet

---

## Module 1 — Pagination

### What & Why
Pagination splits large datasets into smaller pages — prevents returning thousands of records in one response.

### Types
| Type | How it works | Example |
|---|---|---|
| Page-based | Page number + size | `?page=2&limit=10` |
| Offset-based | Skip N records, take N | `?offset=20&limit=10` |

### Common Response Fields
```json
{
  "data": [...],
  "page": 2,
  "limit": 10,
  "total": 95,
  "totalPages": 10
}
```

### Test Cases
| Test | Expected |
|---|---|
| First page | Returns first N records |
| Last page | Returns remaining records (may be less than limit) |
| Page beyond total | Empty array `[]`, not an error |
| `page=0` or negative | `400 Bad Request` |
| `limit=0` | `400 Bad Request` |
| Very large limit | Should be capped or return `400` |

---

## Module 2 — Filtering

### What & Why
Filtering narrows results using query parameters — returns only records matching specific criteria.

```
GET /users?role=admin
GET /users?role=admin&status=active     ← multiple filters
```

### Test Cases
| Test | Expected |
|---|---|
| Single valid filter | Returns matching records only |
| Multiple valid filters | Returns records matching ALL conditions |
| Filter with no matches | Empty array `[]`, not an error |
| Invalid filter value | `400 Bad Request` |
| Filter on non-existent field | `400 Bad Request` or ignored (check spec) |
| Filter + pagination combined | Pagination applied after filtering |

---

## Module 3 — Sorting

### Parameters
```
GET /users?sort=name&order=asc
GET /users?sort=createdAt&order=desc
```

| Parameter | Values | Default |
|---|---|---|
| `sort` | Field name (`name`, `age`, `createdAt`) | Usually `id` or `createdAt` |
| `order` | `asc` or `desc` | Usually `asc` |

### Test Cases
| Test | Expected |
|---|---|
| `order=asc` | Results in ascending order |
| `order=desc` | Results in descending order |
| Invalid `sort` field | `400 Bad Request` |
| Invalid `order` value | `400 Bad Request` |
| Sort + filter combined | Filter first, then sort results |
| Sort + pagination combined | Sort applied before pagination |

---

## Module 4 — Searching vs Filtering

### Difference
| | Searching | Filtering |
|---|---|---|
| Input | Free text | Specific field value |
| Matches | Partial / fuzzy matches | Exact matches |
| Parameter | `?q=alice` or `?search=alice` | `?role=admin` |
| Example | Find users whose name contains "ali" | Find all users with role = admin |

```
GET /users?q=alice          ← search
GET /users?role=admin       ← filter
```

### Test Cases
| Test | Expected |
|---|---|
| Valid search term | Returns matching records |
| No matches | Empty array `[]` |
| Empty search string | `400 Bad Request` or return all (check spec) |
| Special characters (`<`, `>`, `'`) | Should be sanitized — not cause errors |
| Very long search string | `400 Bad Request` or truncated |
| Search + filter combined | Both conditions applied |

---

## Module 5 — API Versioning

### Why It Exists
Allows the API to evolve without breaking existing clients that depend on the old version.

### Versioning Styles
| Style | Example |
|---|---|
| URL versioning | `/v1/users`, `/v2/users` |
| Header versioning | `Accept: application/vnd.api+json;version=2` |
| Query param versioning | `/users?version=2` |

> **Most common:** URL versioning (`/v1`, `/v2`)

### Key Concepts
| Concept | Summary |
|---|---|
| Backward compatibility | Old clients using v1 must not break when v2 is released |
| Deprecation | v1 still works but shows warning — will be removed at a future date |

### Test Cases
| Test | Expected |
|---|---|
| Request to `/v1` endpoint | Returns v1 response structure |
| Request to `/v2` endpoint | Returns v2 response structure |
| Request to deprecated version | `200` but with deprecation warning header |
| Request to non-existent version | `404 Not Found` |
| v1 and v2 same endpoint | Responses may differ — test both schemas |

---

## Module 6 — Rate Limiting

### What & Why
Limits the number of requests a client can make in a time window — prevents abuse and brute-force attacks.

### Key Header
```
HTTP/1.1 429 Too Many Requests
Retry-After: 60
```

### Limit Types
| Type | Example |
|---|---|
| Per user | 100 requests / minute per account |
| Per IP | 1000 requests / hour per IP address |
| Per API key | 500 requests / day per key |

### Test Cases
| Test | Expected |
|---|---|
| Within rate limit | `200 OK` |
| Exceeds rate limit | `429 Too Many Requests` |
| `Retry-After` header present | Shows seconds until reset |
| After wait period expires | Requests succeed again |
| Brute-force login attempts | Locked out after N failures |
| Different users, same IP | Limits tracked separately per user |

---

## Module 7 — Caching

### What & Why
Caching stores previous responses and reuses them — reduces load on the server and speeds up responses.

### Key Headers
| Header | Purpose | Example |
|---|---|---|
| `Cache-Control` | Controls caching behaviour | `Cache-Control: max-age=3600` |
| `max-age` | Seconds the response is valid | `3600` = 1 hour |
| Stale cache | Cached response past its `max-age` | Should be refreshed |

### What to Cache vs Not Cache
| Cache ✅ | Don't Cache ❌ |
|---|---|
| Product listings | User-specific data |
| Public static content | Auth tokens |
| Search results (short-lived) | Payment / financial data |
| Config / metadata | Real-time data (live scores, stock prices) |

### Test Cases
| Test | Expected |
|---|---|
| Repeated GET within `max-age` | Returns cached response (faster) |
| GET after `max-age` expires | Fetches fresh data from server |
| Sensitive endpoint (user profile) | No caching — fresh data every time |
| `Cache-Control: no-store` | Response never stored |

---

## Module 8 — Idempotency

### What It Means
An operation is **idempotent** if calling it multiple times produces the same result as calling it once.

| Method | Idempotent? | Why |
|---|---|---|
| `GET` | ✅ Yes | Reads only — no side effects |
| `PUT` | ✅ Yes | Replaces resource — same result every time |
| `DELETE` | ✅ Yes | Already deleted = same end state |
| `POST` | ❌ No | Creates new record every time (without idempotency key) |
| `PATCH` | ⚠️ Depends | Usually yes, but depends on implementation |

### Idempotency Key
A unique key sent by the client to prevent duplicate operations.

```
POST /payments
Idempotency-Key: a1b2c3d4-unique-key
```

- If the same key is sent again → server returns the **original response** instead of processing again
- Critical for payments, order creation, and any non-reversible operations

### Scenarios
| Scenario | Without Idempotency | With Idempotency Key |
|---|---|---|
| Payment retry on network failure | Double charge | Single charge |
| Duplicate order submit (double click) | Two orders created | One order created |
| Request timeout + retry | Duplicate record | Same record returned |

### Test Cases
| Test | Expected |
|---|---|
| First request with key | Processed normally, `201 Created` |
| Retry with same key | Returns original response, not processed again |
| Same key, different body | `422` or original response (check spec) |
| No idempotency key on payment | Should be rejected or handled carefully |
| Network failure + retry simulation | No duplicate created |

---

## Quick Reference — Advanced REST Parameters

```
Pagination  → ?page=2&limit=10
Filtering   → ?role=admin&status=active
Sorting     → ?sort=name&order=asc
Searching   → ?q=alice
Versioning  → /v1/users  or  /v2/users
Combined    → /v1/users?role=admin&sort=name&order=asc&page=1&limit=20
```
