
# **CLI-Based Student Management System – Beginner's Guide**

## **1. Introduction**
A **Command Line Interface (CLI) Student Management System** is a simple application that allows users to manage student records efficiently using only the terminal. The system supports essential **CRUD (Create, Read, Update, Delete)** operations.

This project is implemented using **Python** and focuses on key programming concepts like:
- Functions & Classes
- Dictionaries & Data Storage
- Exception Handling
- Object-Oriented Programming (OOP)
- CLI-based interaction

---

## **2. Project Features**
This system allows users to:
1. **Add Student** – Create a new student record.
2. **View Students** – Display all student records.
3. **Search Student** – Find a student using their roll number.
4. **Update Student** – Modify student details.
5. **Delete Student** – Remove a student from the system.
6. **Exit** – Quit the program.

---

## **3. Key Python Concepts Used**
### **A. Object-Oriented Programming (OOP)**
This project follows the **OOP** paradigm. We use:
- **Classes** to define the structure of the program.
- **Objects** to interact with student records.
- **Methods (Functions inside Classes)** to perform specific tasks.

#### **Class Example**
```python
class StudentManagement:
    def __init__(self):
        self.students = {}  # Dictionary to store student records
```
Here, the `StudentManagement` class contains all the functionalities of our system.

### **B. Dictionaries for Data Storage**
We use a **dictionary (`dict`)** to store student data:
```python
self.students = {
    "101": {"name": "John", "age": "20", "marks": "85"}
}
```
Each **roll number** acts as a **unique key**, and the value is another dictionary containing student details.

### **C. Exception Handling**
Exception handling prevents the program from crashing when unexpected input is provided.

#### Example:
```python
try:
    roll_no = input("Enter roll number: ")
    if roll_no not in self.students:
        raise ValueError("Student not found!")
except ValueError as e:
    print(f"Error: {e}")
```
Here, if the roll number is not found, we manually **raise an error** using `raise ValueError("Student not found!")`.

---

## **4. Explanation of CRUD Operations**
### **A. Create (Add a Student)**
The `add_student()` method:
1. Asks for student details.
2. Checks if the roll number already exists.
3. Stores student details in the dictionary.

#### **Code Example**
```python
def add_student(self):
    roll_no = input("Enter student roll_num: ")
    if roll_no in self.students:
        print("Student already exists!")
        return
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    marks = input("Enter student marks: ")

    self.students[roll_no] = {"name": name, "age": age, "marks": marks}
    print("Student added successfully!")
```

### **B. Read (View Students)**
The `view_students()` method:
1. Checks if any students exist.
2. Loops through the dictionary and prints student details.

#### **Code Example**
```python
def view_students(self):
    if not self.students:
        print("No data exists")
        return
    print("\n--- STUDENT LIST ---\n")
    for roll_no, data in self.students.items():
        print(f"Roll No.: {roll_no}, Name: {data['name']}, Age: {data['age']}, Marks: {data['marks']}")
```

### **C. Search Student**
The `search_student()` method:
1. Takes a roll number as input.
2. Checks if it exists in the dictionary.
3. Displays student details if found.

#### **Code Example**
```python
def search_student(self):
    roll_no = input("Enter roll number: ")
    student = self.students.get(roll_no)
    if student:
        print(f"Found: {student}")
    else:
        print("Student not found")
```

### **D. Update Student Details**
The `update_details()` method:
1. Asks for the roll number.
2. If found, asks for new details (allows skipping updates).
3. Updates the dictionary.

#### **Key Concept: Default Values using `or`**
```python
name = input("Enter New Name (leave blank to keep existing): ") or self.students[roll_no]["name"]
```
- If the user **enters a value**, it is stored.
- If the user **presses Enter (leaving blank)**, it keeps the existing value.

#### **Code Example**
```python
def update_details(self):
    roll_no = input("Enter roll number: ")
    if roll_no not in self.students:
        print("Student not found!")
        return
    name = input("Enter New Name (leave blank to keep existing): ") or self.students[roll_no]["name"]
    age = input("Enter New Age (leave blank to keep existing): ") or self.students[roll_no]["age"]
    marks = input("Enter New Marks (leave blank to keep existing): ") or self.students[roll_no]["marks"]

    self.students[roll_no] = {"name": name, "age": age, "marks": marks}
    print("Student updated successfully!")
```

### **E. Delete a Student**
The `delete_student()` method:
1. Takes a roll number as input.
2. Deletes the entry from the dictionary.

#### **Code Example**
```python
def delete_student(self):
    roll_no = input("Enter roll number: ")
    if roll_no in self.students:
        del self.students[roll_no]
        print("Student details removed!")
    else:
        print("Student not found")
```

---

## **5. CLI Menu System**
A `while True` loop is used to create a **menu-driven interface**:
```python
def run(self):
    while True:
        print("\n1. Add Student\n2. View Students\n3. Search Student\n4. Update Student\n5. Delete Student\n6. Exit")
        choice = input("Enter your choice: ")

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
```
### **Key Points:**
- Users **choose an option** (1-6).
- Corresponding **method is executed**.
- **Loop continues** until the user selects **Exit (6)**.

---

## **6. Running the Program**
To run the program only when executed directly:
```python
if __name__ == "__main__":
    app = StudentManagement()
    app.run()
```
This ensures that the script **only runs when executed**, not when imported.

---

## **7. Summary of Key Takeaways**
✅ **Used Python Classes & OOP**  
✅ **Implemented CRUD Operations**  
✅ **Used Dictionaries for Data Storage**  
✅ **Handled Exceptions Gracefully**  
✅ **Built a CLI-Based Interactive System**  

---

## **8. Possible Enhancements**
- **Store Data Permanently** (Using JSON or SQLite)
- **Add More Fields** (e.g., Address, Course)
- **Implement Sorting & Filtering**
- **GUI Version (Tkinter or Flask Web App)**

---

