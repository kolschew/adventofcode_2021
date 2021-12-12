from copy import deepcopy
import numpy as np

file = 'input_puzzles/day_11.txt'
with open(file, 'r') as f:
    data_raw = f.read().splitlines()


class OctupusFlashes:

    def __init__(self, data_input):
        self.data = self.parser(data_input)
        self.xrange = len(self.data[0])
        self.yrange = len(self.data)

    @staticmethod
    def parser(data):
        return np.array([list(d) for d in data], dtype=int)

    def find_neighbours(self, ypos, xpos):
        """Finds neighbours around a given coordinate on the specified grid"""

        neighbours = [[], []]
        for xx in [xpos - 1, xpos, xpos + 1]:
            for yy in [ypos - 1, ypos, ypos + 1]:
                if xx == xpos and yy == ypos:
                    pass
                elif 0 <= xx < self.xrange and 0 <= yy < self.yrange:
                    neighbours[0].append(yy)
                    neighbours[1].append(xx)
                else:
                    pass
        return np.array(neighbours)

    def find_neighbours_vectorize(self, ypos, xpos):
        """Vectorized version of neighbour finding because np.vectorize does not understand my needs"""

        xneighbours = np.array([], dtype=int)
        yneighbours = np.array([], dtype=int)
        for ii in range(len(ypos)):
            yneighbours = np.append(yneighbours, self.find_neighbours(ypos[ii], xpos[ii])[0])
            xneighbours = np.append(xneighbours, self.find_neighbours(ypos[ii], xpos[ii])[1])
        return yneighbours, xneighbours

    def flash_cycle(self, input, cycles):
        """Function for the octopus cycles.
        Returns: field: Final constellation of octopi
                 flashcnt: Number of flashes that occured
                 fullsync: Cycles at which a full synchronization occured
        """

        field = deepcopy(input)
        fullsync = []
        flashcnt = 0
        for cyc in range(cycles):
            field += 1
            while np.any(field > 9):
                flasher = np.where(field > 9)
                flashcnt += len(flasher[0])
                yneighbours, xneighbours = self.find_neighbours_vectorize(flasher[0], flasher[1])

                field[field > 9] = 0
                for ii, yy in enumerate(yneighbours):
                    if field[yy][xneighbours[ii]] != 0:
                        field[yy][xneighbours[ii]] += 1
            if np.all(field == 0):
                fullsync.append(cyc + 1)
        return field, flashcnt, fullsync


oc = OctupusFlashes(data_raw)