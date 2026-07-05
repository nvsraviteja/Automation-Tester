# API Testing Types — Cheatsheet

---

## Quick Reference

| Type | What it checks |
|---|---|
| Functional | Does the API work as per requirements? |
| Integration | Does the API work with other systems / databases? |
| Load | Does the API handle expected traffic? |
| Stress | What happens when pushed beyond its limits? |
| Security | Is the API protected from unauthorized access? |
| Validation | Does the API follow correct schema / data format? |
| Regression | Did recent changes break existing functionality? |
| Fuzz | How does the API handle random / invalid inputs? |
| Contract | Does the API follow the agreed client-server contract? |
| End-to-End | Does a full workflow across multiple APIs work? |
| Mocking | Can functionality be tested without real services? |

---

## Details

### Functional Testing
- Verifies the API does what it's supposed to do
- Checks correct responses for valid inputs
- Example: `POST /login` with valid credentials → 200 + token

### Integration Testing
- Verifies the API works with connected systems (DBs, third-party services)
- Example: Creating a user via API → check the record appears in the database

### Load Testing
- Tests performance under **expected** user traffic
- Checks response times and stability under normal load
- Example: 500 concurrent users hitting `GET /products`

### Stress Testing
- Pushes the API **beyond its limits** to find breaking points
- Example: 10,000 concurrent requests — when does it fail? How does it fail?

### Security Testing
- Checks for unauthorized access, data leaks, injection attacks
- Example: Accessing another user's data with your token → should return 403

### Validation Testing
- Confirms response matches expected schema, data types, and required fields
- Example: Response always contains `id`, `name`, `email` — none are null or missing

### Regression Testing
- Ensures new changes don't break what already worked
- Example: After a bug fix, re-run all existing test cases to confirm nothing broke

### Fuzz Testing
- Sends random, malformed, or unexpected inputs
- Checks the API doesn't crash or expose sensitive errors
- Example: Sending `null`, empty strings, huge payloads, or special characters in every field

### Contract Testing
- Validates the API matches the agreed spec between client and server
- Example: Frontend expects `{ "userId": int }` — API must always return exactly that

### End-to-End Testing
- Tests a complete business workflow across multiple APIs
- Example: Register → Login → Place Order → Check Order Status

### Mocking / Simulation Testing
- Uses a fake (mock) server instead of the real one
- Useful when the real API isn't ready yet or is unstable
- Example: Mock the payment API to test checkout flow without real transactions

---

## When to Use What

| Scenario | Testing Type |
|---|---|
| Verifying a new endpoint works | Functional |
| Checking DB gets updated after an API call | Integration |
| Measuring performance before release | Load |
| Finding the failure point under extreme traffic | Stress |
| Checking if auth is properly enforced | Security |
| Validating response structure matches the spec | Validation |
| After a bug fix or new feature merge | Regression |
| Checking how the API handles garbage input | Fuzz |
| Ensuring frontend and backend stay in sync | Contract |
| Testing a full user journey | End-to-End |
| Testing when a dependency isn't available | Mocking |
