"""
Challenge: Next Bingo Number
Description: Given a bingo number, return the next bingo number sequentially. 
A bingo number consists of a letter followed by a number in its specific range: 
B (1-15)
I (16-30) 
N (31-45)
G (46-60)
O (61-75). 
If given the last number "O75", it returns "B1".
"""
def get_next_bingo_number(n):
    # Extract the number from the string and increment it by 1 to get the next value
    number = int(n[1:]) + 1
    
    # Reset the sequence back to the first number "B1"
    if number > 75:
        return "B1"
    
    letters = "BINGO"
  
    # Each letter covers a fixed range of exactly 15 numbers.
    # (number - 1) ensures the transition happens exactly at 16, 31, 46, and 61.
    idx = (number - 1) // 15
    
    return f"{letters[idx]}{number}"
