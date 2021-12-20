from collections import defaultdict

file = 'input_puzzles/day_16_test.txt'


def hex_to_bin(hex_input):
    return bin(int(hex_input, 16))[2:].zfill(len(hex_input) * 4)


def decode(bin_input, ii, final_dict):
    if ii >= len(bin_input):
        return final_dict

    final_dict['versions'].append(version := int(bin_input[ii:ii + 3], 2))
    final_dict['IDs'].append(typeID := int(bin_input[ii + 3:ii + 6], 2))
    ii += 6

    if typeID == 4:
        literal = ''
        while True:
            breaker = int(bin_input[ii]) == 0
            literal += bin_input[ii + 1:ii + 5]
            ii += 5
            if breaker:
                break
        final_dict['literals'].append(int(literal, 2))

    lengthID = int(bin_input[ii])
    if lengthID == 0:
        length = int(bin_input[ii + 1:ii + 16], 2)

    return final_dict


with open(file, 'r') as f:
    hex_data = f.read()

bin_data = hex_to_bin(hex_data)
lit_test = hex_to_bin('D2FE28')