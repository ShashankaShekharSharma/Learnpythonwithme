list1 = []
list2 = []
def wordset(word, char_list):
    for char in word:
        char_list.append(char)
def remove_duplicates(input_list):
    unique_list = list(set(input_list))
    return unique_list
word1 = input("Enter first word: ")
wordset(word1.lower(), list1)
word2 = input("Enter second word: ")
wordset(word2.lower(), list2)
list1.sort()  
list2.sort()  
list1 = remove_duplicates(list1)
list2 = remove_duplicates(list2)
if list1 == list2:
    print("Anagram")
else:
    print("Not an Anagram")
