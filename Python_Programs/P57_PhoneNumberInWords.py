'''
def NumberWords(phone):
    NumberToWords = {'1': 'One','2' : 'Two','3':'Three','4' : 'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','0':'Zero'}
    phonenum = []
    for num in phone:
        phonenum.append(NumberToWords[num])
    print(' '.join(' '.join(word.split()) for word in phonenum))
phone = input("Enter your Phone Number: ")
NumberWords(phone)
'''
'''
def NumberWords(phone):
    NumberToWords = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '0': 'Zero'}
    phonenum = []
    for char in phone:
            phonenum.append(NumberToWords[char])
    print(' '.join(' '.join(word.split()) for word in phonenum))
phone = input("Enter your Phone Number: ")
NumberWords(phone)
'''
def NumberWords(phone):
    NumberToWords = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine', '0': 'Zero'}
    output = ""
    for ch in phone:
        output += NumberToWords.get(ch, "!")+ " "
    return output
phone = input("Enter your Phone Number: ")
print(NumberWords(phone))