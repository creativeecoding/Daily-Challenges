"""
Challenge: Character Frequency
Description: Given a string, return a dictionary mapping each character to the number of times it appears.
"""
def get_frequency(s):
    char_counts = {}
    
    for char in s:
        # Update the count or add the character if it's new
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
            
    return char_counts
