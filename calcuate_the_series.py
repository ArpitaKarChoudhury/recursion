# Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... 
# (until n-x =< 0)

def cal(n,i):
    global b
    if n == 0:
        return 0
    else:
        b = n+(n-i)
        cal(n-b,i+2)
        return b
n=int(input("enter possitive int number"))
i=0
b=0
print(cal(n,i))
