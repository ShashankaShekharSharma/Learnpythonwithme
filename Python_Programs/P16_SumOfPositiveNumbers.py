# Write a code in Python to add the numbers in a list and print its sum

# Simple Code
# a = int(input("How many numbers are there in the list: "))
# list=[]
# sum = 0
# for i in range(1,a+1):
#     num= int(input("Enter number (positive/negative): "))
#     list.append(num)
# for i in range(len(list)):
#     if list[i]>0:
#         sum+=list[i]
# print("Sum of all positive integers: ",sum)

def takeinput():
    a = list(map(int,input("Enter the numbers in the list separated by space: ").split(" ")))
    return a
def takesum(*a):
    sum = 0
    for i in a:
        sum += i
    return sum
num = takeinput()
print(takesum(*num))
