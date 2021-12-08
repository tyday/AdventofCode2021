# Advent of Code /home/tyrda/LocalProgramming/AdventofCode2021/Day07/input.txt
#
# Created: 12-07-2021 08:58:55
# Creator: Ty Day
from time import time

def crab_gas(distance):
    fuel = 0
    for i in range(distance):
        fuel += i + 1
    return fuel

def part_one(data, data_dict):
    fuel_cost = []
    lowest_fuel = float("inf")
    lowest_fuel_position = 0
    for i in range(max(data)+1):
        fuel = 0
        for k,v in data_dict.items():
            fuel += abs(k-i) *v
        fuel_cost.append(fuel)
        if fuel < lowest_fuel:
            lowest_fuel = fuel
            lowest_fuel_position = i
    # print(fuel_cost)
    print(lowest_fuel)
    print("Lowest fuel:",lowest_fuel, "Position:",lowest_fuel_position)


def part_two(data,data_dict):
    start = time()
    fuel_cost = []
    fuel_cost_dict = {}
    lowest_fuel = float("inf")
    lowest_fuel_position = 0
    for i in range(max(data)+1):
        fuel = 0
        for k,v in data_dict.items():
            distance = abs(k - i)
            if distance not in fuel_cost_dict:
                fuel_cost_dict[distance] = crab_gas(distance)
            
            fuel += fuel_cost_dict[distance] *v
        fuel_cost.append(fuel)
        if fuel < lowest_fuel:
            lowest_fuel = fuel
            lowest_fuel_position = i
    # print(fuel_cost)
    print(lowest_fuel)
    print("Lowest fuel:",lowest_fuel, "Position:",lowest_fuel_position)
    print("time: {0:.2f}".format(time() - start))

if __name__ == '__main__':
    data = ''
    with open('/home/tyrda/LocalProgramming/AdventofCode2021/Day07/input.txt') as f:
        data = f.read().strip()
        data = data.split('\n')
    data = [int(d) for d in data[0].split(',')]
    print('Length:',len(data), 'max:', max(data), 'min:',min(data))
    # data = [16,1,2,0,4,2,7,1,2,14]
    data_dict = {}
    for i in data:
        if i in data_dict:
            data_dict[i] += 1
        else:
            data_dict[i] = 1
    # print(len(data_dict))

    
    part_one(data,data_dict)
    part_two(data,data_dict)
        
    