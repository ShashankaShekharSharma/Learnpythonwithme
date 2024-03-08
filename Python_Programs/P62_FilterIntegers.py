'''
def filter(listset):
    onlyint = []
    for element in listset:
        if isinstance(element, list):
            for i in element:
                if isinstance(i,int):
                    onlyint.append(i)
        elif isinstance(element,int):
            onlyint.append(element)
    return onlyint
list1 = [1, 2, 'three', [4, 'five', 6], 7, 'eight']
print(filter(list1))
'''
def filter_integers(lst):
    result = []
    for element in lst:
        if isinstance(element, list):
            result.extend(filter_integers(element))
        elif isinstance(element, int):
            result.append(element)
    return result

list1 = [1, 2, 'three', [4, 'five', 6], 7, 'eight']
print(filter_integers(list1))
