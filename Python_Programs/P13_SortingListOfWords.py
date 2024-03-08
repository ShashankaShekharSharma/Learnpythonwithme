#Write a Python program that prompts the user to enter the number of words they want to sort. Then, ask the user to enter each word one by one. Finally, sort the entered words in alphabetical order and print the sorted list.
a=int(input("Enter the number of words: "))
list = []
for i in range(1,a+1):
    print("Enter word ",i)
    name=input()
    list.append(name)
list = sorted(list)
print("Sorted List: ",list)
