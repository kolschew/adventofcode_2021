import pandas as pd
from collections import Counter

'''
Today I wrote a class for the task - just to try something different. Counter helps a lot with tasks where anything
needs to be counted. Especially .most_common is great - once you understand the syntax properly (which I now have).
In addition in pandas dataframes you can access the first letter in every line with .str[n] - which makes this task 
much simpler! 
'''

df3_test = pd.read_csv('input_puzzles/day_3_test.txt', header=None, dtype=str)[0]
df3 = pd.read_csv('input_puzzles/day_3.txt', header=None, dtype=str)[0]


class BinaryCounter:

    def __init__(self, data):
        self.data = data
        self.line_len = len(data[0])

    @staticmethod
    def max_occurrences(arr, pos):
        cnt = Counter(arr.str[pos])
        if cnt.most_common(2)[0][1] == cnt.most_common(2)[1][1]:
            occ = '1'
        else:
            occ = cnt.most_common(1)[0][0]
        return occ

    @staticmethod
    def min_occurrences(arr, pos):
        cnt = Counter(arr.str[pos])
        if cnt.most_common(2)[0][1] == cnt.most_common(2)[1][1]:
            occ = '0'
        else:
            occ = cnt.most_common()[-1][0]
        return occ

    def gamma_rate(self):
        fin = ''
        for pos in range(self.line_len):
            fin += self.max_occurrences(self.data, pos)
        return int(fin, 2)

    def epsilon_rate(self):
        fin = ''
        for pos in range(self.line_len):
            fin += self.min_occurrences(self.data, pos)
        return int(fin, 2)

    def oxygen_rate(self):
        ox_rate = self.data
        for pos in range(self.line_len):
            if len(ox_rate) == 1:
                break
            else:
                ox_rate = pd.DataFrame([i for i in ox_rate if i[pos] == self.max_occurrences(ox_rate, pos)])[0]
        return int(ox_rate[0], 2)

    def co2_rate(self):
        co2_rate = self.data
        for pos in range(self.line_len):
            if len(co2_rate) == 1:
                break
            else:
                co2_rate = pd.DataFrame([i for i in co2_rate if i[pos] == self.min_occurrences(co2_rate, pos)])[0]
        return int(co2_rate[0], 2)


bc = BinaryCounter(df3)

print(f'Part 1: {bc.gamma_rate() * bc.epsilon_rate()}')
print(f'Part 2: {bc.oxygen_rate() * bc.co2_rate()}')
