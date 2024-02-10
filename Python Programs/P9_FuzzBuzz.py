#FizzBuzz: Write a program that prints "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both.
a = int(input("Enter a number "))
def FizzBuzz(a):
    if a%3==0 and a % 5 ==0:
        print("FizzBuzz")
    elif a%3==0:
        print("Fizz")
    elif a%5==0:
        print("Buzz")
    else:
        print(a)
FizzBuzz(a)