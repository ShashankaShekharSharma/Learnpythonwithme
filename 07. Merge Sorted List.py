#Write a Python program to merge two sorted lists into a single sorted list.
def merge_sorted_lists(list1, list2):
  merged_list = list1 + list2
  merged_list.sort()
  return merged_list
list1 = [1, 8, 9, 3, 5]
list2 = [2, 4, 6, 7, 10]
print("List 1:", list1)
print("List 2:", list2)
result = merge_sorted_lists(list1, list2)
print("Merged list is " + str(result))
