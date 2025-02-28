

def add_student():
    Name = input("Enter student name: ")
    Roll_no = int(input("Enter student roll no.: "))
    Age = int(input("Enter student age: "))
    CGPA = float(input("Enter student CGPA:"))
    print(f"Student Name:{Name}\nRoll_no:{Roll_no}\nAge: {Age}\nCGPA: {CGPA}")


def view_student():


def delete_student():

    # with open("student.txt", "w") as file:


def option_1():
    print("Add student")
    add_student()


def option_2():
    print("View student")
    view_student()


def option_3():
    print("Delete student")
    delete_student()
