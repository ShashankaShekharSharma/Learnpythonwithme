class NegativeValueError(Exception):
    def __init__(self, value):
        super().__init__(f"Error: Cannot calculate square root of a negative number ({value}).")
def calculate_sqrt(number):
    try:
        if number < 0:
            raise NegativeValueError(number)
        sqrt = number ** 0.5
        return sqrt
    except NegativeValueError as e:
        return e
try:
    user_input = float(input("Enter a number to calculate its square root: "))
    result = calculate_sqrt(user_input)
    print(f"Square root: {result}")

except ValueError:
    print("Error: Please enter a valid number.")
except NegativeValueError as e:
    print(f"Error: {e}")