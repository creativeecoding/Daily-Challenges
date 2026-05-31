"""
Challenge: Pizza Party
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-27
"""
import math


def get_pizzas_to_order(hours_worked):
    total_slices = sum(max(2, math.ceil(hours / 3)) for hours in hours_worked)
    return math.ceil(total_slices / 8)
