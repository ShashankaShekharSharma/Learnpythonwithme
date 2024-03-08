#Write a Python program that defines a function called prime that takes an integer as input. The function should check if the number is a prime number. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should utilize a flag variable to track primality and print whether the entered integer is a prime number or not.
def prime(n):
    Flag = 0
    for i in range(1,n):
        if n%i==0:
            Flag = 0
        else:
            Flag = 1
    if Flag == 1:
        print("Prime Number")
    else:
        print("Not Prime Number")
a=int(input("Enter an integer: "))
prime(a)