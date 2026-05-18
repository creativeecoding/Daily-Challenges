"""
Challenge: Bingo Range
Description: Given a bingo letter ("B", "I", "N", "G", "O"), return an array with all numbers in the range associated with that letter from smallest to largest.
"""
def get_bingo_range(letter):
    bingo_ranges = {
        "B": list(range(1, 16)),
        "I": list(range(16, 31)),
        "N": list(range(31, 46)),
        "G": list(range(46, 61)),
        "O": list(range(61, 76))
    }
    
    return bingo_ranges[letter]
