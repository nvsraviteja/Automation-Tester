# SQL Cheat Sheet — Sprint 6, Story 8
### Topic: Views

---

## 1. What is a View?

A **View** is a **virtual table** based on the result of a stored `SELECT` query. It doesn't store data itself — it stores the query definition, and the data is fetched fresh from the underlying table(s) every time the view is queried.

```sql
CREATE VIEW ITEmployees AS
SELECT EmpID, EmpName, Salary
FROM Employee
WHERE DeptID = 10;
```

---

## 2. Virtual Table vs Physical Table

| Aspect | Physical Table | View (Virtual Table) |
|---|---|---|
| Data storage | Stores actual data on disk | Stores only the query definition |
| Data freshness | Data as it was last written | Always reflects current underlying table data |
| Space usage | Takes storage space | Takes negligible space (just the query) |
| Creation | `CREATE TABLE` | `CREATE VIEW` |
| Independence | Exists on its own | Depends on one or more base tables |

**Key point:** A view is like a **saved, reusable query** — it looks and behaves like a table when you query it, but there's no separate copy of the data sitting behind it.

---

## 3. Creating a View (`CREATE VIEW`)

```sql
CREATE VIEW HighEarners AS
SELECT EmpID, EmpName, Salary, DeptID
FROM Employee
WHERE Salary > 55000;
```

**Key points**
- Can include `JOIN`s, `WHERE`, `GROUP BY`, aggregate functions, etc. — anything a normal `SELECT` supports.
```sql
CREATE VIEW DeptSummary AS
SELECT d.DeptName, COUNT(e.EmpID) AS TotalEmployees, AVG(e.Salary) AS AvgSalary
FROM Department d
JOIN Employee e ON d.DeptID = e.DeptID
GROUP BY d.DeptName;
```

---

## 4. Querying a View

A view is queried exactly like a regular table.

```sql
SELECT * FROM HighEarners;

SELECT EmpName FROM HighEarners WHERE DeptID = 10;

SELECT * FROM DeptSummary ORDER BY AvgSalary DESC;
```

**Key point:** You can apply further `WHERE`, `ORDER BY`, `JOIN`, etc. on top of a view, just like on a table.

---

## 5. Why Views are Used

### a) Security
Views can expose only **specific columns/rows**, hiding sensitive data (e.g., salary, SSN) from users who only need limited access.

```sql
CREATE VIEW PublicEmployeeInfo AS
SELECT EmpID, EmpName, Department
FROM Employee;
-- Salary and other sensitive columns are never exposed through this view
```

### b) Simplicity
Complex joins/aggregations can be wrapped into a single view, so users/apps just query the view instead of rewriting the complex logic every time.

```sql
-- Instead of repeating this complex JOIN everywhere:
SELECT e.EmpName, d.DeptName, e.Salary
FROM Employee e JOIN Department d ON e.DeptID = d.DeptID;

-- Just create it once as a view, then reuse:
CREATE VIEW EmployeeDeptView AS
SELECT e.EmpName, d.DeptName, e.Salary
FROM Employee e JOIN Department d ON e.DeptID = d.DeptID;

SELECT * FROM EmployeeDeptView;
```

### c) Reusability
The same view can be reused across multiple reports, queries, or applications without duplicating the underlying logic.

---

## 6. Dynamic Nature of Views

A view **always reflects the current data** in the underlying table(s) — it's not a static snapshot.

```sql
-- If Employee table gets updated...
UPDATE Employee SET Salary = 70000 WHERE EmpID = 101;

-- ...the view immediately reflects the change on next query, no refresh needed
SELECT * FROM HighEarners;
```

**Key point:** Every time you `SELECT` from a view, the underlying query re-executes against the live base table(s) — there's no stale/cached data (unless it's specifically a **materialized view**, which is a different concept that does store a physical snapshot).

---

## 7. Inserting into a View

You **can** insert into a view in some cases, but the insert actually affects the **underlying base table**.

```sql
INSERT INTO PublicEmployeeInfo (EmpID, EmpName, Department)
VALUES (110, 'Sana', 'IT');
```

