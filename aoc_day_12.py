from collections import defaultdict, Counter

file = 'input_puzzles/day_12_test.txt'

# Create a dict with all nodes and connections #
with open(file, 'r') as f:
    graphs = defaultdict(list)
    for line in f.read().splitlines():
        a, b = line.split('-')
        graphs[a].append(b)
        graphs[b].append(a)

_cave_name_len = len(graphs['start'][0])  # Assumes start and end are never directly connected


def find_first_lowercase(s):
    """Function returns first lowercase letter and '' if there are none"""
    lowercases = [ii for ii in s if ii.islower()]
    if not lowercases:
        return ''
    else:
        return lowercases[0]


def pathfinder(startvert='start', visited={'start'}, current_path='', pathcount={}):
    """Function to find all paths through the cave system from given startvertex
       Returns: Dictionary of all paths
     """

    for vert in graphs[startvert]:
        if vert in visited and vert.islower():
            continue
        elif vert == 'end':
            pathcount[current_path] = 1
            continue
        else:
            if vert.islower():
                visited.add(vert)
            current_path += vert
            pathfinder(vert, visited, current_path, pathcount)

            # Removes path again from visited and current path after recursion step #
            current_path = current_path[:-_cave_name_len]
            if vert.islower():
                visited.remove(vert)
    return pathcount


print(f'Part 1: {len(pathfinder())}')
