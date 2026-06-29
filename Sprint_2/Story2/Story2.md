# Sprint 2 — Story 2: Modules & Importing Modules

## Topics Covered
1. Modules
2. Importing Modules
   - Style 1 — Import whole module
   - Style 2 — Import specific item
   - Difference Between Import Styles
   - Aliasing (`as`)
   - Wildcard Import (Avoid)
   - Circular Imports
3. Packages
4. Package Imports
5. `__init__.py`
6. QA Framework Import Structure

---

## 1. Modules

A **module** is simply a Python file (`.py`) that contains code — functions, classes, variables — that you can reuse in other files. Instead of writing everything in one giant file, you split your code into logical modules and import what you need.

### Example

**`math_utils.py`** (this file is a module)
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

PI = 3.14159
```

Any other Python file can now reuse this code by importing `math_utils`.

### Why use modules?
- **Reusability** — write once, use anywhere.
- **Organization** — group related code together.
- **Maintainability** — easier to debug and update smaller, focused files.
- **Namespacing** — avoids naming conflicts between different parts of a large project.

---

## 2. Importing Modules

To use code from another module, you need to **import** it. Python offers several ways to do this.

### Style 1 — Import Whole Module

```python
import math_utils

result = math_utils.add(5, 3)
print(result)  # 8
print(math_utils.PI)  # 3.14159
```

You access everything using the `module_name.item` syntax. This keeps things explicit — it's always clear where `add` and `PI` came from.

### Style 2 — Import Specific Item

```python
from math_utils import add, PI

result = add(5, 3)
print(result)  # 8
print(PI)       # 3.14159
```

Here you import only the specific function(s) or variable(s) you need, and call them directly — no module prefix required.

### Difference Between Import Styles

| Aspect | `import module_name` | `from module_name import item` |
|---|---|---|
| Usage | `module_name.item` | `item` directly |
| Namespace | Keeps module's namespace separate (safer) | Brings item into current namespace (risk of name clashes) |
| Clarity | Clear where the function/variable came from | Less obvious at the call site |
| Best for | Using many items from a module, or avoiding name conflicts | Using one or two specific items frequently |

**Rule of thumb:** Use `import module_name` for clarity in larger codebases. Use `from module_name import item` when you need just a couple of things and want shorter, cleaner code.

### Aliasing (`as`)

You can rename a module or imported item using `as` — useful for shortening long names or avoiding conflicts.

```python
import math_utils as mu
print(mu.add(2, 3))  # 5

from math_utils import add as add_numbers
print(add_numbers(2, 3))  # 5
```

This is extremely common with well-known libraries:
```python
import pandas as pd
import numpy as np
```

### Wildcard Import (Avoid)

```python
from math_utils import *
```

This imports **everything** from the module directly into your current namespace.

**Why to avoid it:**
- **Name collisions** — if two modules have a function with the same name, the second import silently overwrites the first, causing confusing bugs.
- **Poor readability** — when you see `add(5, 3)` in code, it's unclear which module it came from.
- **Pollutes the namespace** — you might unintentionally import dozens of names you don't need.

```python
# Bad practice
from module_one import *
from module_two import *

# If both modules define a function called 'process()',
# you won't know which one is actually being called.
```

**Best practice:** Always prefer explicit imports (`import module` or `from module import specific_item`).

### Circular Imports

A **circular import** happens when two (or more) modules try to import each other, directly or indirectly, creating a loop.

**Example of the problem:**

**`module_a.py`**
```python
import module_b

def func_a():
    return module_b.func_b()
```

**`module_b.py`**
```python
import module_a

def func_b():
    return module_a.func_a()
```

When Python tries to load `module_a`, it starts importing `module_b`, which in turn tries to import `module_a` again — but `module_a` hasn't finished loading yet. This usually raises an `ImportError` or `AttributeError`.

### How to Avoid/Fix Circular Imports
1. **Restructure code** — move shared logic into a third module that both can import from.
2. **Import inside the function** (delayed/local import) instead of at the top of the file:
   ```python
   def func_a():
       import module_b  # imported only when func_a() runs
       return module_b.func_b()
   ```
3. **Import only what's needed**, using `from module import specific_item`, to reduce the chance of a full circular dependency.
4. **Rethink your design** — circular imports are often a sign that two modules are too tightly coupled and responsibilities should be split differently.

---

