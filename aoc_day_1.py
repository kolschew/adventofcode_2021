import numpy as np

# Import the puzzle data as numpy array #
df1 = np.loadtxt('input_puzzles/day_1.txt')


# Function for counting the number of increases to previous value #
def count_increase(data):
    prev_val = data[0]
    cnt = 0

    for curr_val in data:
        if prev_val < curr_val:
            cnt += 1
        prev_val = curr_val
    return cnt


# Function for counting the number of increases of consecutive sums if three #
def count_sum_increase(data):
    prev_sum = data[0] + data[1] + data[2]
    cnt = 0

    for idx in range(1, len(data) - 2):
        curr_sum = data[idx] + data[idx + 1] + data[idx + 2]
        if prev_sum < curr_sum:
            cnt += 1
        prev_sum = curr_sum
    return cnt
