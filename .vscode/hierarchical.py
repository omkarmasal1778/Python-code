# Here, we will create the Base class
class Parent1:
    def func_1(self):
        print("This function is defined inside the parent class.")

# Derived class 1
class Child_1(Parent1):
    def func_2(self):
        print("This function is defined inside the child 1.")

# Derived class 2
class Child_2(Parent1):
    def func_3(self):
        print("This function is defined inside the child 2.")

# Creating objects of the derived classes
object1 = Child_1()
object2 = Child_2()

# Calling functions from the objects
object1.func_1()  # Calls Parent1's method
object1.func_2()  # Calls Child_1's method
object2.func_1()  # Calls Parent1's method
object2.func_3()  # Calls Child_2's method