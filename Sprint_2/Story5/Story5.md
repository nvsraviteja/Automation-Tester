# Sprint 2 — Story 5: `pip` & Virtual Environments (`venv`)

## Topics Covered
1. What is `pip`
2. Why `pip` is Needed
3. Installing Python Packages (`pip install package_name`)
4. Common QA Libraries
5. What is a Virtual Environment (`venv`)
6. Why `venv` is Needed
7. Creating a Virtual Environment
8. Activating a Virtual Environment
9. Installing Packages Inside `venv`
10. `requirements.txt`
11. Installing from Requirements File
12. Typical QA Project Setup Flow
13. `pip` + `venv` in QA Framework Usage

---

## 1. What is `pip`

**`pip`** stands for **"Pip Installs Packages"**. It is Python's official **package manager** — a command-line tool used to install, upgrade, and remove third-party Python libraries and frameworks.

`pip` comes bundled with Python (3.4+) by default, so you typically don't need to install it separately.

```bash
pip --version
```

```
pip 24.0 from /usr/lib/python3/dist-packages/pip (python 3.12)
```

---

## 2. Why `pip` is Needed

Python's built-in functionality (the "standard library") covers a lot, but real-world projects almost always need extra functionality that isn't built in — things like browser automation, HTTP requests, data analysis, or testing frameworks.

