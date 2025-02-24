# similar to list but immutable

numbers = (10, 20, 40)
diff_dataatype = ("rohit", 3, 3.5, True)

single_elem = (10,)  # without comma it is just an int

for i in numbers:
    print(i, end=" ")
print()
# packing and unpacking

person = ("rohit", 21, "B.E-C.S.E")  # packing
name, age, stream = person  # unpacking
print(name, end=" ")
print(age, end=" ")
print(stream)

# convert tuple to list and vice-versa

# tuple to list
tup_num = (10, 20, 30)
list_num = list(tup_num)
for i in list_num:
    print(i, end=" ")
print()
list_num.append(40)
for i in list_num:
    print(i, end=" ")
print()

# list to tuple
list_num = tuple(tup_num)
print("this is a tuple")
for i in list_num:
    print(i, end=" ")
print()
print("practice questions")


# create a tuple of 5 numbers and find their sum.
tup_sum = 0
for i in tup_num:
    tup_sum += i
print(f"the sum is {tup_sum}")

# Swap two numbers using a tuple(without using a third variable).

tuple_num = (5, 6)
print(tuple_num)
tuple_num = (tuple_num[1], tuple_num[0])
print(tuple_num)
