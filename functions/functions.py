print("without argument")


def greet():
    print("hello")


greet()

# with argument
print("with argument")


def Name(name):
    print(f"{name}")


Name("rohit")

# with return


def add(a, b):
    return a+b


print(add(10, 20))

# default parameter

print("default parameter")


def greet(name="Guest"):
    print(f"Hello, {name}!")


greet()        # Uses default: "Guest"
greet("Rohit")  # Uses "Rohit"


# lambda function
print("lambda fxn")
def square(x): return x*x


print(square(4))
# cube = lambda y: y*y*y
# print(cube(4))

print("practice question")
# Write a function multiply(a, b) that returns the product of two numbers.


def multiply(a, b): return a*b


print(multiply(5, 6))

# Write a function is_even(n) that returns True if a number is even, otherwise False.


def is_even(num):
    return num % 2 == 0


print(is_even(5))
print(is_even(4))
