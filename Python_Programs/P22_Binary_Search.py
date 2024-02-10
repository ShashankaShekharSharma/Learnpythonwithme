import random
list=[]
n = int(input("Enter the number of elements: "))
for i in range(n):
    num = int(input("Enter the number: "))
    list.append(num)
target = list[random.randint(0,n-1)]
def binarysearch(list,target):
    low, high = 0,len(list)-1
    while low <= high:
        mid = (low+high)//2
        mid_value = list[mid]
        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid+1
        else: 
            high = mid-1
    return -1
print("The target value is: ",target)
result = binarysearch(list,target)
if result != -1:
    print("The target value (From Binary Search) is found at index: ",result)
else:
    print("Error 404")
