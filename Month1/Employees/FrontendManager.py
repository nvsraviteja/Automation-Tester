from Employees_Manager import EmployeesManager
manager = EmployeesManager()

class FrontendManager():
    def __init__(self):
         pass

    def adding_new_employee(self):
        name = input("Enter name:")
        age = int(input("Enter age:"))
        salary = int(input("Enter salary:"))
        manager.add_a_new_employee(name,age,salary)

    def find_employee(self):
        find_name = input("Enter Employee name:")
        manager.find_employee(find_name)
    
    def delete_employee_by_age(self):
        min_age = int(input("Enter minimum age:"))
        max_age = int(input("Enter maximum age:"))
        manager.delete_employees(min_age,max_age)
    
    def update_employee_salary(self):
        find_name = input("Enter Employee name:")
        new_salary = int(input("Enter new salary:"))
        manager.update_salary(new_salary,find_name)
