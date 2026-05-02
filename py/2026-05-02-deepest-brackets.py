"""
Challenge: Deepest Brackets
Description: Given a string containing balanced brackets, return the content of the deepest nested brackets. 
Brackets can be any of the three types: (), [], and {}.
The input will always have a single deepest group.
For example, given "(hello (world))", return "world".
"""
def get_deepest_brackets(s):
    # Find the maximum nesting depth of the brackets
    max_depth = 0
    current_depth = 0
    
    for char in s:
        if char in "([{":
            current_depth += 1
            if current_depth > max_depth:
                max_depth = current_depth
        elif char in ")]}":
            current_depth -= 1
            
    # Extract only the characters located at the maximum depth
    deepest_content = ""
    current_depth = 0
    
    for char in s:
        if char in "([{":
            current_depth += 1
        elif char in ")]}":
            current_depth -= 1
        else:
            if current_depth == max_depth:
                deepest_content += char
                
    return deepest_content
