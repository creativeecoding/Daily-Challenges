"""
Challenge: Sum of Differences
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-26
"""

def sum_of_differences(nums):
    if len(nums) < 2:
        return 0
        
    return nums[-1] - nums[0]
