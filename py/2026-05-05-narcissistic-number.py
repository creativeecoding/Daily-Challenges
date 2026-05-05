"""
Challenge: Narcissistic Number
Description: Given a positive integer, determine whether it is a narcissistic number.
A number is narcissistic if the sum of each of its digits raised to the power of the total number of digits equals the number itself.
"""
def is_narcissistic(n):
    # Calculate the total number of digits
    length = len(str(n))
    
    # Use a temporary variable for the loop to preserve the original n
    temp = n
    total_sum = 0
    
    while temp > 0:
        res = (temp % 10) ** length
        temp //= 10
        total_sum += res
        
    # Check if the calculated sum equals the original number
    return total_sum == n
