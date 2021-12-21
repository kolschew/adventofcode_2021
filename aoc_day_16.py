from collections import defaultdict
file = 'input_puzzles/day_16.txt'


def hex_to_bin(hex_input):
    return bin(int(hex_input, 16))[2:].zfill(len(hex_input) * 4)


def decode(bin_input, ii, final_dict):
    # Termination condition for recursion
    if '1' not in bin_input[ii:] or ii >= len(bin_input):
        return len(bin_input), final_dict

    # Get version and type ID and append to dict
    version = int(bin_input[ii:ii + 3], 2)
    typeID = int(bin_input[ii + 3:ii + 6], 2)
    final_dict['versions'].append(version)
    final_dict['IDs'].append(typeID)
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

        while ii <= breaker:
            ii, final_dict = decode(bin_input, ii, final_dict)

        return ii, final_dict

    # Extraction of subpacket by number of packets
    elif lengthID == 1:
        subpacks = int(bin_input[ii + 1:ii + 12], 2)
        ii += 12

        for cnt in range(subpacks):
            ii, final_dict = decode(bin_input, ii, final_dict)

        return ii, final_dict


def appender(dict, subpack, id):
    if id == 0:
        dict['sum'].append(sum(subpack))
    elif id == 1:
        dict['']


with open(file, 'r') as f:
    hex_data = f.read()

bin_data = hex_to_bin(hex_data)
lit_test = hex_to_bin('D2FE28')
sub_len_test = hex_to_bin('38006F45291200')
sub_cnt_test = hex_to_bin('EE00D40C823060')
test_1 = hex_to_bin('8A004A801A8002F478')
test_2 = hex_to_bin('620080001611562C8802118E34')
test_3 = hex_to_bin('C0015000016115A2E0802F182340')
test_4 = hex_to_bin('A0016C880162017C3686B18A3D4780')

assert sum(decode(test_1, 0, defaultdict(list))[1]['versions']) == 16
assert sum(decode(test_2, 0, defaultdict(list))[1]['versions']) == 12
assert sum(decode(test_3, 0, defaultdict(list))[1]['versions']) == 23
assert sum(decode(test_4, 0, defaultdict(list))[1]['versions']) == 31