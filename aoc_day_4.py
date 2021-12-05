import pandas as pd
import numpy as np

"""
My idea for this solution was to first create an array for the numbers and one with arrays of the different 
bingo boards. Then while iterating through them I set every drawn number to -1 on the respective boards. Whenever
one of the rows (or transpose which means columns) would be a -1 vector, this would quantify as bingo for the first 
solution or the index would be memorized for the second solution to then subsequently delete the bingo boards until 
only one is left.
"""

file = 'input_puzzles/day_4.txt'
puzzle_size = 5
check = -np.ones(puzzle_size)

numbers_in = pd.read_csv(file, nrows=1, header=None).to_numpy()[0]
boards_raw = np.array(np.loadtxt(file, skiprows=1, usecols=range(puzzle_size)))
boards_in = np.vsplit(boards_raw, len(boards_raw)/puzzle_size)


def first_board(numbers, boards):
    final_board = np.copy(boards)
    for num in numbers:
        for board in final_board:
            board[board == num] = -1
            for ii in range(puzzle_size):
                if (board[ii] == check).all() or (board.transpose()[ii] == check).all():
                    board[board == -1] = 0
                    return sum(board.flatten()), num


def last_board(numbers, boards):
    final_board = np.copy(boards)
    for num in numbers:
        del_idx = []
        for idx, board in enumerate(final_board):
            board[board == num] = -1
            for ii in range(puzzle_size):
                if (board[ii] == check).all() or (board.transpose()[ii] == check).all():
                    if len(final_board) == 1:
                        final_board[final_board == -1] = 0
                        return sum(final_board.flatten()), num
                    else:
                        del_idx.append(idx)
        final_board = np.delete(final_board, del_idx, 0)


res1 = first_board(numbers_in, boards_in)
res2 = last_board(numbers_in, boards_in)
print(f'First part: {res1[0] * res1[1]}')
print(f'Second part: {res2[0] * res2[1]}')
