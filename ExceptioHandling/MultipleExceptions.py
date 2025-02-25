# Handling Multiple Exceptions in One except Block
try:
    num = int(input("enter a num: "))
    result = 10/num
    print(result)
except (ZeroDivisionError, ValueError) as e:
    print(f"error: {e}")
