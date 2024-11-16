# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

# Child class
class Student(Person):
    def __init__(self, name, age, dob):
        # Inheriting the properties of the parent class
        super().__init__(name, age)  # Use the parameters passed to the constructor
        self.dob = dob

    def displayInfo(self):
        print(self.name, self.age, self.dob)  # Use self.name and self.age from the parent class

# Creating an instance of the Student class
obj = Student("Mayank", 23, "16-03-2000")

# Calling methods
obj.display()       # Calls the display method from the Person class
obj.displayInfo()   # Calls the displayInfo method from the Student class