"""
Challenge: Vowel Balance
Description: Check if the number of vowels in the first half of a string is equal to the number of vowels in the second half. 
If the string length is odd, the middle character is ignored.
"""
def is_balanced(s):
    vowels = 'aeiouAEIOU'
    mid = len(s) // 2
    
    # Count vowels in the first half
    cnt1 = 0
    for char in s[:mid]:
        if char in vowels:
            cnt1 += 1
            
    # Count vowels in the second half using negative indexing
    cnt2 = 0
    for char in s[-mid:]: 
        if char in vowels:
            cnt2 += 1
            
    return cnt1 == cnt2
