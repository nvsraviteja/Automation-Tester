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
        manager.update_salary(find_name, new_salary)
    
    def list_employees(self):
        manager.list_employees()

fem = FrontendManager()


while True:
    select = int(input("1. Adding new Employee\n2. Listing existing employees\n3. Find employee\n4. Deleting employees based on age range\n5. Updating employee salaries by name\n6. exit\nenter number:"))
    if select == 1:
        fem.adding_new_employee()
    elif select ==2:
        fem.list_employees()
    elif select == 3:
        fem.find_employee()
    elif select == 4:
        fem.delete_employee_by_age()
    elif select == 5:
        fem.update_employee_salary()
    elif select == 6:
        break
