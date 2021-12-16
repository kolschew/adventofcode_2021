from collections import Counter
from numpy import ceil

file = 'input_puzzles/day_14.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

# Python's dict() also creates a dictionary from a list of len-2 lists: dict([[Any, Any],...])
# even though pycharm marks this. Dict() does accept all arguments like dict(Iterable(Iterable(Any, Any)))

# noinspection PyTypeChecker
RULES = dict([s.split(' -> ') for s in data[2:]])
polystart = data[0]


def count_pairs(polymer, cycles):
    """Recursively counts the number of pairs after n cycles """
    if cycles == 0:
        return polymer

    if type(polymer) == str:
        slices = [polymer[i:i + 2] for i in range(len(polymer) - 1)]
        polymer = Counter(slices)

    curr_pairs = Counter()
    for key, val in polymer.items():
        curr_pairs[key[0] + RULES[key]] += val
        curr_pairs[RULES[key] + key[1]] += val
    return count_pairs(curr_pairs, cycles - 1)


def count_chars(pairs):
    """
    Counts the characters in the final result of pairs.
    Because of overlap only half is added and ceil is used in the end
    """
    fullcount = Counter()
    for key, val in pairs.items():
        fullcount[key[0]] += 0.5 * val
        fullcount[key[1]] += 0.5 * val
    return Counter({key: int(ceil(val)) for key, val in fullcount.items()})


count_occs_1 = count_chars(count_pairs(polystart, 10))
count_occs_2 = count_chars(count_pairs(polystart, 40))
print(f'Part 1: {count_occs_1.most_common(1)[0][1] - count_occs_1.most_common()[-1][1]}')
print(f'Part 2: {count_occs_2.most_common(1)[0][1] - count_occs_2.most_common()[-1][1]}')