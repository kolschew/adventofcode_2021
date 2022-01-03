import re
from numpy import sign, heaviside

file = 'input_puzzles/day_17.txt'

with open(file, 'r') as f:
    area = f.readlines()
_xarea = list(map(int, re.findall(r'\d+', area[1])))[:2]
_yarea = list(map(int, re.findall(r'-\d+', area[1])))


class Trajectory:
    def __init__(self, velx, vely):
        self.velx = velx
        self.vely = vely

    def trajectory(self, steps):
        velx, vely = self.velx, self.vely
        xpath, ypath = 0, 0
        for t in range(steps):
            xpath += velx
            ypath += vely
            velx -= sign(velx)
            vely -= 1
        return xpath, ypath

    def highest_point(self):
        t = 0
        highest = 0
        while True:
            if self.trajectory(t)[1] >= highest:
                highest = self.trajectory(t)[1]
                t += 1
            else:
                break
        return highest

    def hits_target(self):
        t = 0
        while True:
            if (self.trajectory(t)[0] in range(_xarea[0], _xarea[1] + 1) and
                    self.trajectory(t)[1] in range(_yarea[0], _yarea[1] + 1)):
                return True
            elif self.trajectory(t)[0] > _xarea[1] or self.trajectory(t)[1] < _yarea[0]:
                return False
            t += 1


def find_highest():
    highest = []
    for x in range(_xarea[1]):
        for y in range(-_yarea[0] + 1):
            if Trajectory(x, y).hits_target():
                highest.append(Trajectory(x, y).highest_point())
    return max(highest)


def find_initials():
    cnt = 0
    for x in range(_xarea[1] + 1):
        for y in range(_yarea[0] - 1, -_yarea[0] + 2):
            if Trajectory(x, y).hits_target():
                cnt += 1
    return cnt


print(f'Part 1: {find_highest()}')
print(f'Part 2: {find_initials()}')
