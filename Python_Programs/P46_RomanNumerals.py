def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}

    result = 0
    prev_value = 0

    for symbol in s:
        current_value = roman_dict[symbol]

        # If the value of the current symbol is greater than the previous one, subtract the previous value
        if current_value > prev_value:
            result += current_value - 2 * prev_value
        else:
            result += current_value

        prev_value = current_value

    return result
roman_numeral = input("Enter the Roman Numeral ")
result = roman_to_int(roman_numeral)
print(f"The integer representation of {roman_numeral} is: {result}")