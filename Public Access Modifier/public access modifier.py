class Employee:
    def __init__(self,name,salary):
        self.name=name #Public Attribute
        self.salary=salary #Public Attribute

    def show_details(self):
        print(f"Employee Name:{self.name}, Salary: Rs{self.salary}")

#Creating an object
emp=Employee("Jhon",5000)


#Accessing public attributes
print(emp.name)
print(emp.salary)


#Calling public method
emp.show_details()
