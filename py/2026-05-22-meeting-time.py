"""
Challenge: Meeting Time
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-22
"""

def get_meeting_time(availability):
    for t in range(24):
        if all(any(start <= t and end >= t + 1 for start, end in person) for person in availability):
            return t
            
    return "None"
