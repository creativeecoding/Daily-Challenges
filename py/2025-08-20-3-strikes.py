"""
Challenge: 3 Strikes
Description: Given an integer between 1 and 10,000, return a count of how many numbers from 1 up to n have a square that contains at least one digit 3.
"""
def squares_with_three(n):
    cnt = 0
  
    for i in range(1, n + 1):
        # Calculate the square of the current number
        square = i * i
        
        # Convert to string to check for the presence of digit '3'
        if '3' in str(square):
            cnt += 1
            
    return cnt
