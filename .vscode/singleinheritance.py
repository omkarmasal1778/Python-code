from abc import ABC

class A(ABC):
    def func_1(self):
        pass  # print("This is defined inside the parent class")

class B(A):
    def func_1(self):
        print('This is inside the child class')

# Create an object of class B and call the methods
object = B()
object.func_1()
# object.func_2()