class Employee:

    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    """def display_count(self):
        print(f"Total  number of employees: {Employee.emp_count}")"""

    def display_employee(self):
        print("Name: ", self.name, "\nSalary: ", self.salary, "\n")


emp1 = Employee('Juma Adonis',  5500)
emp2 = Employee('Christian Brown',  78500)
emp3 = Employee('Daniel Mbando',  70000)
emp1.salary = 804500
emp1.display_employee()
emp2.display_employee()
emp3.display_employee()
del emp1.salary
print(hasattr(emp1, 'salary'))
print(f"Total number of employees: {Employee.emp_count}")
