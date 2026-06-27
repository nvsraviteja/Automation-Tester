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
        for i in self.list_of_employees:
            print(i,"\n")
    
    def delete_employees(self):
        


manager = EmployeesManager()
nikhil = Employee("Nikhil",26,150000)
manager.add_existing_employee(nikhil)  

manager.list_employees()
