# with arbitrary arguments: when we dont know the no. of arguments beforehand

from functools import reduce
print("with arbitrary arguments")


def add(*nums):
    return sum(nums)


print(add(1, 2, 3, 4))

# to accept any number of named arguments **kwargs


def student_info(**details):
    for key, value in details.items():
        print(f'{key}: {value}')


student_info(name="rohit", age=21, city="cgd")

# lambda functions: one line functions, use of map(),filter(),reduce()

nums = [1, 2, 3, 4, 5]
square = list(map(lambda x: x*x, nums))
print(square)

even = list(filter(lambda x: x % 2 == 0, nums))
print(even)

# from functools import reduce
product = reduce(lambda x, y: x*y, nums)
print(product)


print("practice questions")
# Write a function multiply_list(numbers) that takes a list and returns the product of all elements.


def multiply_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product


print(multiply_list([1, 2, 3, 4, 5]))


# Use a lambda function to filter out even numbers from [3, 6, 9, 12, 15]
num_list = [3, 6, 9, 12, 15]
even_num = list(filter(lambda x: x % 2 == 0, num_list))
odd_num = list(filter(lambda x: x % 2 != 0, num_list))
print(even_num)
print(odd_num)
