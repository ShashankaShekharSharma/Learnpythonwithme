#Write a Python function that takes a string as input and returns the reversed version of the string. Additionally, write code that prompts the user to enter a string, utilizes the defined function to reverse it, and then prints the reversed string.
def reverse(string):
  return string[::-1]
string = input("Enter a string to reverse: ")
reversed_string = reverse(string)
print("The reversed string is:", reversed_string)
