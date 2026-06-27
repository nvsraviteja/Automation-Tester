class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
   

# name = input("Enter name:")
# age = int(input("Enter age:"))
# salary = int(input("Enter Salary"))

e1 = Employee("name","age","salary")

class EmployeesManager():
    def __init__(self,employee):
        self.Employee = employee

m1 = EmployeesManager(e1)
print(m1.Employee.name)