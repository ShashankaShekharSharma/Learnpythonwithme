# Write a code in Python which uses recursion to find the factorial of a number given by the user
def takeinput():
    a = int(input("Enter the number whose factorial you want to find: "))
    return a
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)