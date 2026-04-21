"""
Challenge: Factorializer
Description: Calculate the factorial of an integer between 0 and 20.
The factorial of 0 is 1 and for n > 0 is the product of all integers from 1 to n.
"""
def factorial(n):
    # Factorial of 0 is 1
    if n == 0:
        return 1
    
    # Multiply n by the factorial of (n - 1)
    return n * factorial(n - 1)
