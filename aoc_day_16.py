from collections import defaultdict
from functools import reduce

file = 'input_puzzles/day_16.txt'


def hex_to_bin(hex_input):
    return bin(int(hex_input, 16))[2:].zfill(len(hex_input) * 4)


def decode(bin_input, ii, final_dict):
    # Termination condition for recursion
    if '1' not in bin_input[ii:]:
        return ii, final_dict['value'], final_dict

    # Get version and type ID and append to dict
    final_dict['versions'].append(int(bin_input[ii:ii + 3], 2))
    final_dict['IDs'].append(typeID := int(bin_input[ii + 3:ii + 6], 2))
    ii += 6

    # Extraction of literal number
    if typeID == 4:
        literal = ''

        while True:
            breaker = int(bin_input[ii]) == 0
            literal += bin_input[ii + 1:ii + 5]
            ii += 5
            if breaker:
                break
        final_dict['literals'].append(int(literal, 2))

        return ii, int(literal, 2), final_dict

    lengthID = int(bin_input[ii])
    # Extraction of subpacket by length
    if lengthID == 0:
        length = int(bin_input[ii + 1:ii + 16], 2)
        ii += 16
        breaker = ii + length
        numbers = []

        while ii < breaker:
            ii, res, final_dict = decode(bin_input, ii, final_dict)
            numbers.append(res)

    # Extraction of subpacket by number of packets
    elif lengthID == 1:
        subpacks = int(bin_input[ii + 1:ii + 12], 2)
        ii += 12
        numbers = []

        for _ in range(subpacks):
            ii, res, final_dict = decode(bin_input, ii, final_dict)
            numbers.append(res)

    # Append value from operation on subpackets
    value = operator(numbers, typeID)
    final_dict['value'] = value
    return ii, value, final_dict


def operator(subpack, id):
    if id == 0:
        return sum(subpack)
    elif id == 1:
        return reduce(lambda x, y: x*y, subpack)
    elif id == 2:
        return min(subpack)
    elif id == 3:
        return max(subpack)
    elif id == 5:
        return int(subpack[0] > subpack[1])
    elif id == 6:
        return int(subpack[0] < subpack[1])
    elif id == 7:
        return int(subpack[0] == subpack[1])
    return


with open(file, 'r') as f:
    hex_data = f.read()

bin_data = hex_to_bin(hex_data)

res_1 = sum(decode(bin_data, 0, defaultdict(list))[2]['versions'])
res_2 = decode(bin_data, 0, defaultdict(list))[1]
print(f'Part 1: {res_1}')
print(f'Part 2: {res_2}')