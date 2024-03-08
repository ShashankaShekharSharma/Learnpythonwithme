# Write a Python program that asks the user to enter the number of elements for a list. The program should then prompt the user to enter each element one by one. Finally, the program should find and display the largest number in the list.
'''
def numberlist(a):
  numbers=[]
  for i in range(a):
    n=int(input("Enter the number: "))
    numbers.append(n)
  return largestnumber(a,numbers)
def largestnumber(a,numbers):
  max=0
  for i in range(a):
    if numbers[i]>max:
      max = numbers[i]
  print("The largest number is: ",max)
a = int(input("Enter the number of elements"))
numberlist(a)
'''
def numberlist():
    numbers = list(map(int, input("Enter space-separated numbers: ").split()))
    return numbers

def largestnumber(numbers):
    max_num = max(numbers)
    return "The largest number is:", max_num

numbers = numberlist()

print(largestnumber(numbers))
