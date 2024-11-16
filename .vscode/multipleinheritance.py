# Here, we will create the Base class 1
class Mother1:
    def __init__(self, mothername1=""):  # Constructor to initialize mother's name
        self.mothername1 = mothername1

    def mother1(self):
        print(self.mothername1)

# Here, we will create the Base class 2
class Father1:
    def __init__(self, fathername1=""):  # Constructor to initialize father's name
        self.fathername1 = fathername1

    def father1(self):
        print(self.fathername1)

# Now, we will create the Derived class
class Son1(Mother1, Father1):
    def __init__(self, mothername1="", fathername1=""):  # Constructor for Son1
        Mother1.__init__(self, mothername1)  # Initialize Mother1 part
        Father1.__init__(self, fathername1)  # Initialize Father1 part

    def parents1(self):
        print("Father name is:", self.fathername1)
        print("Mother name is:", self.mothername1)

# Create an instance of Son1
s1 = Son1("Shreya", "Rajesh")
s1.parents1()