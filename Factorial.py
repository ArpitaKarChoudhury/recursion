# Write a Python program to get the factorial of a non-negative integer. 
def factorial(a):
    if a == 1:
        return 1
    else:
        return a* factorial(a-1)
a= int(input("enter possitive number"))
print(factorial(a))