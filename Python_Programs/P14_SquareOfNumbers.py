#Write a Python program that asks the user to enter the number of integers they want to square. The program should then prompt the user to enter each integer one by one. Finally, it should create a new list containing the squares of the entered numbers and print the resulting squared list.
a = int(input("Enter the number of inputs: "))
list=[]
for i in range(1,a+1):
    b = int(input("Enter the number "))
    list.append(b)
list = [x ** 2 for x in list]
print("Squared List: ",list)