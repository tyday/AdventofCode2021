with open('/home/pi/Programming/AdventOfCode/2021/Day02/day02.txt') as f:
    data = f.read()
    data = data.split('\n')
    horizontal = 0
    vertical = 0
    for datum in data:
        if len(datum) == 0:
            break
        direction, distance = datum.split()
        distance = int(distance)
        if direction == 'up':
            vertical -= distance
            if vertical < 0:
                vertical = 0
        elif direction == 'down':
            vertical += distance
        elif direction == 'forward':
            horizontal += distance
        else:
            print('Unknown command: {datum}')
    print(f'horizontal: {horizontal}, vertical: {vertical} = {horizontal * vertical}')

    # Part Two
    horizontal = 0
    vertical = 0
    aim = 0
    for datum in data:
        if len(datum) == 0:
            break
        direction, distance = datum.split()
        distance = int(distance)
        if direction == 'up':
            aim -= distance
            if vertical < 0:
                vertical = 0
        elif direction == 'down':
            aim += distance
        elif direction == 'forward':
            horizontal += distance
            vertical += aim * distance
        else:
            print('Unknown command: {datum}')
    print(f'horizontal: {horizontal}, vertical: {vertical} = {horizontal * vertical}')