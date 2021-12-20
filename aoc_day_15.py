import numpy as np
from copy import deepcopy

file = 'input_puzzles/day_15.txt'
with open(file, 'r') as f:
    data = f.read().split()

grid_input = np.array([list(d) for d in data], dtype=int)

# Code runs really slow - Check if heap increases runtime


class ShortestPath:
    def __init__(self, grid):
        self.grid = grid
        self.xsize = len(self.grid[0])
        self.ysize = len(self.grid)

    def generate_full_cave(self):
        """Generates map of the full cave row by row"""

        # Initialize new map, first row and first segment in that row
        new_map = np.zeros((self.ysize * 5, self.xsize * 5))
        xmap = deepcopy(self.grid)
        next_segment = deepcopy(self.grid)

        for yy in range(5):
            for xx in range(1, 5):
                next_segment = np.where(next_segment + 1 > 9, 1, next_segment + 1)
                xmap = np.concatenate((xmap, next_segment), axis=1)

            # Set a whole new row and reset variables for the next row the diagonal subgrid of the former one
            new_map[yy * self.ysize:(yy + 1) * self.ysize] = xmap
            next_segment = xmap[::, self.xsize:2 * self.xsize]
            xmap = xmap[::, self.xsize:2 * self.xsize]
        return new_map

    @staticmethod
    def find_neighbours(pos, grid):
        """Finds neighbours around a given coordinate on the specified grid without diagonals"""
        neighbours = []
        ysize, xsize = np.shape(grid)
        ypos, xpos = pos
        for yy in [ypos - 1, ypos + 1]:
            if yy < 0 or yy >= ysize:
                pass
            else:
                neighbours.append((yy, xpos))
        for xx in [xpos - 1, xpos + 1]:
            if xx < 0 or xx >= xsize:
                pass
            else:
                neighbours.append((ypos, xx))
        return neighbours

    def dijkstra(self, graph, start=(0, 0), end=None):
        """
        Dijkstra algorithm finds the shortest path between two nodes on a grid.
        If no input is provided, it starts in the top left and ends in the bottem right of the grid.
        Can be altered to return the best path by tracking the best predecessor to each node in a dictionary.
        """
        if end is None:
            end = (np.shape(graph)[0] - 1, np.shape(graph)[1] - 1)

        to_visit = {start}
        distances = {start: 0}

        while to_visit != set():
            # Find the node with minimal distance in to_visit
            minsearch = {k: distances[k] for k in distances.keys() if k in to_visit}
            min_dist = min(minsearch, key=minsearch.get)

            if min_dist == end:
                return distances[end]

            # Check all neighbours of current minimal node
            for successor in self.find_neighbours(min_dist, graph):
                compare = distances[min_dist] + graph[successor]
                if successor not in distances or compare < distances[successor]:
                    distances[successor] = compare
                    to_visit.add(successor)
                else:
                    pass

            # Remove minimal node from heap
            to_visit.remove(min_dist)

        return distances[end]


sp = ShortestPath(grid_input)