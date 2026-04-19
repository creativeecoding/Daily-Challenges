"""
Challenge: Fibonacci Sequence
Description: Generate a Fibonacci sequence of a specific length starting from two given numbers.
Each subsequent number is the sum of the two preceding ones. 
If the length is 0 return an empty array.
"""
def fibonacci_sequence(start_sequence, length):
    # Handle the edge case for zero length
    if length == 0:
        return []
    
    # Initialize the result and handle lengths shorter than the start_sequence
    result = start_sequence[:length]
    
    # Generate the sequence until it reaches the target length
    while len(result) < length:
        # Calculate the next number by summing the last two elements
        next_number = result[-1] + result[-2]
        result.append(next_number)
        
    return result
