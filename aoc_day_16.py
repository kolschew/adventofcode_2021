from collections import defaultdict
from functools import reduce

file = 'input_puzzles/day_16.txt'


def hex_to_bin(hex_input):
    return bin(int(hex_input, 16))[2:].zfill(len(hex_input) * 4)


def decode(bin_input, ii, final_dict):
    # Termination condition for recursion
    if '1' not in bin_input[ii:] or ii >= len(bin_input):
        return len(bin_input), final_dict

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

        return ii, final_dict

    lengthID = int(bin_input[ii])

    # Extraction of subpacket by length
    if lengthID == 0:
        length = int(bin_input[ii + 1:ii + 16], 2)
        ii += 16
        breaker = ii + length
        subdict = defaultdict(list)

        while ii <= breaker:
            ii, subdict = decode(bin_input, ii, subdict)

    # Extraction of subpacket by number of packets
    elif lengthID == 1:
        subpacks = int(bin_input[ii + 1:ii + 12], 2)
        ii += 12
        subdict = defaultdict(list)

        for cnt in range(subpacks):
            ii, subdict = decode(bin_input, ii, subdict)

    final_dict['versions'] += subdict['versions']
    final_dict['IDs'] += subdict['IDs']
    final_dict['literals'].append(appender(subdict['literals'], typeID))

    return ii, final_dict


def appender(subpack, id):
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


def tester(ids, literals, litcnt):
    for ii in range(len(ids)):
        if ids[ii] == 4:
            lit = literals[litcnt]
            litcnt += 1
            return lit
        else:
            return tester(ids[ii:], literals, litcnt)

with open(file, 'r') as f:
    hex_data = f.read()

bin_data = hex_to_bin(hex_data)

# Assertions for part 1 #
assert sum(decode(hex_to_bin('8A004A801A8002F478'), 0, defaultdict(list))[1]['versions']) == 16
assert sum(decode(hex_to_bin('620080001611562C8802118E34'), 0, defaultdict(list))[1]['versions']) == 12
assert sum(decode(hex_to_bin('C0015000016115A2E0802F182340'), 0, defaultdict(list))[1]['versions']) == 23
assert sum(decode(hex_to_bin('A0016C880162017C3686B18A3D4780'), 0, defaultdict(list))[1]['versions']) == 31

# Assertions for part 2 #
# assert decode(hex_to_bin('C200B40A82'), 0, defaultdict(list))[1]['literals'][0] == 3
# assert decode(hex_to_bin('04005AC33890'), 0, defaultdict(list))[1]['literals'][0] == 54
# assert decode(hex_to_bin('880086C3E88112'), 0, defaultdict(list))[1]['literals'][0] == 7
# assert decode(hex_to_bin('CE00C43D881120'), 0, defaultdict(list))[1]['literals'][0] == 9
# assert decode(hex_to_bin('D8005AC2A8F0'), 0, defaultdict(list))[1]['literals'][0] == 1
# assert decode(hex_to_bin('F600BC2D8F'), 0, defaultdict(list))[1]['literals'][0] == 0
# assert decode(hex_to_bin('9C005AC2F8F0'), 0, defaultdict(list))[1]['literals'][0] == 0
# assert decode(hex_to_bin('9C0141080250320F1802104A08'), 0, defaultdict(list))[1]['literals'][0] == 1

res_1 = sum(decode(bin_data, 0, defaultdict(list))[1]['versions'])
print(f'Part 1: {res_1}')