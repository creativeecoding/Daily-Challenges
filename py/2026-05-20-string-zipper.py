"""
Challenge: String Zipper
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-20
"""

def zip_strings(a, b):
    result = ""
    min_length = min(len(a), len(b))
    
    for i in range(min_length):
        result += a[i] + b[i]
        
    result += a[min_length:] + b[min_length:]
    
    return result
