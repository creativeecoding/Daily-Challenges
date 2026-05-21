"""
Challenge: I Before E
Description: Given a word or sentence, return a corrected version where every word follows the "I before E except after C" rule.
If a word contains "ei" not preceded by "c", replace it with "ie".
If a word contains "ie" preceded by "c", replace it with "ei".
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
