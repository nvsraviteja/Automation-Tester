# Sprint 4 — Story 2: Pytest Cheatsheet

---

## Setup

```bash
pip install pytest
pytest --version
```

---

## Test Functions

- Every test function must start with `test_`
- Uses plain `assert` statements — no special methods needed
- One test function = one behaviour being verified

```python
def test_addition():
    assert 1 + 1 == 2

def test_string_upper():
    assert "hello".upper() == "HELLO"
```

---

## Assertions

| Assertion | Example |
|---|---|
| Equality | `assert response.status_code == 200` |
| Not equal | `assert result != 0` |
| True / False | `assert response.ok` / `assert not response.ok` |
| In / not in | `assert "token" in response.json()` |
| Greater / less | `assert response.elapsed.total_seconds() < 2` |
| None check | `assert response is not None` |
| Type check | `assert isinstance(data["id"], int)` |

### Custom Failure Message
```python
assert response.status_code == 200, f"Expected 200, got {response.status_code}"
```

---

## Fixtures

Fixtures provide **reusable setup** for tests — run before (and optionally after) each test.

```python
import pytest

@pytest.fixture
def base_url():
    return "https://api.example.com"

@pytest.fixture
def auth_headers():
    return {"Authorization": "Bearer test_token_123"}

def test_get_user(base_url, auth_headers):
    response = requests.get(f"{base_url}/users/1", headers=auth_headers)
    assert response.status_code == 200
```

### Fixture Scopes
| Scope | Runs once per… | Use for |
|---|---|---|
| `function` (default) | Each test function | Fresh data per test |
| `class` | Each test class | Shared setup for grouped tests |
| `module` | Each test file | Module-level setup |
| `session` | Entire test run | DB connection, browser launch |

```python
@pytest.fixture(scope="session")
def db_connection():
    conn = create_connection()
    yield conn        # ← code after yield runs as teardown
    conn.close()
```

### Yield Fixtures (Setup + Teardown)
```python
@pytest.fixture
def browser():
    driver = webdriver.Chrome()   # setup
    yield driver                  # test runs here
    driver.quit()                 # teardown — always runs
```

---

## Parametrization

Run the **same test with multiple inputs** — no code duplication.

```python
import pytest

@pytest.mark.parametrize("username, password, expected", [
    ("alice", "correct_pass", 200),
    ("alice", "wrong_pass",   401),
    ("",      "any_pass",     400),
])
def test_login(username, password, expected):
    response = requests.post(
        "https://api.example.com/login",
        json={"username": username, "password": password}
    )
    assert response.status_code == expected
```

- Each tuple = one test case
- Pytest runs the function once per tuple
- Shows up as separate test results in the report

---

## Markers

Markers **tag** tests so you can run specific groups.

### Built-in Markers
| Marker | Purpose |
|---|---|
| `@pytest.mark.skip` | Always skip this test |
| `@pytest.mark.skipif(condition, reason="...")` | Skip if condition is true |
| `@pytest.mark.xfail` | Expected to fail — won't count as a failure |
| `@pytest.mark.parametrize` | Run test with multiple inputs |

### Custom Markers
```python
# In conftest.py or pytest.ini
# pytest.ini:
# [pytest]
# markers =
#     smoke: smoke tests
#     regression: regression tests
#     auth: authentication tests

@pytest.mark.smoke
def test_login_valid():
    ...

@pytest.mark.regression
def test_login_invalid():
    ...
```

### Running by Marker
```bash
pytest -m smoke           # run only smoke tests
pytest -m "not regression" # run everything except regression
pytest -m "smoke and auth"  # run tests with both markers
```

---

## Test Discovery

Pytest automatically finds tests using these rules:

| Rule | Example |
|---|---|
| Files named `test_*.py` or `*_test.py` | `test_login.py`, `auth_test.py` |
| Functions starting with `test_` | `def test_valid_login():` |
| Classes starting with `Test` | `class TestLogin:` |
| Methods starting with `test_` inside Test classes | `def test_invalid_password(self):` |

### conftest.py
- Special file Pytest recognises automatically
- Place shared fixtures here — available to all tests in the same folder and subfolders
- No import needed

```
qa_framework/
├── conftest.py          ← shared fixtures (base_url, headers, driver)
├── tests/
│   ├── test_login.py
│   └── test_users.py
```

---

## Running Test Suites

```bash
pytest                          # run all tests in current directory
pytest tests/                   # run all tests in tests/ folder
pytest tests/test_login.py      # run one specific file
pytest tests/test_login.py::test_valid_login   # run one specific test

pytest -v                       # verbose — show each test name + result
pytest -s                       # show print() output during tests
pytest -v -s                    # both

pytest -m smoke                 # run tests tagged with @pytest.mark.smoke
pytest -k "login"               # run tests whose name contains "login"
pytest --tb=short               # shorter traceback on failure
pytest -x                       # stop after first failure
pytest --maxfail=3              # stop after 3 failures
```

### With Allure Reporting
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

## Quick Reference — Typical Project Structure

```
qa_framework/
├── conftest.py              ← shared fixtures
├── pytest.ini               ← markers, settings
├── requirements.txt
└── tests/
    ├── test_auth.py
    ├── test_users.py
    └── test_orders.py
```

### `pytest.ini`
```ini
[pytest]
markers =
    smoke: smoke test suite
    regression: regression test suite
    auth: authentication tests
```

---

## Summary

| Concept | Purpose |
|---|---|
| `test_` prefix | Pytest discovers and runs the function as a test |
| `assert` | Validates expected vs actual — fails the test if false |
| Fixtures | Reusable setup/teardown — injected via function parameters |
| `yield` in fixture | Code before = setup, code after = teardown |
| `parametrize` | One test function, multiple input sets |
| Markers | Tag and group tests — run subsets with `-m` |
| `conftest.py` | Shared fixtures available across all test files |
| `-v` flag | Verbose output — see every test name and status |
| `-x` flag | Stop on first failure — useful for debugging |
