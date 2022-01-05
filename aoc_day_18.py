import ast
from numpy import floor, ceil

file = 'input_puzzles/day_18.txt'
with open(file, 'r') as f:
    numbers = f.read().splitlines()
numbers = [ast.literal_eval(num) for num in numbers]


def magnitude(lst):
    max_depth = max([val[1] for val in lst])

    if max_depth > 0:
        for i, val in enumerate(lst):
            if val[1] == max_depth:
                left, right = lst.pop(i), lst.pop(i)
                lst.insert(i, [3 * left[0] + 2 * right[0], right[1] - 1])
        return magnitude(lst)
    else:
        return lst[0][0]


def depth(lst):
    if isinstance(lst, list):
        return 1 + max(depth(item) for item in lst) if lst else 1
    else:
        return 0


def levels(lst, depth=0):
    if not isinstance(lst, list):
        yield [lst, depth]
    else:
        for sublist in lst:
            yield from levels(sublist, depth + 1)


def explode(lst):
    for i, val in enumerate(lst):
        if val[1] > 4:
            left, right = lst.pop(i), lst.pop(i)
            if i == 0:
                lst[i] = [lst[i][0] + right[0], right[1] - 1]
                lst.insert(i, [0, right[1] - 1])
            elif i == len(lst):
                lst[i - 1] = [lst[i - 1][0] + left[0], left[1] - 1]
                lst.append([0, left[1] - 1])
            else:
                if left[1] == lst[i - 1][1] + 1:
                    lst[i - 1] = [lst[i - 1][0] + left[0], left[1] - 1]
                    lst[i] = [lst[i][0] + right[0], lst[i][1]]
                    lst.insert(i, [0, right[1] - 1])
                else:
                    lst[i - 1] = [lst[i - 1][0] + left[0], lst[i - 1][1]]
                    lst[i] = [lst[i][0] + right[0], right[1] - 1]
                    lst.insert(i, [0, right[1] - 1])
            break
    return lst


def split(lst):
    for i, val in enumerate(lst):
        if val[0] > 10:
            lst[i] = [int(ceil(val[0] / 2)), val[1] + 1]
            lst.insert(i, [int(floor(val[0] / 2)), val[1] + 1])
            break
    return lst


def snail_add(lst1, lst2):
    for val in lst1:
        val[1] += 1
    for val in lst2:
        val[1] += 1
    return lst1 + lst2


test = [[[[[9,8],1],2],3],4]
test2 = list(levels([7,[6,[5,[4,[3,2]]]]]))
test3 = list(levels([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]))
test4 = list(levels([[[[0,7],4],[7,[[8,4],9]]],[1,1]]))