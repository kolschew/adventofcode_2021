from dataclasses import dataclass
from collections import defaultdict

_uniques = [2, 3, 4, 7]


@dataclass
class SubmarineInterface:
    input: list
    output: list

    @classmethod
    def parser(cls, s: list):
        input = [i.split(' | ')[0] for i in s]
        output = [i.split(' | ')[1] for i in s]
        return cls(input, output)

    @staticmethod
    def count_unique_numbers(numbers: list):
        cnt = 0
        for num in ' '.join(numbers).split(' '):
            if len(num) in _uniques:
                cnt += 1
        return cnt

    @staticmethod
    def determine_wires(line):
        wires = defaultdict(set)
        while len(wires) < 10:
            for char in line.split(' '):
                if len(char) == 6 and wires[1].issubset(set(char)) and not wires[4].issubset(set(char)):
                    wires[0] = set(char)
                elif len(char) == 2:
                    wires[1] = set(char)
                elif len(char) == 5 and wires[1].issubset(set(char)):
                    wires[3] = set(char)
                elif len(char) == 4:
                    wires[4] = set(char)
                elif len(char) == 5 and wires[4].difference(wires[1]).issubset(set(char)):
                    wires[5] = set(char)
                elif len(char) == 6 and not wires[1].issubset(set(char)):
                    wires[6] = set(char)
                elif len(char) == 3:
                    wires[7] = set(char)
                elif len(char) == 7:
                    wires[8] = set(char)
                elif len(char) == 6 and wires[1].issubset(set(char)) and wires[4].issubset(set(char)):
                    wires[9] = set(char)
                elif len(char) == 5 and not set(char).issubset(wires[3]) and not set(char).issubset(wires[5]):
                    wires[2] = set(char)
                else:
                    pass
        return wires


file = 'input_puzzles/day_8_test.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

sf = SubmarineInterface.parser(data)

print(f'Part 1: {sf.count_unique_numbers(sf.output)}')