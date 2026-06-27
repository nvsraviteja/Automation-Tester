class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def __str__(self):
        return f"Name:{self.name}\n Age:{self.age}\nSalary:{self.salary}"


