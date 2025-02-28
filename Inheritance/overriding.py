# Overriding is a concept , in which we have same function name, in both the parent and child class, but with a different body,
# (OR)
# Overriding means redefining a method in the child class that already exists in the parent class .
# The child class replaces the parent's method with its own version.
class parent:
    def show(self):
        print("parent class")


class child(parent):
    def show(self):
        print("child class")


obj = child()
obj.show()
