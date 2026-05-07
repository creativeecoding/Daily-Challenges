"""
Challenge: Longest Common Substring
Description: Given a string, return the longest substring that appears more than once.
The substrings can overlap.
"""
def get_longest_substring(s):
    string_length = len(s)
    
    for length in range(string_length - 1, 0, -1):
        
        for i in range(string_length - length + 1):
            substring = s[i:i+length]
            
            # If the first occurrence index is different from the last occurrence index
            # Means the substring appears more than once (even if overlapping)
            if s.find(substring) != s.rfind(substring):
                return substring
                
    return ""
