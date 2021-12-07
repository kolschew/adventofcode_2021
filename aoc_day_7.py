"""
This problem absolutely cries for numpy. Mathematically the position which has the least linear distance
to all datapoints is simply the median. For the second part the best alignment position is the mean rounded down
to the next integer, because we want to now weigh the difference accordingly. The closed form for a sum of integers is
known thanks to 7 year old Gauss: sum(x, 0, n) = (n^2 + n) / 2.
"""
import numpy as np

file = 'input_puzzles/day_7.txt'
df7 = np.loadtxt(file, delimiter=',')


def fuel_expanse_constant(positions):
    opt_dist = np.median(positions)
    fuel = np.sum(np.abs(positions - opt_dist))
    return fuel


def fuel_expanse_linear(positions):
    opt_dist = np.floor(np.mean(positions))
    fuel = np.sum((np.abs(positions - opt_dist) ** 2 + np.abs(positions - opt_dist)) / 2)
    return fuel


print(f'Part 1: {fuel_expanse_constant(df7)}')
print(f'Part 2: {fuel_expanse_linear(df7)}')
