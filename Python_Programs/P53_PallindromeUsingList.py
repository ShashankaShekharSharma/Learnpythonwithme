def pallindromeCheck(elementList):
    elementListReversed = elementList[::-1]
    if elementList == elementListReversed:
        print("It is a pallindrome")
    else:
        print("Not a pallindrome")

a = map(int,input("Enter the list with elements separated by space: ").split())
elementList = []
for elements in a:
    elementList.append(elements)
pallindromeCheck(elementList)
