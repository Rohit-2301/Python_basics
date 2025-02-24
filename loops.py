languages = ["python", "c++", "java", "html", "js"]

# for loop(definite loop)
# without range
for lang in languages:
    print(lang, end=" ")
print()

# with range
for i in range(1, 6):
    print(i, end=" ")
print()
for i in range(5):
    print(i, end=" ")
print()

# here 1 is start, 10 is end and 2 is to add to every iterations until <10
for i in range(1, 10, 2):
    print(i, end=" ")
print()


# while loop(indefinite loop)
num = 1
while num <= 5:
    print(num, end=" ")
    num += 1  # increases number to avoid infinite loop
print()


char = 'a'
while char <= 'd':
    print(char, end=" ")
    char = chr(ord(char)+1)
print()
# continue and break: continue is used to skip that specific iteration and move to next, break is used to exit from the loop
for i in range(1, 10):
    if i == 3:
        continue
    print(i, end=" ")
print()
for i in range(1, 10):
    if i == 3:
        break
    print(i, end=" ")
print()

print("practice questions")

# Write a Python program to print all even numbers from 1 to 20 using a for loop.
for i in range(1, 10):
    if i % 2 == 0:
        print(i, end=" ")
print()
# Use a while loop to count down from 10 to 1.
i = 10
while i >= 1:
    print(i, end=" ")
    i -= 1
print()
