# Advent of Code /home/tyrda/LocalProgramming/AdventofCode2021/Day13/input.txt
#
# Created: 12-18-2021 07:50:51
# Creator: Ty Day

def print_grid(dot_locations):
    max_x = max([i[0] for i in dot_locations])
    max_y = max([i[1] for i in dot_locations])
    for row in range(max_y + 1):
        for col in range(max_x+ 1):
            if (col,row) in dot_locations:
                print('#',end = '')
            else:
                print(' ', end='')
        print()


def get_instruction(instruction):
    direction, distance = instruction.split('=')
    direction = direction[-1]
    distance = int(distance)
    return direction, distance
def part_two(dot_locations, instructions):
    locations = dot_locations.copy()
    for instruction in instructions:
        locations = run_instruction(locations,instruction)

    print_grid(locations)
def part_one(dot_locations, instructions):
    p1 = run_instruction(dot_locations,instructions[0])
    print("Length of part 1 - ",len(p1))

def run_instruction(dot_locations, instruction):
    dot_locations = list(dot_locations)
    direction, distance = get_instruction(instruction)
    for i in range(len(dot_locations)):
        loc = dot_locations.pop(0)
        x,y = loc
        ox,oy = x,y # original x,y
        if direction == 'x':
            if x > distance:
                x = distance - (x-distance)
        elif direction == 'y':
            if y > distance:
                y = distance - (y-distance)
        dot_locations.append((x,y))
    return(set(dot_locations))



if __name__ == '__main__':
    data = ''
    with open('/home/tyrda/LocalProgramming/AdventofCode2021/Day13/input.txt') as f:
        data = f.read().strip()
        data = data.split('\n')
    
    # Split instructions off from data
    instructions = []
    dot_locations = []
    max_X = 0
    max_Y = 0
    for item in data:
        i = item.split(',')
        if len(i) == 1:
            if i[0] == '':
                # Don't add non instruction to instructions
                pass
            else:
                instructions.append(i[0])
        else:
            i[0] = int(i[0])
            i[1] = int(i[1])
            dot_locations.append((i[0],i[1]))
            if i[0] > max_X: max_X = i[0]   
            if i[1] > max_Y: max_Y = i[1]

    dot_locations = set(dot_locations)
    # print_grid(dot_locations)
    p1 = part_one(dot_locations,instructions)
    # print_grid(p1)
    # print(len(dot_locations))
    part_two(dot_locations,instructions)