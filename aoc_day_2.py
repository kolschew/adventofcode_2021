import pandas as pd

# Today I use pandas for a nice dataframe of the input data #
df2_test = pd.read_csv('input_puzzles/day_2_test.txt', sep=' ', header=None, names=['direction', 'steps'])
df2 = pd.read_csv('input_puzzles/day_2.txt', sep=' ', header=None, names=['direction', 'steps'])


def position_determiner(route):
    vert_pos = 0
    hor_pos = 0
    for idx, dir in enumerate(route['direction']):
        if dir == 'forward':
            hor_pos += route['steps'][idx]
        elif dir == 'up':
            vert_pos -= route['steps'][idx]
        elif dir == 'down':
            vert_pos += route['steps'][idx]
        else:
            raise KeyError('Direction unknown!')
    return hor_pos, vert_pos


def position_determiner_aim(route):
    vert_pos = 0
    hor_pos = 0
    aim = 0
    for idx, dir in enumerate(route['direction']):
        if dir == 'forward':
            hor_pos += route['steps'][idx]
            vert_pos += route['steps'][idx] * aim
        elif dir == 'up':
            aim -= route['steps'][idx]
        elif dir == 'down':
            aim += route['steps'][idx]
        else:
            raise KeyError('Direction unknown!')
    return hor_pos, vert_pos


print(f'Result of the first puzzle is {position_determiner(df2)[0] * position_determiner(df2)[1]}.')
print(f'Result of the second puzzle is {position_determiner_aim(df2)[0] * position_determiner_aim(df2)[1]}.')
