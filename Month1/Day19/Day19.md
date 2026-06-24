# Python OOP Cheat Sheet (QA Automation Focus)

## 1. What is OOP?
OOP stands for **Object-Oriented Programming**.

It organizes code using:
- Objects
- Classes
- Attributes
- Methods

### QA Examples
- LoginPage
- DashboardPage
- Browser
- User
- TestSuite

## 2. Why OOP?
With OOP:
- Better structure
- Reusable code
- Easier maintenance
- Scalable automation frameworks

## 3. Class
A class is a blueprint/template for creating objects.

```python
class Game:
    pass
```

## 4. Object
Object is an instance created from a class.

```python
g1 = Game()
```

## 5. Attributes
Variables inside objects/classes.

```python
qa1 = Tester()
qa1.name = "Ravi"
```

## 6. Methods
Functions inside a class.

```python
class Game:
    def play(self):
        print("Playing Game")
```

## 7. self
`self` = current object/instance.

- It is a parameter
- Python passes it automatically

## 8. Constructor (__init__)
Runs automatically when object is created.

```python
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role
```

## 9. Inheritance
Child gets parent features.

```python
class Child(Parent):
    pass
```

## 10. Encapsulation
Protect internal data and expose controlled access.

Example:
```python
self._balance
```

## 11. Polymorphism
Same method name, different behavior.

```python
class Car:
    def start(self):
        print("Car Started")

class Bike:
    def start(self):
        print("Bike Started")
```

## Interview Definitions
- Class → Blueprint
- Object → Instance
- Attribute → Variable inside object/class
- Method → Function inside class
- self → Current object
- Constructor → Runs during object creation
- Inheritance → Child gets parent features
- Encapsulation → Protect internal data
- Polymorphism → Same method, different behavior
