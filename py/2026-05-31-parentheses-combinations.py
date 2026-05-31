"""
Challenge: Parentheses Combinations
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-31
"""
import math


def get_combinations(n):
    return math.comb(2 * n, n) // (n + 1)
