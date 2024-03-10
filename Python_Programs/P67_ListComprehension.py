list = [i+1 for i in range(10)]
print("Original List: ",list)
evenList = [i for i in list if i%2 == 0]
print("Even Numbers in the list: ",evenList)
oddList = [i for i in list if i%2 != 0]
print("Odd Numbers in the list: ",oddList)