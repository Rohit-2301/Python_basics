# 📚 CLI-Based Student Management System

## Overview
A simple CLI-based Student Management System that:
✅ Uses custom exceptions for input validation (e.g., invalid age, duplicate ID)
✅ Uses file handling to store student data persistently
✅ Implements OOP (Object-Oriented Programming) for better structure
✅ Follows a menu-driven CLI format

## Features
- Add a student (ID, name, age)
- View all students
- Search for a student by ID
- Delete a student
- Exit

## Why Use a CLI Tool?
✅ Lightweight and fast ⚡
✅ Can be used remotely (e.g., SSH into a server)
✅ Ideal for automation tasks
✅ Easy to integrate into scripts

## 🖥️ Examples of CLI Tools:
- git (Version Control)
- pip (Python Package Manager)
- ls, cd, mkdir (Linux commands)

# 🚀 Project Overview
This project is a ** Command Line Interface(CLI) Student Management System ** that allows users to manage student records efficiently. It follows ** Object-Oriented Programming(OOP) ** principles and incorporates ** custom exceptions ** for input validation. Additionally, student data is stored using ** file handling ** for persistence.

# ✨ Features
✅ Add a student(ID, name, age)
✅ View all students
✅ Search for a student by ID
✅ Delete a student
✅ Exit

# 🛠 Technologies Used
- **Python ** (Core programming language)
- **File Handling ** (For persistent storage)
- **Custom Exceptions ** (For error handling)
- **OOP(Object-Oriented Programming) ** (For better code structure)

# 📂 File Structure
```
StudentManagementSystem/
│── main.py               # Entry point of the program
│── student.py            # Student class definition
│── student_manager.py    # Handles student operations
│── students.txt          # Stores student data
│── exceptions.py         # Custom exceptions for validation
│── README.md             # Project documentation
```

# 🎯 How It Works
# 1️⃣ **Add a Student**
- Users can add a student by providing a ** unique ID, name, and age**.
- The system validates the input and prevents duplicate IDs.
- Data is stored in a file for persistence.

# 2️⃣ **View All Students**
- Displays all student records stored in the file.
- Ensures data is retrieved in a readable format.

# 3️⃣ **Search for a Student by ID**
- Users can enter a ** Student ID ** to find a specific record.
- Returns details if the student exists
otherwise, shows an error message.

# 4️⃣ **Delete a Student**
- Users can delete a student using their ** ID**.
- The system removes the entry from the file.

# 5️⃣ **Exit the Program**
- Ends the CLI session gracefully.

# ⚙️ How to Run the Program
# Step 1️⃣: Clone the Repository
```sh
git clone https: // github.com/your-username/StudentManagementSystem.git
cd StudentManagementSystem
```

# Step 2️⃣: Run the Program
```sh
python main.py
```

# 🚨 Custom Exception Handling
The system uses custom exceptions for:
- **Invalid Age Exception**: Ensures the age is a positive integer.
- **Duplicate ID Exception**: Prevents adding students with the same ID.
- **Student Not Found Exception**: Handles errors when searching for non-existent students.

# 📝 Future Enhancements
- Implement a ** GUI version ** of the system.
- Add ** database storage ** instead of file handling.
- Include ** student grade tracking**.

# 💡 Contributing
Contributions are welcome! Feel free to submit issues and pull requests.

# � License
This project is open-source and available under the ** MIT License**.

---
Developed with ❤️ by[Rohit]
