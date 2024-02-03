#Determine whether the given string is pallindrome or not
def pallindrome(string):
  reverse_string = string[::-1]
  if reverse_string == string:
    return "pallindrome"
  else:
    return "not pallindrome"
string = input("Enter the word: ")
print(pallindrome(string))
