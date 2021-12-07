"""
This problem absolutely cries for numpy. Mathematically the position which has the least linear distance
to all datapoints is simply the median.
"""
import numpy as np

file = 'input_puzzles/day_7.txt'
df7 = np.loadtxt(file, delimiter=',')


def fuel_expanse_linear(positions):
    med = np.median(positions)
    fuel = np.sum(np.abs(positions - med * np.ones(len(positions))))
    return fuel


print(f'Part 1: {fuel_expanse_linear(df7)}')
