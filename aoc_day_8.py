"""
I used a dataclass for this task today just because I wanted to finally try it out. Also I was curious if it helps
to write a classmethod that parses the input and then a bunch of staticmethod to do the actual work on things.
Turns out this actually makes the code very readable and tidied up, so I might come back to this in the future.
There was no real necissity for the dataclass in the end however - anyways I still liked it.
"""
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
    def decode_wires(line: str):
        wires = defaultdict(set)
        while len(wires) < 10 or set() in wires.values():
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

    def decode_outputs(self, inputs: str, outputs: str):
        result = ''
        decode = self.decode_wires(inputs)
        for out in outputs.split(' '):
            result += str(list(decode.keys())[list(decode.values()).index(set(out))])
        return int(result)


file = 'input_puzzles/day_8.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()

sf = SubmarineInterface.parser(data)
res_p1 = sf.count_unique_numbers(sf.output)
res_p2 = sum([sf.decode_outputs(sf.input[ii], out) for ii, out in enumerate(sf.output)])

print(f'Part 1: {res_p1}')
print(f'Part 2: {res_p2}')
