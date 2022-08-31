# Write a Python program to get the sum of a non-negative integer. Go to the editor
# Test Data:
# sumDigits(345) -> 12
# sumDigits(45) -> 9

def total(i):
    global b
    if len(a) == i:
        return i
    else:
        b = int(a[i]) + b
        total(i+1)
        return b


a = input("enter positive number")
b = 0
print(total(0))
