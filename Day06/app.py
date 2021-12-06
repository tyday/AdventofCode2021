# Advent of Code /home/pi/Programming/AdventOfCode/2021/Day06/input.txt
#
# Created: 12-06-2021 08:17:31
# Creator: Ty Day

import time


def part_one(data):
    part_one = data[:]
    day = 0
    start_time = time.time()
    while day < 80:
        round_time = time.time()
        day += 1
        new_fish = []
        for i in range(len(part_one)):
            part_one[i] -= 1
            if part_one[i] == -1:
                part_one[i] = 6
                new_fish.append(8)
        part_one = part_one + new_fish
        if time.time() - round_time > 1:
            print(f"Iteration {day} took {time.time() - round_time: .2f}")

    print(len(part_one))
    print(f'Time: {time.time() - start_time: .2f}')


def part_two(data):
    day = 1
    adult_fish = [0, 0, 0, 0, 0, 0, 0]
    baby_fish = [0, 0, 0, 0, 0, 0, 0]
    for fish in data:
        adult_fish[fish] += 1
    print("Start fish: ", adult_fish)

    while True:
        for step in range(7):
            baby_step = step + 2
            baby_fish[baby_step % 7] = adult_fish[step]
            adult_fish[step] = adult_fish[step] + baby_fish[step]
            baby_fish[step] = 0
            # print(f'After {day}: [{sum(adult_fish)+sum(baby_fish)}]- A {adult_fish} - B {baby_fish}')
            # input()
            if day == 256:
                print(
                    f'After {day}: [{sum(adult_fish)+sum(baby_fish)}]- A {adult_fish} - B {baby_fish}')
                return
            day += 1


if __name__ == '__main__':
    data = ''
    with open('/home/pi/Programming/AdventOfCode/2021/Day06/input.txt') as f:
        data = f.read().strip()
        data = data.split('\n')

    data = [int(d) for d in data[0].split(',')]
    test_data = [3, 4, 3, 1, 2]

    # part_one(data)

    part_two(data)
