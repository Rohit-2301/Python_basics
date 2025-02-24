# -w is used to write inside a file
# if file doesnt exist, it creates one
# if file exists, it overwrites the file
with open("example.txt", "w") as file:
    file.write("this is file handling")
    file.write("\n-w mode is used to write inside a file")
print("file written successfully")

# -r is used to read the contents of a file
# if file doesnt exist, it throws an err
with open("example.txt", "r") as file:
    content = file.read()
print(content)

# 'a' mode: Keeps the existing content and adds new data
with open("example.txt", "a") as file:
    file.write("\n-a is used for appending in the same file")
print("appended")

# to read file line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() remove the newline character

# Write a Python script to create a file named "data.txt" and write 5 lines of text.
with open("data.txt", "w") as file:
    file.write("this is a practice question\nline 1\nline 2\nline 3\nline 4")
print("data.txt created and written")
# optimised code:
# with open("data.txt", "w") as file:
#     lines = ["this is a practice question\n",
#              "line 1\n",
#              "line 2\n,"
#              "line 3\n,"
#              "line 4\n"]
#     file.writelines(lines)


# Read the file and print each line one by one.

with open("data.txt", "r") as file:
    content = file.readlines()
    total_words = 0
    total_char = 0
    for line in content:
        print(line.strip())
        total_words += len(line.split())
        total_char += len(line)
# Count the number of lines in "data.txt" and print:
# "Total number of lines in data.txt: X"
    print(f"Total number of lines in data.txt: {len(content)}")
# Modify your script to count the total number of words in "data.txt" and print:
# "Total number of words in data.txt: X"
    print(f"Total number of words in data.txt: {total_words}")
# Count the total number of characters in "data.txt" and print:
# "Total number of characters in data.txt: X"
    print(f"Total number of characters in data.txt: {total_char}")