**Key point:** This only works if the view is based on a **single table** and includes all `NOT NULL` columns of that table (either directly or via defaults) — otherwise the insert fails.

---

## 8. Updating Through a View (Restrictions)

```sql
UPDATE PublicEmployeeInfo
SET Department = 'HR'
WHERE EmpID = 110;
```

**Restrictions on updatable views — update generally FAILS or is disallowed if the view contains:**
- Aggregate functions (`COUNT`, `SUM`, `AVG`, `MAX`, `MIN`)
- `GROUP BY` or `HAVING`
- `DISTINCT`
- `JOIN`s across multiple tables (in most RDBMS, though some allow limited cases)
- `UNION` or `UNION ALL`
- Subqueries in the `SELECT` list

---

## 9. Updatable vs Non-Updatable Views

| Aspect | Updatable View | Non-Updatable View |
|---|---|---|
| Based on | Single table, simple `SELECT` | Joins, aggregates, `GROUP BY`, `DISTINCT`, `UNION` |
| Insert/Update/Delete | Allowed (with restrictions) | Not allowed |
| Example | `SELECT EmpID, EmpName FROM Employee` | `SELECT DeptID, COUNT(*) FROM Employee GROUP BY DeptID` |

**Key point:** As a rule of thumb — the **simpler** the view's query, the more likely it is to be updatable. Anything involving aggregation or multiple tables is generally **read-only**.

---

## 10. Replacing/Modifying a View (`CREATE OR REPLACE VIEW`)

Instead of dropping and recreating a view, you can redefine it directly.

```sql
CREATE OR REPLACE VIEW HighEarners AS
SELECT EmpID, EmpName, Salary, DeptID
FROM Employee
WHERE Salary > 60000;   -- changed threshold from 55000 to 60000
```

**Key point:** `CREATE OR REPLACE VIEW` avoids the need to manually `DROP VIEW` first — it updates the view definition in place, preserving any granted permissions on it (in most RDBMS).

---

## 11. Deleting a View (`DROP VIEW`)

```sql
DROP VIEW HighEarners;

-- Safer version - doesn't error if the view doesn't exist
DROP VIEW IF EXISTS HighEarners;
```

**Key point:** `DROP VIEW` removes only the view definition — the underlying base table and its data are **completely unaffected**.

---

## 12. View vs Table

| Aspect | Table | View |
|---|---|---|
| Stores data | Yes (physically) | No (virtual, except materialized views) |
| Creation | `CREATE TABLE` | `CREATE VIEW` |
| Modifiable structure | `ALTER TABLE` | `CREATE OR REPLACE VIEW` |
| Performance | Direct access, generally faster | Slight overhead (query re-runs each time) |
| Storage space | Uses disk space for data | Minimal (just stores query definition) |
| Insert/Update/Delete | Always allowed | Allowed only if "updatable" |
| Reflects live data | N/A (it IS the data) | Always current |

---

## 13. Real-World QA Use Cases

- **Test data isolation:** Create a view exposing only a safe, filtered subset of production-like data for QA environments (e.g., masking sensitive columns).
- **Simplified validation queries:** Wrap a complex multi-table join used repeatedly in test data validation into a single view, so testers/automation scripts query one simple view instead of rewriting the join each time.
- **Regression checks:** Create a view summarizing key metrics (e.g., order counts, failed transactions) to quickly validate data integrity after a release/deployment.
- **Role-based access in test environments:** Give certain team members/testers access only to a view (not the full table), restricting visibility into sensitive fields like salary or personal data.
- **Consistent reporting baseline:** Use views as a single source of truth for common report queries used across different test scripts, avoiding inconsistent logic across the team.

---

## Quick Reference Table

| Task | Syntax |
|---|---|
| Create view | `CREATE VIEW view_name AS SELECT ...` |
| Query view | `SELECT * FROM view_name` |
| Replace view | `CREATE OR REPLACE VIEW view_name AS SELECT ...` |
| Delete view | `DROP VIEW view_name` / `DROP VIEW IF EXISTS view_name` |
| Insert via view | `INSERT INTO view_name (...) VALUES (...)` (single-table view only) |
| Update via view | `UPDATE view_name SET ... WHERE ...` (only if updatable) |
