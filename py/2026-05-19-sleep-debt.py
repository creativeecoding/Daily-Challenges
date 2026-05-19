"""
Challenge: Sleep Debt
Description: Given an array of hours slept each night leading up to today, and a target number of hours per night, return how many hours of sleep you need tonight to eliminate your sleep debt.
"""

def sleep_debt(hours_slept, target_hours):
    total_target = (len(hours_slept) + 1) * target_hours
    debt = total_target - sum(hours_slept)
    
    # Return 0 if the target is already met or exceeded
    if debt < 0:
        return 0
        
    return debt
