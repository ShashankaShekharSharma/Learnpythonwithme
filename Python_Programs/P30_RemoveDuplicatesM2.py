def remove_duplicates(input_list):
    unique_list = list(set(input_list))
    return unique_list
user_input = input("Enter elements of the list separated by spaces: ")
user_list = [int(x) for x in user_input.split()]
result_list = remove_duplicates(user_list)
print("Original List:", user_list)
print("List with Duplicates Removed:", result_list)
