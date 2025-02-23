# initialising variable
# case sensitive language
x = 12
y = 30
print(12+30)
# using variables in expressions
a = 5
b = 7
c = 10
print(a*b*c)
# taking input from user
name = input("Enter your name: ")  # default input type is string
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
# print
print("\nHello, {}! You are {} years old. If you weigh {} kg and stand {} meters tall.".format(
    name, age, weight, height))
