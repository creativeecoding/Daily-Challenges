"""
Challenge: Schema Validator Part 2
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-06-02
"""

def is_valid_schema(obj):
    return isinstance(obj.get("username"), str) and type(obj.get("posts")) in (int, float) and isinstance(obj.get("verified"), bool)
