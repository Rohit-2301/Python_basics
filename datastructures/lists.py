# A list is an ordered, mutable(changeable) collection of elements in Python. Lists can store any type of data(numbers, strings, other lists, etc.).

# list is a datatype which contains heterogenous data
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i, end=" ")
print()

info = ['rohit', 21, '22BCS13677']
for i in info:
    print(i, end=" ")
print()

empty_list = []

# accessing list
fruits = ["apple", "mango", 'banana', "guava", "cherry"]
print(fruits[0])
print(fruits[0:2])  # slice
print(fruits[-1])  # last element

# replacing
fruits[1] = "watermelon"
print(fruits[1])

# adding
fruits.append("melon")  # adds in end
print(fruits)
fruits.insert(2, "tomato")
print(fruits)

# removing
fruits.remove("tomato")  # remove specific element
print(fruits)
fruits.pop()  # remove last element
print(fruits)

# Create a list of 5 numbers and print their total_sum.
num = [1, 2, 3, 4, 5]
total_sum = 0
for i in num:
    total_sum = total_sum+i
print(total_sum)
# Reverse a list without using[::-1].

while fruits:
    fruit = fruits.pop()
    empty_list.append(fruit)
print(empty_list)
