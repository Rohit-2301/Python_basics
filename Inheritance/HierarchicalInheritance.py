# Hierarchical Inheritance:In this multiple child inherit a single parent
# like here we 'A' and 'B' inherit 'parent', i.e., obj of both 'A' and 'B' can access function/variable of parent class
class parent:
    def common(self):
        print("parent")


class A(parent):
    def feature1(self):
        print("A")


class B(parent):
    def feature2(self):
        print("B")


obj1 = A()
obj2 = B()
obj1.common()
obj2.common()
