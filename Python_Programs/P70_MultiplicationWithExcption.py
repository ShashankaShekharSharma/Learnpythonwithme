def multiplicationTable(a):
    try:
        print(f"Multiplication Table of {a} is: ")
        for i in range(1,11):
            print(f"{a} X {i} = {a*i}")
    except:
        print("Error 404")
a = 1
while a != 0:
    a = int(input("Enter the number for the multiplication table (enter 0 to exit): "))
    multiplicationTable(a)
    