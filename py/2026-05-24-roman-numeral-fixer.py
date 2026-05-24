"""
Challenge: Roman Numeral Fixer
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-24
"""

def fix_numerals(s):
    char_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = sum(char_values[char] for char in s)
    
    roman_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    result = ""
    for value, symbol in roman_map:
        while total >= value:
            result += symbol
            total -= value
            
    return result
