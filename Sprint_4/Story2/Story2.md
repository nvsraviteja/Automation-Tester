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
