"""
Challenge: Schema Validator Part 1
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-06-01
"""

def is_valid_schema(obj):
    return isinstance(obj.get("username"), str)
