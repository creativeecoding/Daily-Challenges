"""
Challenge: I Before E
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-21
"""

def i_before_e(sentence):
    result = ""
    i = 0
    
    while i < len(sentence):
        if sentence[i:i+3] == "cie":
            result += "cei"
            i += 3
            
        elif sentence[i:i+2] == "ei":
            if i == 0 or sentence[i-1] != "c":
                result += "ie"
            else:
                result += "ei"
            i += 2
            
        else:
            result += sentence[i]
            i += 1
            
    return result
