# Inheritance allows a class (child class) to reuse attributes and methods from another class (parent class).

class parent:
    def greet(self):
        print("hello, from parent")


class child(parent):
    def greet2(self):
        print("hello, from child")
    pass  # inherits everything from parent


obj = child()
obj.greet()
obj.greet2()
