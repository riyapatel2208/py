class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def details(self):
        print(f"Person Details - Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

    def details(self):
        print(f"Employee Details - Name: {self.name}, Age: {self.age}, "
              f"Employee ID: {self.employee_id}, Department: {self.department}")


if __name__ == "__main__":
    # Get user input for Person details
    name = input("Enter the name of the person: ")
    age = int(input("Enter the age of the person: "))
    person = Person(name, age)
    
    print("\nPerson Info:")
    person.display()
    person.details()

    # Get user input for Employee details
    name = input("\nEnter the name of the employee: ")
    age = int(input("Enter the age of the employee: "))
    employee_id = input("Enter the employee ID: ")
    department = input("Enter the department: ")
    employee = Employee(name, age, employee_id, department)
    
    print("\nEmployee Info:")
    employee.display()
    employee.details()
