"""
Challenge: ISBN-13 Validator
Description: Given a string, determine if it is a valid ISBN-13 number.
A valid ISBN-13 contains only digits and hyphens, has exactly 13 digits 
after removing hyphens, and passes a mathematical check where the sum of 
each digit multiplied by 1 or 3 alternatingly is divisible by 10.
"""
def is_valid_isbn_13(s):
    # Check for invalid characters (only digits and hyphens are allowed)
    for char in s:
        if not char.isdigit() and char != '-':
            return False
            
    clean_isbn = s.replace('-', '')
    
    # Must contain exactly 13 digits
    if len(clean_isbn) != 13:
        return False
        
    total_sum = 0
    
    for i in range(13):
        digit = int(clean_isbn[i])
        
        # Multiply by 1 for even indices and by 3 for odd indices
        if i % 2 == 0:
            total_sum += digit * 1
        else:
            total_sum += digit * 3
            
    return total_sum % 10 == 0
