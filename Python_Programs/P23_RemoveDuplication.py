my_list = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    num = int(input("Enter the number: "))
    my_list.append(num)

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

result_list = remove_duplicates(my_list)
print("List with Duplicates:", my_list)
print("List without Duplicates:", result_list)
