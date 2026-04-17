"""
Challenge: Base Check
Description: Determine if a string represents a valid number in a given base.
A number is valid if every character exists within the allowed digits for that specific base. The check is case-insensitive.
"""
def is_valid_number(n, base):
    # Define all possible digits and letters used in bases up to 36
    all_digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Slice the master string to get only the valid characters for the given base
    valid_chars = all_digits[:base]
    # Convert input to uppercase to handle case-insensitivity
    n = n.upper()
    for char in n:
        if char not in valid_chars:
            return False
    return True
