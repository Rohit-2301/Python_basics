# A child class inherits from another child class.
# here {Grandparent <-- Parent <-- child}, child has properties of both parent and grandparent, therefore we can access their function with the help of obj of 'child'


class Grandparent:
    def feature1(self):
        print("Feature from Grandparent")


class Parent(Grandparent):
    def feature2(self):
        print("Feature from Parent")


class Child(Parent):
    def feature3(self):
        print("Feature from Child")


obj = Child()
obj.feature1()  # From Grandparent
obj.feature2()  # From Parent
obj.feature3()  # Defined in Child
