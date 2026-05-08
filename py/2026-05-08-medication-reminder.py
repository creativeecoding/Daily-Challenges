"""
Challenge: Medication Reminder
Description: Given an array of medications and a string representing the current time, return the next medication you need to take and how long until you need to take it.
Each medication is in the format [name, lastTaken].
Return a string in the format "{name} in Hh Mm".
"""
def medication_reminder(medications, current_time):
    # Convert current time to total minutes from midnight
    current_time_mins = int(current_time[:2]) * 60 + int(current_time[3:])
    
    # Store schedules directly in minutes for a cleaner code
    # Deployxitrin: 08:00 (480) and 16:00 (960)
    # Debuggamanizole: 07:00 (420), 13:00 (780) and 21:00 (1260)
    fixed_schedules = {
        "Deployxitrin": [480, 960],
        "Debuggamanizole": [420, 780, 1260]
    }
    
    shortest_wait_time = float('inf')
    next_medication = ""
    
    for med_name, last_taken_str in medications:
        # Convert the last taken time to minutes
        last_taken_mins = int(last_taken_str[:2]) * 60 + int(last_taken_str[3:])
        next_dose_mins = 0
        
        if med_name == "Mergeflictamine":
            # Every 4 hours (240 minutes)
            next_dose_mins = last_taken_mins + 240
        else:
            found_dose_today = False
            for scheduled_dose_mins in fixed_schedules[med_name]:
                if scheduled_dose_mins > last_taken_mins:
                    next_dose_mins = scheduled_dose_mins
                    found_dose_today = True
                    break
                    
            # If all doses for today are done, the next one is the first dose tomorrow
            if not found_dose_today:
                next_dose_mins = fixed_schedules[med_name][0]
                
        # Calculate wait time from the current time
        wait_time_mins = (next_dose_mins - current_time_mins) % 1440
        
        # Check if this is the soonest medication
        if wait_time_mins < shortest_wait_time:
            shortest_wait_time = wait_time_mins
            next_medication = med_name
            
    # Convert the shortest wait time back to hours and minutes format
    hours_to_wait = shortest_wait_time // 60
    minutes_to_wait = shortest_wait_time % 60
    
    return f"{next_medication} in {hours_to_wait}h {minutes_to_wait}m"
