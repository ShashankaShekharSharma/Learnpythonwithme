# A data entry operator has a faulty keyboard. The keys 0 and 1 are very unreliable. Sometimes they work and sometimes they don't. While entering phone numbers into a database, the operator uses 'l' as a replacement of 1 and 'o' as a relacement of 0 whenever these binary digits let him down. Both 'l' and 'o' are in lower case. 
# Accept a 10 digit number as input. Find the number of places where the numbers 0 and 1 have been relaced by letters. If there is no mistakes print the string "No Mistakes", if not print the number of replacement and in the next line print the correct phone number
a = input()
count = 0
num = ""
for i in range(len(a)):
    if a[i] == 'l':
        count += 1
        num += '1'
    elif a[i] == 'o':
        count += 1
        num += '0'
    else:
        num += a[i]

if count == 0:
    print("No Mistakes")
else:
    print(f"{count} Mistakes\n{a}")