num = int(input("Enter a number: "))
numstring = str(num)  
digit_sum = 0  

for i in range(len(numstring)):
    digit_sum += int(numstring[i])

print("Sum of digits:", digit_sum)
