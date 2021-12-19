import numpy as np

file = 'input_puzzles/day_15_test.txt'
with open(file, 'r') as f:
    data = f.read().split()

grid_input = np.array([list(d) for d in data], dtype=int)


class ShortestPath:
    def __init__(self, grid):
        self.grid = grid
        self.xsize = len(self.grid[0])
        self.ysize = len(self.grid)

    def generate_full_cave(self):
        new_map = np.array()
        xmap = self.grid
        for yy in range(5):
            for xx in range(5):
                if xx == yy == 0:
                    pass
                else:
                    next_segment = np.where(self.grid + yy + xx > 9, 1, self.grid + yy + xx)
                    xmap = np.concatenate((xmap, next_segment), axis=1)



    def find_neighbours(self, pos):
        """Finds neighbours around a given coordinate on the specified grid without diagonals"""
        neighbours = []
        ypos, xpos = pos
        for yy in [ypos - 1, ypos + 1]:
            if yy < 0 or yy >= self.ysize:
                pass
            else:
                neighbours.append((yy, xpos))
        for xx in [xpos - 1, xpos + 1]:
            if xx < 0 or xx >= self.xsize:
                pass
            else:
                neighbours.append((ypos, xx))
        return neighbours

    def dijkstra(self, start=(0, 0), end=None):
        if end is None:
            end = (self.ysize - 1, self.xsize - 1)

        to_visit = {start}
        distances = {start: 0}

        while to_visit != set():
            # Find the node with minimal distance in to_visit
            minsearch = {k: distances[k] for k in distances.keys() if k in to_visit}
            min_dist = min(minsearch, key=minsearch.get)

            # Check all neighbours of current minimal node
            for successor in self.find_neighbours(min_dist):
                compare = distances[min_dist] + self.grid[successor]
                if successor not in distances or compare < distances[successor]:
                    distances[successor] = compare
                    to_visit.add(successor)
                else:
                    pass

            to_visit.remove(min_dist)

        return distances[end]


sp = ShortestPath(grid_input)