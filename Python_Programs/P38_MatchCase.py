# Write a function classify_vowel(char) that takes a single character as input and uses a match-case statement to determine and return its vowel classification.
def classify_vowel(char):
    match char:
        case 'a' | 'e' | 'i' | 'o' | 'u':
            return "Lowecase Vowel"
        case 'A' | 'E' | 'I' | 'O' | 'U':
            return "Uppercase Vowel"
        case _:
            if char.isalpha():
                return "Not a vowel"
            else:
                return "Invalid Input"
a = input("Enter a char: ")
print(classify_vowel(a))
