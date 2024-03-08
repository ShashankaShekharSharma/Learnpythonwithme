def average(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum/len(numbers)
num = map(int,input("Enter the numbers separated by space ").split(' '))
print(average(*num))
# *number is considered as a tuple