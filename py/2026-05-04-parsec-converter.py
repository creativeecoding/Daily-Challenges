"""
Challenge: Parsec Converter
Description: In a distant galaxy, parsecs are used to measure both time and distance. 
Given an integer number of parsecs, return its equivalent in time or distance. 
If the given integer is odd, it represents time (multiplier 2). If it's even, it represents distance (multiplier 3).
Return the converted value as an integer.
"""
def convert_parsecs(parsecs):
    # If the number is odd, it represents time
    if parsecs % 2 != 0:
        return parsecs * 2
    # If the number is even, it represents distance
    else:
        return parsecs * 3