### Why `pip` matters:
- **Access to a massive ecosystem** — the [Python Package Index (PyPI)](https://pypi.org) hosts hundreds of thousands of community and officially maintained packages.
- **Saves time** — instead of writing complex functionality (like browser automation) from scratch, you install a library that already does it well.
- **Easy version management** — install specific versions, upgrade, or remove packages with simple commands.
- **Standardized installs** — anyone on your team can install the exact same dependencies your project needs, ensuring consistency.

---

## 3. Installing Python Packages

### `pip install package_name`

```bash
pip install requests
```

This downloads the `requests` package from PyPI and installs it so it can be imported in your Python code:

```python
import requests

response = requests.get("https://example.com")
print(response.status_code)
```

### Other Common `pip` Commands

```bash
pip install package_name==2.31.0     # install a specific version
pip install --upgrade package_name   # upgrade to the latest version
pip uninstall package_name           # remove a package
pip list                             # list all installed packages
pip show package_name                # show details about a package (version, location, dependencies)
```

---

## 4. Common QA Libraries

These are some of the most widely used Python packages in test automation and QA work:

### `selenium`
The most popular library for **browser automation** — controlling web browsers programmatically to test web applications (clicking buttons, filling forms, navigating pages).

```bash
pip install selenium
```

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")
```

### `pytest`
A powerful and widely used **testing framework** for writing and running test cases. It supports simple `assert` statements, fixtures, parametrized tests, and detailed test reports.

```bash
pip install pytest
```

```python
# test_sample.py
def test_addition():
    assert 1 + 1 == 2
```

```bash
pytest test_sample.py
```

### `requests`
A simple, widely-used library for making **HTTP requests** — essential for **API testing**.

```bash
pip install requests
```

```python
import requests

response = requests.get("https://api.example.com/users")
print(response.json())
```

### `allure-pytest`
A plugin that integrates **Allure reporting** with `pytest`, generating detailed, visually rich **HTML test reports** (steps, screenshots, pass/fail trends, attachments).

```bash
pip install allure-pytest
```

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 5. What is a Virtual Environment (`venv`)

A **virtual environment** is an **isolated, self-contained Python environment** for a specific project. It has its own Python interpreter and its own set of installed packages, completely separate from your system's global Python installation and from other projects.

Think of it as giving each project its **own private toolbox** of packages, instead of sharing one toolbox across every project on your machine.

`venv` is a module built into Python (3.3+) used to create these isolated environments.

---

## 6. Why `venv` is Needed

### Dependency Isolation
Different projects often need different packages — or different **versions** of the same package. A virtual environment keeps each project's dependencies separate, so installing something for one project never affects another.

```
Project A (venv_A) → selenium 4.10, pytest 7.4
Project B (venv_B) → selenium 4.20, pytest 8.0
```

Without isolation, both projects would be forced to share whatever versions are installed globally — which can easily cause conflicts.

### Version Conflict Prevention
Imagine:
- **Project A** requires `selenium==4.10` (because of compatibility with older code).
- **Project B** requires `selenium==4.20` (to use a newer feature).

If both projects installed packages **globally** (system-wide), installing `selenium==4.20` for Project B would **overwrite** the version Project A needs — breaking Project A.

With separate virtual environments, **each project gets the exact version it needs**, with zero conflicts.

### Additional Benefits
- **Reproducibility** — anyone can recreate the exact same environment using a `requirements.txt` file (covered below).
- **Clean system** — keeps your global Python installation free of clutter from every project you've ever worked on.
- **Safe experimentation** — you can install/remove packages freely inside a venv without risking your system-wide Python setup.

---

## 7. Creating a Virtual Environment

### `python -m venv venv`

```bash
python -m venv venv
```

**Breaking this command down:**
- `python` — runs the Python interpreter.
- `-m venv` — runs the built-in `venv` module.
- The second `venv` — the **name** of the folder that will be created to hold the virtual environment (by convention, often named `venv`, but it could be anything, e.g. `env` or `.venv`).

After running this, you'll see a new folder structure like:

```
my_project/
│
├── venv/
│   ├── bin/        (or Scripts/ on Windows)
│   ├── lib/
│   └── pyvenv.cfg
│
└── main.py
```

This `venv` folder contains its own copy of the Python interpreter and will hold any packages you install while it's active.

> **Tip:** Add `venv/` to your project's `.gitignore` file — it shouldn't be committed to version control since it's specific to each machine and can be recreated anytime using `requirements.txt`.

---

## 8. Activating a Virtual Environment

Creating a venv isn't enough — you need to **activate** it so that `pip install` and `python` commands use the venv's isolated environment instead of your system-wide Python.

### Windows Activation

```bash
venv\Scripts\activate
```

### Mac/Linux Activation

```bash
source venv/bin/activate
```

### How to Know It's Active
Once activated, your terminal prompt typically shows the environment name in parentheses:

```bash
(venv) C:\my_project>
```
or
```bash
(venv) user@machine:~/my_project$
```

### Deactivating

```bash
deactivate
```

This returns you to your system's global Python environment.

---

## 9. Installing Packages Inside `venv`

Once the virtual environment is **activated**, any `pip install` command installs packages **only inside that venv** — not globally.

```bash
# Activate first
source venv/bin/activate   # Mac/Linux
# or
venv\Scripts\activate       # Windows

# Now install packages — they go into venv, not the global Python
pip install selenium pytest requests allure-pytest
```

You can confirm installed packages are isolated to the venv:

```bash
pip list
```

```
Package         Version
---------------- -------
selenium         4.20.0
pytest           8.0.0
requests         2.31.0
allure-pytest     2.13.5
```

If you `deactivate` and run `pip list` again, you'll see your system's global packages instead — confirming the venv's packages are truly separate.

---

## 10. `requirements.txt`

A **`requirements.txt`** file is a plain text file that lists all the Python packages (and optionally their exact versions) that a project depends on. It allows anyone — teammates, CI/CD pipelines, or future you — to recreate the exact same environment with one command.

### Example `requirements.txt`

```
selenium==4.20.0
pytest==8.0.0
requests==2.31.0
allure-pytest==2.13.5
```

### Generating It Automatically
Instead of writing it by hand, you can generate it from your currently installed (activated) packages:

```bash
pip freeze > requirements.txt
```

`pip freeze` outputs all installed packages with their exact versions, and `>` redirects that output into the `requirements.txt` file.

### Why It Matters
- **Consistency** — everyone on the team installs the exact same package versions, avoiding "it works on my machine" issues.
- **Onboarding** — new team members can set up the project in seconds.
- **CI/CD pipelines** — automated build/test servers use it to install dependencies before running tests.
- **Version control friendly** — unlike the `venv` folder itself, `requirements.txt` is small, readable, and meant to be committed to Git.

---

## 11. Installing from Requirements File

### `pip install -r requirements.txt`

```bash
pip install -r requirements.txt
```

**Breaking this down:**
- `-r` — tells `pip` to read package names (and versions) from a **requirements file** rather than typing them individually.
- `requirements.txt` — the file containing the list of packages.

This single command installs **every package listed in the file**, at the specified versions — exactly recreating the intended environment.

```bash
# Typical flow when setting up a project from scratch
python -m venv venv
source venv/bin/activate          # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 12. Typical QA Project Setup Flow

When joining a QA automation project (or setting one up fresh), the standard setup sequence looks like this:

### Step 1 — Clone the Repository
```bash
git clone https://github.com/example-team/qa-framework.git
cd qa-framework
```

### Step 2 — Create and Activate the Virtual Environment
```bash
python -m venv venv

# Activate it:
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate          # Windows
```

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Run Tests
```bash
pytest tests/
```

Or, with Allure reporting:
```bash
pytest --alluredir=allure-results
allure serve allure-results
```

### Why Following This Exact Flow Matters
- Skipping venv activation means packages might install **globally** instead of into the isolated environment — defeating the whole purpose of isolation.
- Skipping `requirements.txt` installation could mean missing dependencies, causing `ModuleNotFoundError` (see Story 4!) when running tests.
- This flow is **repeatable** — any team member, or any CI/CD server, can follow these exact same four steps and get an identical, working environment.

---

## 13. `pip` + `venv` in QA Framework Usage

In a real QA automation project, `pip` and `venv` work together to keep the entire framework's dependencies clean, isolated, and reproducible across every developer's machine and every CI/CD pipeline run.

### Typical Project Structure

```
qa_framework/
│
├── venv/                    # virtual environment (NOT committed to Git)
├── requirements.txt         # list of all dependencies
├── .gitignore                # excludes venv/ from version control
│
├── pages/
├── tests/
├── utils/
└── reports/
```

### `.gitignore` Entry
```
venv/
__pycache__/
*.pyc
```

### CI/CD Pipeline Example (Conceptual)
Most CI/CD systems (GitHub Actions, Jenkins, GitLab CI) follow the same pattern programmatically:

```yaml
# Simplified example (e.g., GitHub Actions step)
- name: Set up Python environment
  run: |
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

- name: Run tests
  run: |
    source venv/bin/activate
    pytest tests/ --alluredir=allure-results
```

This ensures that **every test run** — whether on a developer's laptop or an automated build server — uses the exact same package versions, eliminating "works on my machine but fails in CI" problems.

### Why This Matters for QA
- **Consistency across environments** — local machines, teammates' machines, and CI/CD servers all run tests against identical dependency versions.
- **Easy onboarding** — a new QA engineer can be up and running with four simple commands (clone → venv → install → test).
- **Safe upgrades** — you can test a new version of `selenium` inside the venv without affecting any other project on the same machine.
- **Clean version control** — only `requirements.txt` (small, readable) is committed; the bulky `venv/` folder is excluded and can always be regenerated.

---

## Summary Table

| Concept | Command / Purpose |
|---|---|
| `pip` | Python's package manager — installs/manages third-party libraries |
| `pip install package_name` | Installs a specific package from PyPI |
| Common QA libraries | `selenium` (browser automation), `pytest` (testing framework), `requests` (API calls), `allure-pytest` (reporting) |
| Virtual Environment (`venv`) | Isolated, project-specific Python environment |
| Why `venv` is needed | Dependency isolation; prevents version conflicts between projects |
| `python -m venv venv` | Creates a new virtual environment |
| Activation | `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows) |
| Installing inside `venv` | `pip install` while activated — packages stay isolated to the project |
| `requirements.txt` | Text file listing all project dependencies and versions |
| `pip install -r requirements.txt` | Installs everything listed in the requirements file |
| QA setup flow | Clone repo → activate venv → install dependencies → run tests |
| `pip` + `venv` in QA | Ensures consistent, reproducible environments across team members and CI/CD pipelines |
