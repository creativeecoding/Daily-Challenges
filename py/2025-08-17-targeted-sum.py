"""
Challenge: Targeted Sum
Description: Given an array of numbers and an integer target.
Find two unique numbers in the array that add up to the target value.
Return an array with the indices of those two numbers in ascending order.
"""
def find_target(arr, target):
  
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
          
            # Verify if the sum of the two elements equals the target
            if arr[i] + arr[j] == target:
                # Return the indices as a pair is found
                return [i, j]
              
    # Return the specific error message
    return "Target not found"
