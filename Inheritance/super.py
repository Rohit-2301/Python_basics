# super keyword: it is used to access the functions of parent class
class parent:
    def show(self):
        print("parent class")


class child(parent):
    def show(self):
        super().show()
        print("this is child class")


obj = child()
obj.show()
