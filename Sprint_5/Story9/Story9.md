# Selenium WebDriver — Sprint 5, Story 9 Cheat Sheet
### Topic: WebTable (Static & Dynamic)

Language: **Python + Selenium WebDriver**

---

## 0. What is a WebTable?

A WebTable is an HTML `<table>` made up of:
- `<table>` → the whole table
- `<tr>` → table row
- `<th>` → header cell
- `<td>` → data cell

There's no special Selenium "Table" class — tables are handled purely with locators (`find_element`/`find_elements`) and looping logic.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
```

---

## 1. Static WebTable

A **static table** has a **fixed number of rows and columns** that don't change — data is hardcoded in the HTML. You can locate cells directly using their exact row/column position.

### Example HTML structure
```html
<table id="productTable">
  <tr><th>Name</th><th>Price</th><th>Quantity</th></tr>
  <tr><td>Butter</td><td>3.75</td><td>2</td></tr>
  <tr><td>Milk</td><td>2.99</td><td>1</td></tr>
</table>
```

### Accessing a specific cell (fixed position)

```python
# XPath: row 2, column 1 -> "Milk"
cell = driver.find_element(By.XPATH, "//table[@id='productTable']/tbody/tr[3]/td[1]")
print(cell.text)
```

### Reading the entire static table

```python
table = driver.find_element(By.ID, "productTable")

rows = table.find_elements(By.TAG_NAME, "tr")
print("Total rows:", len(rows))

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    row_data = [col.text for col in cols]
    print(row_data)
```

**Key points**
- Since positions never change, you can safely hardcode `tr[n]/td[n]` in XPath.
- Fragile in real apps only if the table's row/column count changes — but for genuinely static tables this is fine.

---

## 2. Dynamic WebTable

A **dynamic table** has rows/columns that change at runtime — e.g., data loaded from a database, filtered search results, or paginated grids. You **cannot** hardcode row/column indexes reliably; instead, you loop through elements and/or match by data (like a specific product name).

### Example: Counting rows and columns dynamically

```python
table = driver.find_element(By.XPATH, "//table[@id='productTable']")

rows = table.find_elements(By.TAG_NAME, "tr")
print("Total rows:", len(rows))

# Columns in the first row (header)
header_cols = rows[0].find_elements(By.TAG_NAME, "th")
print("Total columns:", len(header_cols))
```

### Example: Finding data by matching a known value (not by fixed index)

```python
rows = driver.find_elements(By.XPATH, "//table[@id='productTable']/tbody/tr")

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    if cols and cols[0].text == "Milk":
        print("Price:", cols[1].text)
        print("Quantity:", cols[2].text)
        break
```

### Example: Dynamic XPath using `contains()`/`text()`

```python
# Find the row containing a cell with text "Milk", then get its price (2nd td)
price = driver.find_element(
    By.XPATH,
    "//table[@id='productTable']//td[text()='Milk']/following-sibling::td[1]"
).text
print("Price:", price)
```

### Example: Summing a numeric column dynamically

```python
rows = driver.find_elements(By.XPATH, "//table[@id='productTable']/tbody/tr")

total = 0
for row in rows:
    price_cell = row.find_elements(By.TAG_NAME, "td")
    if len(price_cell) >= 2:
        total += float(price_cell[1].text)

print("Total price:", total)
```

**Key points**
- Never hardcode `tr[n]` when row count can change — always use `find_elements()` and loop.
- Use `following-sibling`, `text()`, and `contains()` in XPath to locate a cell **relative to known data**, not a fixed position.
- Common real-world use cases: verifying a specific row exists after search/filter, summing/averaging a column, extracting all rows into a list/dict for validation.

---

## Static vs Dynamic — Quick Comparison

| Aspect | Static Table | Dynamic Table |
|---|---|---|
| Row/column count | Fixed | Changes at runtime |
| Locator strategy | Hardcoded `tr[n]/td[n]` OK | Loop with `find_elements()` |
| Data source | Hardcoded in HTML | DB/API driven, filters, pagination |
| XPath style | Absolute/fixed index | `contains()`, `text()`, `following-sibling` |

---

## Assignment / Practice

Practice static and dynamic table handling on:

- 🔗 https://testautomationpractice.blogspot.com/ (has a webtable section — practice both reading fixed cells and looping through rows dynamically)
