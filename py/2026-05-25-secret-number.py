"""
Challenge: Secret Number
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-25
"""

def guess_number(secret, guess):
    if secret > guess:
        return "higher"
    elif secret < guess:
        return "lower"
        
    return "you got it!"
