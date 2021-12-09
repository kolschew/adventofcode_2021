file = 'input_puzzles/day_9.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()


class HeatmapAnalyzer:

    def __init__(self, heatmap=data):
        self.heatmap = heatmap
        self.xsize = len(self.heatmap[0])
        self.ysize = len(data)
        self.low_points = self.find_safe_points()

    def find_neighbours(self, ypos, xpos):
        neighbours = []
        for xx in [xpos - 1, xpos + 1]:
            if 0 <= xx < self.xsize:
                neighbours.append((ypos, xx))
            else:
                pass
        for yy in [ypos - 1, ypos + 1]:
            if 0 <= yy < self.ysize:
                neighbours.append((yy, xpos))
            else:
                pass
        return neighbours

    def find_safe_points(self):
        safe_points = []
        for xx in range(self.xsize):
            for yy in range(self.ysize):
                if int(self.heatmap[yy][xx]) < min(int(self.heatmap[i][j]) for i, j in self.find_neighbours(yy, xx)):
                    safe_points.append((yy, xx))
                else:
                    pass
        return safe_points

    def find_basins(self, loc, visited, basins):
        for pos in self.find_neighbours(loc[0], loc[1]):
            if pos not in visited:
                visited.append(pos)
                if int(self.heatmap[pos[0]][pos[1]]) != 9:
                    basins.append(pos)
                    self.find_basins(pos, visited, basins)
        return basins


heat = HeatmapAnalyzer()
res1 = sum([int(heat.heatmap[i[0]][i[1]]) + 1 for i in heat.find_safe_points()])
res2 = [len(heat.find_basins(pos, [pos], [pos])) for pos in heat.low_points]
res2.sort(reverse=True)

print(f'Part 1: {res1}')
print(f'Part 2: {res2[0] * res2[1] * res2[2]}')