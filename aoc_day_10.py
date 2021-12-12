from numpy import median


# Todays solution is maybe a little clumsy because I wrote it while on the train #
file = 'input_puzzles/day_10.txt'

with open(file, 'r') as f:
    input = f.read().splitlines()

_opener = ['(', '[', '{', '<']
_closer = [')', ']', '}', '>']
_pairing_closer = {_closer[i]: _opener[i] for i in range(len(_opener))}
_pairing_opener = {_opener[i]: _closer[i] for i in range(len(_opener))}
_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}


def check_corruption(line):
    res = []
    for char in line:
        if char in _opener:
            res.append(char)
        else:
            if _pairing_closer[char] != res[-1]:
                return char
            else:
                res.pop(-1)
    return


def find_incompletes(line):
    res = []
    for char in line:
        if char in _opener:
            res.append(char)
        else:
            if _pairing_closer[char] != res[-1]:
                return 
            else:
                res.pop(-1)
    return [_pairing_opener[i] for i in res][::-1]


def autocorrect_score(line):
    fin = 0
    for char in line:
        fin = fin * 5
        fin += _closer.index(char) + 1
    return fin


res1 = sum(_scores[i] for i in [check_corruption(i) for i in input if check_corruption(i) != None])
incompletes = [find_incompletes(i) for i in input if find_incompletes(i) != None]
res2 = median([autocorrect_score(i) for i in incompletes])

print(f'Part 1: {res1}')
print(f'Part 2: {res2}')
