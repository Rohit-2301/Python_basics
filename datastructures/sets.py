# unordered, mutable, unique collection of elements
numbers = {1, 2, 3, 4, 5, 6}
info = {"rohit", 21, "B.E-S.C.S.E"}
empty_set = set()  # {} creates empty dict not set

# no indexing as unordered
print(numbers)
for i in numbers:
    print(i, end=" ")
print()

# adding element to set
numbers.add(4.3)
print(numbers)

# removing element from a set

numbers.remove(3)  # gives error if 3 is not present in the set
print(numbers)

numbers.discard(4)  # does not give error if 3 is not present in the set
print(numbers)

# mathematical operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a)
print(b)
print("a U b: ", a | b)  # union
print("a intersec b: ", a & b)  # intersection
print("a - b: ", a - b)  # difference
print("b - a: ", b - a)  # difference
print("a ^ b: ", a ^ b)  # symmetric difference

print("practice questions")

# Create a set with 5 numbers and remove the largest number.

num = {1, 2, 3, 4, 5}
max_num = max(num)
print(f"largest num is {max_num}")
num.remove(max_num)
# Find the common elements between two sets {10, 20, 30, 40} and {30, 40, 50, 60}.
x = {10, 20, 30, 40}
y = {30, 40, 50, 60}
print("common elements:", x & y, end=" ")
