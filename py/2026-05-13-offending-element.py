"""
Challenge: Offending Element
Description: Given an array of integers that is sorted in ascending order except for one out-of-place element, return the index of that element.
If more than one element could be considered out of place, return the index of the first one.
"""
def find_offender(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            
            # Check if removing the current element fixes the sequence
            if i == 0 or arr[i - 1] <= arr[i + 1]:
                return i
                
            return i + 1
            
    return -1
