# Advent of Code Day 03
#
# Creator: Ty Day


def part_one(data, prnt=True):
    results = {}
    lengths = set([])
    for datum in data:
        lengths.add(len(datum))
        for i in range(len(datum)-1,-1,-1):
            if i not in results:
                results[i] = {0:0,1:0}
            results[i][int(datum[i])] += 1
    # print(lengths)
    # print(results)
    # for k,v in results.items():
    #     print(f'key {k:02d}: total: {v[0] + v[1]}')
    gamma_rate = ''
    epsilon_rate = ''
    for i in range(len(results)):
        val = results[i]
        if val[1] > val[0]:
            gamma_rate += '1'
            epsilon_rate += '0'
        elif val[0] > val[1]:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            # print(f'equal values at {i} - {results[i]}')
            gamma_rate += '1'
            epsilon_rate += '0'
    if prnt:
        print(f'gamma: {gamma_rate}\nepsilon: {epsilon_rate}')
        print(f'gamma: {int(gamma_rate,2)}\nepsilon: {int(epsilon_rate,2)}')
        print(f'{int(gamma_rate,2)} * {int(epsilon_rate,2)} = {int(gamma_rate,2) * int(epsilon_rate,2)}')
    return epsilon_rate, gamma_rate


def part_two(data,epsilon,gamma):
    print("\nPart Two\n")

    # Oxygen Rating
    oxygen_list = data[:]
    co2_list = data[:]
    i = 0
    while len(oxygen_list) > 1:
        oxygen_list = [o  for o in oxygen_list if o[i] == gamma[i]]
        discard, gamma = part_one(oxygen_list,False)
        i += 1
    i = 0
    while len(co2_list) > 1:
        co2_list = [o  for o in co2_list if o[i] == epsilon[i]]
        epsilon, discard = part_one(co2_list,False)
        i += 1
    print(oxygen_list)
    print(co2_list)
    print(f'{int(oxygen_list[0],2)} * {int(co2_list[0],2)} = {int(oxygen_list[0],2) * int(co2_list[0],2)}')
if __name__ == '__main__':
    data = ''
    with open('/home/pi/Programming/AdventOfCode/2021/Day03/day03.txt') as f:
    # with open('/home/pi/Programming/AdventOfCode/2021/Day03/test.txt') as f:
        data = f.read().strip()
        data = data.split('\n')
    print(len(data))
    epsilon, gamma = part_one(data)
    part_two(data,epsilon,gamma)