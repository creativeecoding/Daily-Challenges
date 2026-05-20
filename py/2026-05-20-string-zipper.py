"""
Challenge: String Zipper
Description: Given two strings, return a new string that interleaves their characters one at a time. 
If one string is longer, append the remaining characters at the end.
"""

def zip_strings(a, b):
    result = ""
    min_length = min(len(a), len(b))
    
    for i in range(min_length):
        result += a[i] + b[i]
        
    result += a[min_length:] + b[min_length:]
    
    return result
