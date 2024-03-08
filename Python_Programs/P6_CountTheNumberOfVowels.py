#Write a Python program that asks the user to enter a word. Define a function that takes the word as input and counts the number of vowels (a, e, i, o, u) in the word. The program should then call the function, print the number of vowels found, and calculate and print the number of consonants (assuming all letters are either vowels or consonants).
a=input("Enter a word: ")
def vowels(a):
  count = 0
  for i in range(len(a)):
    if a[i] in "aeiou":
      count+=1
  return count
print("Number of vowels: ",vowels(a))
print("Number of consonants: ",abs(len(a)-vowels(a)))