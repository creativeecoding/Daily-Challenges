"""
Challenge: Good Day
Description: Given a time string in "HH:MM" format (24-hour clock), return the appropriate greeting:
"Good morning" for times 05:00 to 11:59
"Good afternoon" for times 12:00 to 17:59
"Good evening" for times 18:00 to 21:59
"Good night" for times 22:00 to 04:59
"""
def get_greeting(s):
    # Extract the hour as an integer from the "HH:MM" string
    hour = int(s.split(":")[0])
    
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 18:
        return "Good afternoon"
    elif 18 <= hour < 22:
        return "Good evening"
    else:
        return "Good night"
