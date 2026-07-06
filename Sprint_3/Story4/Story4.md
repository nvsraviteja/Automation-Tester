# Sprint 3 — Story 4: Authentication Deep Dive Cheatsheet

---

## Module 1 — Authentication Fundamentals

### Authentication vs Authorization
| | Authentication | Authorization |
|---|---|---|
| Question | Who are you? | What can you do? |
| Proves | Identity | Permission |
| Fails with | `401 Unauthorized` | `403 Forbidden` |

### Auth Types
| Type | How it works |
|---|---|
| Username & Password | Credentials sent → server verifies → grants access |
| Session-based | Server creates a session → stores it → sends session ID via cookie |
| Token-based | Server issues a token → client sends it with every request → stateless |

### Modern Authentication Flow
```
Client → POST /login (credentials)
       ← 200 OK + Access Token + Refresh Token
Client → GET /protected (Authorization: Bearer <token>)
       ← 200 OK + protected data
```

---

## Module 2 — JWT (JSON Web Token)

### Structure
```
Header.Payload.Signature
eyJhbGc...  .  eyJ1c2VyX...  .  SflKxwRJSMeKKF...
```

| Part | Contains | Example |
|---|---|---|
| Header | Algorithm + token type | `{ "alg": "HS256", "typ": "JWT" }` |
| Payload | Claims (user data, expiry) | `{ "userId": 42, "role": "admin", "exp": 1720000000 }` |
| Signature | Verifies token wasn't tampered | `HMACSHA256(header + payload, secret)` |

### Key Points
| Topic | Summary |
|---|---|
| Encoding vs Encryption | JWT is **encoded** (Base64), not encrypted — payload is readable |
| Passwords in JWT | Never store passwords in JWT — payload is visible to anyone |
| Signature purpose | Prevents tampering — if payload is changed, signature breaks |
| Claims | `sub` (subject), `exp` (expiry), `iat` (issued at), `role` |

---

## Module 3 — Access Tokens & Refresh Tokens

### Token Comparison
| | Access Token | Refresh Token |
|---|---|---|
| Purpose | Authenticate API requests | Get a new access token |
| Lifespan | Short (15 min – 1 hr) | Long (days – weeks) |
| Sent with | Every API request | Only to `/refresh` endpoint |
| If stolen | Low risk — expires fast | High risk — store securely |

### Token Refresh Flow
```
Access token expires (401)
  → Client sends Refresh Token to POST /auth/refresh
  → Server validates Refresh Token
  → Issues new Access Token (+ optionally new Refresh Token)
```

### Logout & Revocation
| Scenario | What happens |
|---|---|
| Logout | Refresh token invalidated on server |
| Logout from all devices | All refresh tokens for that user invalidated |
| Password change | All existing tokens invalidated — re-login required |
| Token revocation | Server marks token as invalid before its natural expiry |

---

## Module 4 — OAuth 2.0

### What is OAuth?
Allows users to grant third-party apps access to their data **without sharing their password**.

### Login with Google Flow
```
User clicks "Login with Google"
  → App redirects to Google consent screen
  → User approves requested permissions
  → Google issues an auth code to the app
  → App exchanges code for access token
  → App uses token to access user data
```

### Key Principles
| Concept | Summary |
|---|---|
| No password shared | Third-party app never receives your Google/Facebook password |
| User consent | User explicitly approves what data the app can access |
| Least privilege | App should request only the permissions it actually needs |

### OAuth Test Scenarios
| Test | Expected |
|---|---|
| Valid OAuth login | 200 + token |
| User denies consent | App handles denial gracefully |
| Request excessive permissions | Should be rejected / user warned |
| Invalid auth code | 400 / 401 |

---

## Module 5 — RBAC (Role-Based Access Control)

### Example Roles
| Role | Permissions |
|---|---|
| Player | Read own profile, play game |
| Moderator | Read all profiles, ban users |
| Admin | Full access — create, update, delete anything |

### Permission Matrix Example
| Action | Player | Moderator | Admin |
|---|---|---|---|
| View own profile | ✅ | ✅ | ✅ |
| View all users | ❌ | ✅ | ✅ |
| Ban a user | ❌ | ✅ | ✅ |
| Delete a user | ❌ | ❌ | ✅ |

### Authorization Testing
| Test | Expected |
|---|---|
| Player accesses admin endpoint | `403 Forbidden` |
| Moderator performs admin action | `403 Forbidden` |
| Admin accesses all endpoints | `200 OK` |
| No token sent | `401 Unauthorized` |

---

## Module 6 — API Security Concepts

| Threat | Description | Example |
|---|---|---|
| Bearer Token Theft | Stolen token used to impersonate user | Attacker uses token from intercepted request |
| Token Tampering | Modifying JWT payload to escalate privileges | Change `"role": "user"` → `"role": "admin"` |
| JWT Payload Modification | Payload is editable if signature not verified | Server must always verify signature |
| BOLA | Broken Object Level Authorization — accessing other users' objects | `GET /users/43` with user 42's token |
| IDOR | Insecure Direct Object Reference — guessing IDs to access other records | Change `orderId=101` to `orderId=102` |

### JWT Security Best Practices
- Always verify the signature server-side
- Use short access token expiry
- Store refresh tokens securely (HttpOnly cookie)
- Never store sensitive data (passwords, card numbers) in JWT payload
- Rotate refresh tokens on each use

---

## Module 7 — Authentication Testing

### Positive Tests
| Test | Expected |
|---|---|
| Valid username + password | `200 OK` + access token + refresh token |
| Valid OAuth login | `200 OK` + token |
| Valid token on protected route | `200 OK` + data |

### Negative Tests
| Test | Expected |
|---|---|
| Wrong password | `401 Unauthorized` |
| Non-existent user | `401 Unauthorized` |
| Missing token | `401 Unauthorized` |
| Invalid / malformed token | `401 Unauthorized` |
| Expired access token | `401 Unauthorized` |
| Expired refresh token | `401 Unauthorized` |
| Corrupted refresh token | `400` or `401` |

### Security Tests
| Test | What to verify |
|---|---|
| JWT tampering | Modified token rejected — `401` |
| Token replay | Revoked token cannot be reused |
| Logout | Refresh token invalidated — cannot get new access token |
| Logout all devices | All sessions invalidated |
| Password change | Old tokens rejected after password change |
| OAuth permission denied | App handles denial without crashing |
| BOLA | User A cannot access User B's resources with own token |
| RBAC | Lower role cannot access higher role endpoints |
| SQL Injection | `' OR '1'='1` in login fields → should not bypass auth |

### Bug Reporting Checklist
| Before raising a defect | Check |
|---|---|
| Confirm request is correct | Right URL, headers, body |
| Reproduce consistently | Not a one-off fluke |
| Check expected behaviour | Is it documented in requirements? |
| Include evidence | Request + response screenshots / logs |
| State the impact | What security risk does this create? |

---

## Quick Reference — Status Codes in Auth
| Code | Meaning in Auth context |
|---|---|
| `200` | Login successful |
| `201` | User registered successfully |
| `400` | Malformed request / invalid token format |
| `401` | Not authenticated — missing, invalid, or expired token |
| `403` | Authenticated but not authorized for this action |
| `409` | Email / username already exists |
