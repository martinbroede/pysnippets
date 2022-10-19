# Example usage of classes.
# Keywords
# class / super / init / initialization / inheritance / extend / constructor

class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary


person = Person("Jane Doe")
employee = Employee("John Doe", 10000)
