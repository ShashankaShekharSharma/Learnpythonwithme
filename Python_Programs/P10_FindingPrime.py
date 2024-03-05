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