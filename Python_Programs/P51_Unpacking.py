#Write a function flatten_list that takes a nested list as input and returns a flattened list. The function should use the concept of unpacking to flatten the nested structure.
def unpacking(nested_list):
    result = []
    for element in nested_list:
        if isinstance(element, list):
            result.extend(unpacking(element))
        else:
            result.append(element)
    return result

nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
print(unpacking(nested_list))

#The extend() method in Python is used to extend a list by appending elements from an iterable (such as another list, tuple, string, etc.) to the end of the original list. It modifies the original list in-place.
#The isinstance() function in Python is used to check if an object belongs to a particular class or type. It helps determine whether an object is an instance of a specified class or any of its subclasses.
