# Python Programming Concepts (Theory)

## 1️⃣ Introduction to Python
Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

## 2️⃣ Basic Data Types & Operations
- **Integers (int)**: Whole numbers (e.g., `5`, `-10`)
- **Floats (float)**: Decimal numbers (e.g., `3.14`, `-2.5`)
- **Strings (str)**: Sequence of characters (e.g., `'hello'`, `"Python"`)
- **Booleans (bool)**: `True` or `False`
- **Lists (list)**: Ordered, mutable collections (e.g., `[1, 2, 3]`)
- **Tuples (tuple)**: Ordered, immutable collections (e.g., `(1, 2, 3)`)  
- **Sets (set)**: Unordered, unique elements (e.g., `{1, 2, 3}`)
- **Dictionaries (dict)**: Key-value pairs (e.g., `{"name": "Alice", "age": 25}`)

## 3️⃣ Control Flow Statements
### **Conditional Statements**
```python
if condition:
    # Code block executes if condition is True
elif another_condition:
    # Code block executes if the second condition is True
else:
    # Executes if none of the above conditions are True
```

### **Loops**
- **For Loop**: Iterates over a sequence (list, tuple, string, etc.).
  ```python
  for i in range(5):
      print(i)
  ```
- **While Loop**: Repeats as long as the condition is True.
  ```python
  i = 0
  while i < 5:
      print(i)
      i += 1
  ```

## 4️⃣ Functions
Functions are reusable blocks of code that perform a specific task.
```python
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
```

## 5️⃣ Exception Handling
Exception handling prevents runtime errors from crashing a program.
```python
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed.")
```

## 6️⃣ Object-Oriented Programming (OOP)
### **Classes & Objects**
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def show_details(self):
        return f"Car: {self.brand} {self.model}"
car1 = Car("Toyota", "Camry")
print(car1.show_details())
```

### **Inheritance**
Inheritance allows a class to inherit properties and methods from another class.
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()  # Outputs: Dog barks
```

### **Method Overriding**
When a child class has a method with the same name as a parent class but a different implementation.

## 7️⃣ File Handling
### **Writing to a File**
```python
with open("data.txt", "w") as file:
    file.write("This is a test file.")
```
### **Reading from a File**
```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

## 8️⃣ Custom Exceptions
You can define your own exceptions by inheriting from the Exception class.
```python
class NegativeValueError(Exception):
    def __init__(self, message="Value cannot be negative"):
        super().__init__(message)

try:
    value = int(input("Enter a number: "))
    if value < 0:
        raise NegativeValueError()
except NegativeValueError as e:
    print(f"Error: {e}")
```

---


