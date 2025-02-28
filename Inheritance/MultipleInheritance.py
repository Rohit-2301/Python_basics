# Multiple Inheritance : in multiple inheritance a class can have multiple parents,
# like here 'C' is inheriting 'A' as well as 'B'
class A:
    def a(self):
        print("this is a")


class B:
    def b(self):
        print("this is b")


class C(A, B):
    pass


obj = C()
obj.a()
obj.b()
