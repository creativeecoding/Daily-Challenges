"""
Challenge: Anagram Checker
Description: Determine if two strings are anagrams.
An anagram contains the exact same characters in any order.
"""
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    s1 = str1.lower().replace(" ", "")
    s2 = str2.lower().replace(" ", "")
    
    # If the sorted lists are identical they are anagrams
    return sorted(s1) == sorted(s2)
