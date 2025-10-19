def roman_to_int(s):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for ch in reversed(s):
        value = roman_values[ch]
        if value < prev_value:
            total -= value   # Subtractive notation (e.g., IV = 4)
        else:
            total += value
        prev_value = value

    return total


# Example usage
roman = input("Enter a Roman numeral: ").upper()
print("Integer value:", roman_to_int(roman))
