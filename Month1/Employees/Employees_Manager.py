from Employee import Employee

class EmployeesManager(Employee):
    def __init__(self):
        self.list_of_employees = []

    def add_a_new_employee(self,name,age,salary):
        new_employee = Employee(name,age,salary)
        self.list_of_employees.append(new_employee)
    
    def add_existing_employee(self,existing_employee):
        self.list_of_employees.append(existing_employee)

    def list_employees(self):
        for employee in self.list_of_employees:
            print(employee,"\n")
    
    def delete_employees(self):
        for employee in self.list_of_employees:
            if min_age <= employee.age and max_age >= employee.age:
                self.list_of_employees.remove(employee)
    
    def find_employee(self):
        for employee in self.list_of_employees:
            if find_name == employee.name:
                print(employee)

    def update_salary(self):
        for employee in self.list_of_employees:
            if find_name == employee.name:
                employee.salary = new_salary

# manager = EmployeesManager()
# nikhil = Employee("Nikhil",26,150000)
# manager.add_existing_employee(nikhil)  
# manager.add_a_new_employee("NVS", 24, 40)
# 
# find_name = "Nikhil"
# new_salary = 200000
# 
# manager.list_employees()
# manager.update_salary()
# manager.list_employees()
