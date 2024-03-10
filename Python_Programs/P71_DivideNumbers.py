def divide(numerator,denominator):
    try:
        result = numerator/denominator
        print(f"The Result is: {result}")
    except ZeroDivisionError:
        print("Division by Zero is not possible")
    finally:
        print("Calculation Completed")
a,b = map(int,input("Enter the numerator and denominator separated by space: ").split(" "))
divide(a,b)