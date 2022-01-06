"""
Basic idea here is to reduce the snail numbers to a set
consisting of pairs holding the value of the snail number
and the depth in the original list. Then all operations
are performed on those numbers, which I found much easier.
"""


import ast
from numpy import floor, ceil
from copy import deepcopy


def levels(lst, depth=0):
    """Returns a list of lists containing the value of
    the snail number and its depth in the list.
    """
    if not isinstance(lst, list):
        yield [lst, depth]
    else:
        for sublist in lst:
            yield from levels(sublist, depth + 1)


def snail_add(lst1, lst2):
    """Adds two snail numbers"""
    for val in lst1:
        val[1] += 1
    for val in lst2:
        val[1] += 1
    return lst1 + lst2


def explode(lst):
    """Performs the 'explode' operation"""
    for i, val in enumerate(lst):
        if val[1] > 4:
            left, right = lst.pop(i), lst.pop(i)
            if i == 0:
                lst[i] = [lst[i][0] + right[0], lst[i][1]]
                lst.insert(i, [0, right[1] - 1])
            elif i == len(lst):
                lst[i - 1] = [lst[i - 1][0] + left[0], lst[i - 1][1]]
                lst.append([0, left[1] - 1])
            else:
                if left[1] == lst[i - 1][1] + 1:
                    lst[i - 1] = [lst[i - 1][0] + left[0], lst[i - 1][1]]
                    lst[i] = [lst[i][0] + right[0], lst[i][1]]
                    lst.insert(i, [0, right[1] - 1])
                else:
                    lst[i - 1] = [lst[i - 1][0] + left[0], lst[i - 1][1]]
                    lst[i] = [lst[i][0] + right[0], lst[i][1]]
                    lst.insert(i, [0, right[1] - 1])
            break
    return lst


def split(lst):
    """Performs the 'split' operation"""
    for i, val in enumerate(lst):
        if val[0] >= 10:
            lst[i] = [int(ceil(val[0] / 2)), val[1] + 1]
            lst.insert(i, [int(floor(val[0] / 2)), val[1] + 1])
            break
    return lst


def reduce(lst):
    """Reduces a snail number"""
    while True:
        if any(val[1] > 4 for val in lst):
            explode(lst)
        elif any(val[0] >= 10 for val in lst):
            split(lst)
        else:
            break
    return lst


def magnitude(lst):
    """Recursively finds the magnitude of a snail number"""
    max_depth = max([val[1] for val in lst])

    if max_depth > 0:
        for i, val in enumerate(lst):
            if val[1] == max_depth:
                left, right = lst.pop(i), lst.pop(i)
                lst.insert(i, [3 * left[0] + 2 * right[0], right[1] - 1])
        return magnitude(lst)
    else:
        return lst[0][0]


def evaluate(input_nums):
    """Evaluates the list of snail numbers by adding all up"""
    nums = deepcopy(input_nums)
    res = nums[0]
    for num in nums[1:]:
        res = snail_add(res, num)
        reduce(res)
    return magnitude(res)


def largest_sum(nums):
    """Iterates through all snail numbers and returns the largest
    magnitude possible.
    """
    largest = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i == j:
                continue
            else:
                candidate = max(evaluate([nums[i], nums[j]]),
                                evaluate([nums[j], nums[i]]))

                if largest < candidate:
                    largest = candidate
    return largest


file = 'input_puzzles/day_18.txt'
with open(file, 'r') as f:
    numbers = f.read().splitlines()
numbers_orig = [ast.literal_eval(num) for num in numbers]
numbers = [list(levels(num)) for num in numbers_orig]

print(f'Part 1: {evaluate(numbers)}')
print(f'Part 2: {largest_sum(numbers)}')
