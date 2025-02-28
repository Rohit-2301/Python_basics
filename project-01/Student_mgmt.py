class StudentManagement:
    def __init__(self):
        # Initializes an empty dictionary to store student details.
        self.students = {}

    def add_student(self):
        roll_no = input("Enter student roll_num: ")
        if roll_no in self.students:
            print("Student already exists")
            return

        # Taking student details as input.
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        CGPA = input("Enter student CGPA: ")

        # Storing student details in a dictionary.
        self.students[roll_no] = {"name": name, "age": age, "CGPA": CGPA}
        print("Student details added successfully")

    def view_students(self):
        if not self.students:
            print("No data exists")
            return
        print("\n--- STUDENT LIST ---\n")
        for roll_no, data in self.students.items():
            print(
                f"Roll no.: {roll_no}, Name: {data['name']}, Age: {data['age']}, CGPA: {data['CGPA']}"
            )

    def search_student(self):
        roll_no = input("Enter roll number: ")
        student = self.students.get(roll_no)  # Using .get() to avoid KeyError.
        if student:
            print(f"Found: {student}")
        else:
            print("Student not found")

    def update_details(self):
        roll_no = input("Enter roll number: ")
        if roll_no not in self.students:
            print("Student not found!")
            return

        # If the user enters a blank value, retain the old value using "or".
        name = input(
            "Enter New Name (leave blank to keep existing): ") or self.students[roll_no]["name"]
        age = input(
            "Enter New Age (leave blank to keep existing): ") or self.students[roll_no]["age"]
        CGPA = input(
            "Enter New CGPA (leave blank to keep existing): ") or self.students[roll_no]["CGPA"]

        # Updating student details.
        self.students[roll_no] = {"name": name, "age": age, "CGPA": CGPA}
        print("Student updated successfully!")

    def delete_student(self):
        roll_no = input("Enter roll number: ")
        if roll_no in self.students:
            del self.students[roll_no]  # Removing student from dictionary.
            print("Student details removed!")
        else:
            print("Student not found")

    def run(self):
        while True:
            print("\n1. Add Student\n2. View Students\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Exit")
            choice = input("Enter your choice: ")

            # Checking user's choice and calling respective methods.
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.update_details()
            elif choice == "5":
                self.delete_student()
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please try again.")


# Ensures the script runs only when executed directly, not when imported as a module.
if __name__ == "__main__":
    app = StudentManagement()
    app.run()
