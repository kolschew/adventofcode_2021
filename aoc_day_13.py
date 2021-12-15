import re
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

file = 'input_puzzles/day_13.txt'
with open(file, 'r') as f:
    puzzle_data = f.read()

# Using regex to find the different instructions (also for reminding me of regex) #
_coordinates = re.compile(r'\d+,\d+')
_foldaxis = re.compile(r'fold along ([xy]=\d+)')


class FoldingPaper:

    def __init__(self, data):
        self.instructions = self.parse_instructions(data)
        self.coordinates = self.get_coordinates(data)
        self.paper = self.parse_grid(self.coordinates)

    @staticmethod
    def get_coordinates(coords_in):
        """Parses all # of the paper as list of coords"""
        grid_coords = [tuple(map(int, xx.split(','))) for xx in re.findall(_coordinates, coords_in)]
        return grid_coords

    @staticmethod
    def parse_instructions(inst_in):
        """Parses the folding instructions as a list"""
        inst_list = []
        for inst in re.findall(_foldaxis, inst_in):
            inst_list.append([inst.split('=')[0], int(inst.split('=')[1])])
        return inst_list

    @staticmethod
    def parse_grid(coordinates):
        """Creates a 2d array for the paper with 1s and 0s"""
        xcoord = []
        ycoord = []
        for xx, yy in coordinates:
            xcoord.append(xx)
            ycoord.append(yy)
        grid = np.zeros([max(ycoord) + 1, max(xcoord) + 1], dtype=int)
        grid[ycoord, xcoord] = 1
        return grid

    @staticmethod
    def fold(paper, instruction):
        """
        Folds paper for given instruction. Input must be 2d array and list = [axis: str, position: int]
        Returns: Folded 2d array
        """
        axis, position = instruction[0], instruction[1]
        if axis == 'y':
            fold_onto = paper[:position, :]
            fold_over = np.flipud(np.delete(paper[position:, :], 0, axis=0))
        elif axis == 'x':
            fold_onto = paper[:, :position]
            fold_over = np.fliplr(np.delete(paper[:, position:], 0, axis=1))
        else:
            raise NameError('This axis does not exist')
        return fold_onto | fold_over

    @staticmethod
    def convert_paper_to_picture(paper):
        """Converts 2d array to pixels"""
        plt.imshow(paper, interpolation='nearest')
        return

    def fold_several(self, paper, instruction, folds=None):
        """Performs several subsequent folds. If folds is provided only that amount of folds will be done."""
        folded = deepcopy(paper)
        for idx, inst in enumerate(instruction):
            if idx == folds:
                break
            else:
                folded = self.fold(folded, inst)
        return folded


fp = FoldingPaper(puzzle_data)
print(f'Part 1: {np.sum(fp.fold(fp.paper, fp.instructions[0]))}')
fp.convert_paper_to_picture(fp.fold_several(fp.paper, fp.instructions)) # Part 2 :)