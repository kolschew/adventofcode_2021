from itertools import combinations
from collections import defaultdict


def read_data(file):
    with open(file, 'r') as f:
        scanner_raw = f.read().splitlines()
        scanner = []
        subscan = []
        for sc in scanner_raw[1:]:
            if sc:
                if '--- ' in sc:
                    scanner.append(tuple(subscan))
                    subscan = []
                else:
                    subscan.append(tuple([int(s) for s in sc.split(',')]))
    return tuple(scanner)


def distance(coord1, coord2):
    return sum([(p1 - p2) ** 2 for p1, p2 in zip(coord1, coord2)])


def analyze_distances(scanner):
    distances = defaultdict(list)
    for i, j in combinations(range(len(scanner)), 2):
        dist = distance(scanner[i], scanner[j])
        distances[dist].append(scanner[i])
        distances[dist].append(scanner[j])
    return distances


def all_beacons(allscanner):
    for scanner in allscanner:



puzzle = 'input_puzzles/day_19.txt'
example = 'input_puzzles/day_19_test.txt'
scanners = read_data(example)
