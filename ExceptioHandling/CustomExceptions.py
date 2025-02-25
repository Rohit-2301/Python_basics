# creating custom exceptions


class NegativeValueError(Exception):
    # We define a custom exception class called NegativeValueError.
    # This class inherits from Python's built-in Exception class.
    def __init__(self, message="age cannot be negative"):
        # The __init__ method is used to initialize the exception.
        super().__init__(message)
        # super().__init__(message) calls the parent class (Exception) constructor, passing the message.


try:
    age = int(input("enter age: "))
    if age < 0:
        # raise ValueError("message") manually throws an error when a condition is met.
        raise NegativeValueError()
    print(f"you entered: {age}")
except (NegativeValueError, ValueError) as e:
    print(f"Error: {e}-invalid input")


# example 2: custom exceptions for weak passwords

class WeakPasswordError(Exception):
    def __init__(self, message="password is weak"):
        super().__init__(message)


def setPassword(password):
    if len(password) < 8:
        raise WeakPasswordError()
    print("password set successfully")


try:
    password = input("enter a password: ")
    setPassword(password)
except WeakPasswordError as e:
    print(f"error occured: {e}")
