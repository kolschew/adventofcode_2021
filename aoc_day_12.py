from collections import defaultdict

file = 'input_puzzles/day_12_test.txt'

with open(file, 'r') as f:
    graphs = defaultdict(list)
    for line in f.read().splitlines():
        a, b = line.split('-')
        graphs[a].append(b)
        graphs[b].append(a)

_small_caves = [key for key in graphs.keys() if key.islower()]


def pathfinder(startvert, visited, current_path, pathcount):
    for vert in graphs[startvert]:
        print(vert)
        if vert in visited and vert in _small_caves:
            print(f'Small cave visited at {vert}')
            continue
        elif vert == 'end':
            print(f'End reached')
            pathcount[current_path] = 1
            print(f'Added {current_path} to pathcount')
            current_path = ''
            visited = {'start'}
            continue
        else:
            visited.add(vert)
            current_path += vert
            print(f'Restarting recursion at vertex {vert} and visited:{visited} and current path: {current_path}')
            pathfinder(vert, visited, current_path, pathcount)
    return pathcount
