# collection of key-value pairs , mutable, unordered, no duplicate keys
student = {
    "name": "rohit",
    "age": 20,
    "college": "chandigarh university"
}
print(student)
# accessing:
print(student["name"])
# .get(), preferable as it will not throw error if key is not present
print(student.get("age"))

# adding and updating
student["course"] = "C.S.E"
student["age"] = "21"
print(student)

# removing
student.pop("college")
del student["course"]
print(student)

# looping
for key in student:
    print(key, end=" ")
print()
for value in student.values():
    print(value, end=" ")
print()
for key, value in student.items():
    print(f"{key}:{value}")

# dictionary methods
student1 = {
    "name": "rohit",
    "age": 20,
    "college": "chandigarh university"
}

print()
print(student1.keys())
print(student1.values())
print(student1.items())

# Create a dictionary with 5 student names as keys and their marks as values.
student_marks = {
    "a": 91,
    "b": 93,
    "x": 88,
    "y": 90,
    "z": 92
}
print(student_marks)

print("practice questions")

# Find the student with the highest marks.
scholar = max(student_marks, key=student_marks.get)
# max(dictionary, key=dictionary.get) → Finds key with max value.
print(f"topper student : {scholar} with {student_marks[scholar]} marks")
