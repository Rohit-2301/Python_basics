# The __init__() method is a constructor in Python that is automatically called when an object of a class is created.
# In inheritance, its behavior can be controlled to initialize attributes in both parent and child classes.


class parent:
    def __init__(self):
        print("Parent Constructor")


class Child(parent):
    def __init__(self):
        super().__init__()  # super() function  is used  access the constructor of parent class
        print("Child Constructor")


# If a child class defines its own __init__(), it overrides the parent’s constructor.
class child1(parent):
    def __init__(self):
        print("child1 constructor")


obj = Child()
obj1 = child1()


# If the parent class has parameters, we must pass arguments using super().

