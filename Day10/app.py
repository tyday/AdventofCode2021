# Advent of Code /home/tyrda/LocalProgramming/AdventofCode2021/Day10/input.txt
#
# Created: 12-10-2021 07:29:30
# Creator: Ty Day
CLOSING_CHARS = {
    ')':'(',
    '}':'{',
    ']':'[',
    '>':'<'
}
CHAR_POINTS = {
    ')': 3,
    '}': 1197,
    ']': 57,
    '>': 25137
}
COMPLETE_POINTS = {
    '(': 1,
    '{': 3,
    '[': 2,
    '<': 4
}
def check_for_corruption(line):
    data = [c for c in line]
    stack = []
    while len(data) > 0:
        character = data.pop(0)
        if character in CLOSING_CHARS:
            if len(stack) < 1:
                # corrupt file. Close before open
                return character
            elif stack[-1] != CLOSING_CHARS[character]:
                # corrupt file. Wrong Character
                return character
            else:
                stack.pop(-1)
        else:
            stack.append(character)

    # If we've reached this point
    # The line is not corrupt
    auto_complete_points = 0
    while len(stack) > 0:
        last_char = stack.pop(-1)
        auto_complete_points *= 5
        auto_complete_points += COMPLETE_POINTS[last_char]
    return auto_complete_points
        


def part_one(data):
    points = 0
    for line in data:
        check = check_for_corruption(line)
        if check in CHAR_POINTS:
            points += CHAR_POINTS[check]
    print('Part one. Score:', points)
def part_two(data):
    points = []
    for line in data:
        check = check_for_corruption(line)
        if type(check) == int:
            points.append(check)
    points = sorted(points)
    print(points)
    print('Part two. Score:', points[len(points)//2])

if __name__ == '__main__':
    data = ''
    with open('/home/tyrda/LocalProgramming/AdventofCode2021/Day10/input.txt') as f:
        data = f.read().strip()
        data = data.split('\n')
    
    part_one(data)
    part_two(data)

    # print('asdflad')
    # print(check_for_corruption('<{([{{}}[<[[[<>{}]]]>[]]'))