# Sprint 2 — Story 1: Advanced Functions

## Today's Agenda
1. `*args`
2. `**kwargs`
3. Lambda Functions
4. Nested Functions
5. Decorators

---

## 1. `*args` — Variable-Length Positional Arguments

`*args` allows a function to accept **any number of positional arguments**. Inside the function, `args` is a tuple containing all the extra positional values passed in.

### Why use it?
Sometimes you don't know in advance how many arguments the caller will pass. `*args` lets your function stay flexible.

### Syntax & Example

```python
def add_numbers(*args):
    print(type(args))   # <class 'tuple'>
    return sum(args)

print(add_numbers(1, 2, 3))        # 6
print(add_numbers(5, 10, 15, 20))  # 50
print(add_numbers())               # 0
```

### Key Points
- The `*` is what matters, not the name `args` (you could call it `*values`, `*numbers`, etc.).
- `*args` must come **after** regular positional parameters in the function definition.
- You can also "unpack" a list/tuple into a function call using `*`:

```python
nums = [1, 2, 3, 4]
print(add_numbers(*nums))  # unpacks to add_numbers(1, 2, 3, 4)
```

---

## 2. `**kwargs` — Variable-Length Keyword Arguments

`**kwargs` allows a function to accept **any number of keyword (named) arguments**. Inside the function, `kwargs` is a dictionary of those key-value pairs.

### Why use it?
Useful when you want to pass named, optional data to a function without defining every possible parameter upfront.

### Syntax & Example

```python
def print_user_info(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_info(name="Alice", age=25, city="Hyderabad")
# name: Alice
# age: 25
# city: Hyderabad
```

### Key Points
- `**kwargs` must come **after** `*args` if both are used together.
- You can unpack a dictionary into a function call using `**`:

```python
details = {"name": "Bob", "age": 30}
print_user_info(**details)
```

### Combining Everything — Order Matters

```python
def example(a, b, *args, **kwargs):
    print(a, b, args, kwargs)

example(1, 2, 3, 4, x=10, y=20)
# 1 2 (3, 4) {'x': 10, 'y': 20}
```

The required order in a function definition is:
**`normal args → *args → default args → **kwargs`**

---

## 3. Lambda Functions

A **lambda function** is a small, anonymous (unnamed) function defined using the `lambda` keyword instead of `def`. It can take any number of arguments but can only contain **one expression**.

### Syntax

```python
lambda arguments: expression
```

### Examples

```python
square = lambda x: x * x
print(square(5))  # 25

add = lambda a, b: a + b
print(add(3, 4))  # 7
```

### Common Use Cases
Lambdas are most useful when you need a quick, throwaway function — often passed as an argument to another function like `map()`, `filter()`, or `sorted()`.

```python
numbers = [1, 2, 3, 4, 5]

# With map()
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# With filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# With sorted()
students = [("Alice", 25), ("Bob", 20), ("Carol", 23)]
sorted_students = sorted(students, key=lambda s: s[1])
print(sorted_students)  # [('Bob', 20), ('Carol', 23), ('Alice', 25)]
```

### Key Points
- No `return` statement needed — the expression's result is returned automatically.
- Best for short, simple operations. For anything complex, use a regular `def` function for readability.

---

## 4. Nested Functions

A **nested function** (or inner function) is a function defined inside another function. The inner function is local to the outer function and can access the outer function's variables (this is part of what enables **closures**).

### Syntax & Example

```python
def outer_function(message):
    def inner_function():
        print(f"Inner says: {message}")
    inner_function()  # called from within outer

outer_function("Hello!")
# Inner says: Hello!
```

### Why use nested functions?
- **Encapsulation** — hide helper logic that's only relevant inside one function.
- **Closures** — the inner function "remembers" variables from the outer function's scope even after the outer function finishes executing.

### Closure Example

```python
def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier  # returns the inner function itself

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

Here, `double` and `triple` are functions that "remember" the `factor` value (2 and 3) from when they were created. This memory is the essence of a closure.

### Key Points
- Inner functions are not accessible from outside the outer function (unless returned, like above).
- Use the `nonlocal` keyword if you need to modify an outer function's variable from within the inner function.

```python
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter1 = counter()
print(counter1())  # 1
print(counter1())  # 2
```

---

## 5. Decorators

A **decorator** is a function that takes another function as input, adds some extra functionality to it, and returns a new function — **without modifying the original function's code**.

Decorators rely heavily on the concepts above: nested functions, closures, and `*args`/`**kwargs`.

### The Building Block

```python
def my_decorator(func):
    def wrapper():
        print("Something before the function runs")
        func()
        print("Something after the function runs")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()
# Something before the function runs
# Hello!
# Something after the function runs
```

### The `@` Syntax (Syntactic Sugar)

Python gives us a cleaner way to apply decorators using `@`:

```python
def my_decorator(func):
    def wrapper():
        print("Something before the function runs")
        func()
        print("Something after the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Same output as above
```

`@my_decorator` above `say_hello()` is exactly equivalent to writing `say_hello = my_decorator(say_hello)`.

### Handling Functions with Arguments

Real functions often take arguments, so decorators typically use `*args` and `**kwargs` to stay generic and work with **any** function signature:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

add(3, 5)
# Calling add with (3, 5), {}
# add returned 8
```

### Practical Use Cases
- **Logging** — record when functions are called and with what arguments.
- **Timing** — measure how long a function takes to execute.
- **Authentication/Authorization** — check permissions before running a function.
- **Caching** — store results of expensive function calls.

### Example: A Timing Decorator

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    print("Done sleeping")

slow_function()
# Done sleeping
# slow_function took 1.0002 seconds
```

### Key Points
- Decorators are applied **top to bottom** when stacked:

```python
@decorator_one
@decorator_two
def my_func():
    pass
# Equivalent to: my_func = decorator_one(decorator_two(my_func))
```

- Use `functools.wraps` to preserve the original function's name and docstring when writing decorators:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

---

## Summary Table

| Topic | Purpose | Key Symbol |
|---|---|---|
| `*args` | Accept variable number of positional arguments | `*` |
| `**kwargs` | Accept variable number of keyword arguments | `**` |
| Lambda | Create small, anonymous, single-expression functions | `lambda` |
| Nested Functions | Define a function inside another; enables closures | — |
| Decorators | Wrap a function to extend/modify its behavior | `@` |
