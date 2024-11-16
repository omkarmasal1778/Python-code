# Base class
class Base:
    # Constructor
    def __init__(self, name):
        self.name = name
    
    # To get name
    def getName(self):
        return self.name

# Inherited or sub-class
class Child(Base):
    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age  # Initialize age properly
    
    # To get age
    def getAge(self):
        return self.age

# Grandchild class (multi-level inheritance)
class GrandChild(Child):
    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address  # Initialize address properly
    
    # To get address
    def getAddress(self):
        return self.address

# Create an object of the GrandChild class
g = GrandChild('Geek1', 23, 'Noida')

# Print name, age, and address using the methods
print(g.getName(), g.getAge(), g.getAddress())
