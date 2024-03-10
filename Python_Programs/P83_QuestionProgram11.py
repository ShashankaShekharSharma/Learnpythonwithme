# A phone number is belonging to a specific operator is valid if it satisfies all the following conditions:
# It should have 10 digits
# It should begin with 98123
# A digit can occur at most 5 times
# Keep accepting a phone number as input on each line. The last line of the input stream will have the word STOP
# Create a dictionary named D. The key should be the phone numbers. If a phone number is valid, if not, the value should be INVALID.
# Print the dictionary as output. The keys and values of the dictionary should be of type str. The keys should be added to the dictionary in the order in which they appear in the test-case area.
def validphone(phone_number):
    if len(phone_number) != 10:
        return False
    if phone_number[:5] == '98123':
        return False
    for i in phone_number:
        if phone_number.count(i)>5:
            return False
    return True
d = {}
while True:
    phone_number = input()
    if phone_number == "STOP":
        break
    if validphone(phone_number):
        d[phone_number] = "Valid"
    else:
        d[phone_number] = "Invalid"
print(d)