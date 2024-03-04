def removeduplicates(originalString):
    seen = set()
    newString = ""
    for char in originalString:
        if char not in seen:
            seen.add(char)
            newString += char
    return newString
originalString = input("Enter the string: ")
print(removeduplicates(originalString))