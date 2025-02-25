# exceptions are runtime errors that can crash your program
try:  # The risky code runs here.
    a = int(input("enter a number"))
    b = int(input("enter another number"))
    result = a/b
    print(f"result: {result}")
except ZeroDivisionError:  # Handles specific exceptions like ZeroDivisionError.
    print("cannot be divided by zero")
except ValueError:
    print("invalid input")
finally:  # Runs always, whether an exception occurs or not.
    print("execution completed")

# custon exceptions

try:
    num = int(input("enter a positive number"))
    if num < 0:
        # raise ValueError("message") manually throws an error when a condition is met.
        raise ValueError("negative number not allowed")
    print(f"you entered: {num}")
except ValueError as e:
    print(f"Error: {e}")


print("practice question")

#  Write a program that:

# Takes age as input.
# If age is negative, raise an exception with a message "Age cannot be negative!"
# Handle this exception and print the error message.

try:
    age = int(input("Enter age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(f"Age: {age}")
except ValueError as e:
    print(f"Error: {e}-invalid input")

