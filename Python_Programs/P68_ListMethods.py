import random
list = []
while len(list)<10:
    a = random.randint(1,10)
    list.append(a)
print("Original List: ",list)
list.sort()
print("Ascending Order: ",list)
list.reverse()
print("Descendingh Order: ",list)
list.reverse()
count_dict = {}
for element in list:
    count_dict[element] = list.count(element)
print(count_dict)