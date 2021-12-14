from collections import defaultdict, Counter

file = 'input_puzzles/day_12.txt'

# Create a dict with all nodes and connections #
with open(file, 'r') as f:
    graphs = defaultdict(list)
    for line in f.read().splitlines():
        a, b = line.split('-')
        graphs[a].append(b)
        graphs[b].append(a)

_cave_name_len = len(graphs['start'][0])  # Assumes start and end are never directly connected


# My first attempt to part 1, which I was not able to make work for part 2 unfortunately
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
            current_path = current_path[:-_cave_name_len]
            if vert in visited:
                visited.remove(vert)
    return pathcount


# Someone elses basic architecture which I restructured to return all paths in a list #
def count_paths(final_paths, cave="start", visited={"start"}, path='start', allow_small_cave=False) -> list[str]:
    if cave == "end":
        final_paths.append(path)
        return
    for nb in graphs[cave]:
        if nb.isupper():
            path += f' {nb} '
            count_paths(final_paths, nb, visited, path, allow_small_cave)
        elif nb not in visited:
            path += f' {nb} '
            count_paths(final_paths, nb, visited | {nb}, path, allow_small_cave)
        elif allow_small_cave and nb != "start":
            path += f' {nb} '
            count_paths(final_paths,nb, visited, path, False)
    return final_paths


print(f'Part 1: {len(pathfinder())}')
print(f'Part 2: {len(count_paths([], allow_small_cave=True))}')
