a=input("Enter a word: ")
def vowels(a):
  count = 0
  for i in range(len(a)):
    if a[i] in "aeiou":
      count+=1
  return count
print("Number of vowels: ",vowels(a))
print("Number of consonants: ",abs(len(a)-vowels(a)))
