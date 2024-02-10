list1 = []
list2 = []
def listupdate(lenlist):
    for a in range(lenlist):
        num = int(input("Enter the number: "))
        list1.append(num)
for i in range(1,3):
    lenlist = int(input("How many elements are there in list: "))
    listupdate(lenlist)
list1=set(list1)
list2=set(list2)
print("The common elements are: ",list1.intersection(list2))