# Advent of Code /home/tyrda/LocalProgramming/AdventofCode2021/Day09/input.txt
#
# Created: 12-09-2021 11:03:21
# Creator: Ty Day




def part_one(data):
    shallows = []
    total = 0
    row = col = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            neighbors = []
            cell = data[row][col]
            if row != 0: neighbors.append(data[row-1][col]) # UP
            if row != len(data) - 1: neighbors.append(data[row + 1][col]) # DOWN
            if col != 0: neighbors.append(data[row][col-1]) # LEFT
            if col != len(data[row]) -1: neighbors.append(data[row][col + 1])
            if cell < min(neighbors):
                shallows.append((row,col))
                total += cell +1
            col += 1
        col = 0
        row += 1
    # print(shallows)
    print(f'Part One : {len(shallows)} -- {total}')
    return shallows
def get_neighbors(data,position,previously_checked):
    neighbors = []
    row, col = position
    value = data[row][col]
    if row != 0:
        UP = data[row-1][col]
        if UP < 9 and (row-1,col) not in previously_checked:
            neighbors.append((row-1,col))
    if row != len(data) - 1:
        DOWN = data[row + 1][col]
        if DOWN < 9 and (row + 1,col) not in previously_checked:
            neighbors.append((row+1,col)) # DOWN
    if col != 0:
        LEFT = data[row][col-1]
        if LEFT < 9 and (row,col-1) not in previously_checked:
            neighbors.append((row,col-1)) # LEFT
    if col != len(data[row]) -1:
        RIGHT = data[row][col+1]
        if RIGHT < 9 and (row,col+1) not in previously_checked:
            neighbors.append((row,col+1))   
    return neighbors

def part_two(data,shallows):
    WIDTH = len(data[0])
    HEIGHT = len(data)
    all_basins = []     # contains any location that is in a basin
    basins = []

    for position in shallows:
        basin = []
        if position in all_basins:
            pass
        else:
            neighbors = [position]
            while len(neighbors) > 0:
                sel = neighbors.pop(0)
                if sel in basin:
                    pass
                else:
                    all_basins.append(sel)
                    basin.append(sel)
                    neighbors += get_neighbors(data,sel,basin)
            basins.append(basin)
    print('Part two')
    basins = sorted([len(basin) for basin in basins])
    total = 1
    print(basins)
    for basin in basins[-3:]:
        print(basin)
        total *= basin
    print(total)


if __name__ == '__main__':
    data = ''
    with open('/home/tyrda/LocalProgramming/AdventofCode2021/Day09/input.txt') as f:
    # with open('/home/tyrda/LocalProgramming/AdventofCode2021/Day09/test.txt') as f:
        data = f.read().strip()
        data = data.split('\n')
    data = [[int(i) for i in d] for d in data]
    shallows = part_one(data)
    part_two(data,shallows)