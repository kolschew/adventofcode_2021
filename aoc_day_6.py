"""
The solution to this problem could be brute forced, however this way it should be much faster!
The idea is to create a list, containing the amount of fish with the respective index representing the cycle the
fish is currently in. Then when popping the 0th element of the list all others also automatically reduce their cycle by
one. All left to be done is add the ones at that same position to the ones at cycle 6.
"""
from collections import Counter

with open('input_puzzles/day_6.txt', 'r') as f:
    data = f.read()
df5 = Counter([int(i) for i in data.split(',')])


def count_fish(fish_data, days):
    fish = [fish_data[i] for i in range(9)]
    for day in range(days):
        popped = fish.pop(0)
        fish.append(popped)
        fish[6] += popped
    return sum(fish)


print(f'Part 1: {count_fish(df5, 80)}.')
print(f'Part 2: {count_fish(df5, 256)}.')
