from P17_Factorial import factorial
def takeinput():
    print("For nCr, give input for n and r: ")
    n = int(input("Enter the value of n: "))
    r = int(input("Enter the value of r: "))
    return n, r
n,r = takeinput()
if n>r:
    a = factorial(n)
    b = factorial(r)
    c = factorial(n-r)
    combination = a/(b*c)
    print(combination)
else:
    print("Invalid Operation")