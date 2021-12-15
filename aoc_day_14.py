from collections import Counter

file = 'input_puzzles/day_14.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

# Python's dict() also creates a dictionary from a list of len-2 lists: dict([[Any, Any],...])
# even though pycharm marks this. Dict() does accept all arguments like dict(Iterable(Iterable(Any, Any)))

# noinspection PyTypeChecker
RULES = dict([s.split(' -> ') for s in data[2:]])
polystart = data[0]


# Finally defined a successful recursive function!
def pair_insertion(polymer, cycles):
    if cycles == 0:
        return polymer
    sliced = [polymer[i:i+2] for i in range(len(polymer)-1)]
    new_polymer = ''
    for slice in sliced:
        new_polymer += slice[0] + RULES[slice]
    return pair_insertion(new_polymer + polymer[-1], cycles - 1)


count_occs_1 = Counter(pair_insertion(polystart, 10))
count_occs_2 = Counter(pair_insertion(polystart, 40))
print(f'Part 1: {count_occs_1.most_common(1)[0][1] - count_occs_1.most_common()[-1][1]}')
print(f'Part 2: {count_occs_2.most_common(1)[0][1] - count_occs_2.most_common()[-1][1]}')