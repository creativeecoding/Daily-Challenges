"""
Challenge: Jbelmud
Description: Transform a string by jumbling each word while keeping the first and last letters in place.
Letters between them are sorted alphabetically. 
The input is lowercase and contains no punctuation.
"""
def jbelmu(text):
    words = text.split()
    
    for i in range(len(words)):
        word = words[i]
        
        if len(word) > 2:
            first, last = word[0], word[-1]
            
            # Sort the characters between first and last
            mid_sorted = "".join(sorted(word[1:-1]))
            words[i] = first + mid_sorted + last
        else:
            words[i] = word
            
    # Reconstruct the sentence with original spacing
    return " ".join(words)
