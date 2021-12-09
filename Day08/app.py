# Advent of Code /home/tyrda/LocalProgramming/AdventofCode2021/Day08/input.txt
#
# Created: 12-08-2021 00:01:32
# Creator: Ty Day

#        0:      1:      2:      3:      4:
#         aaaa    ....    aaaa    aaaa    ....
#        b    c  .    c  .    c  .    c  b    c
#        b    c  .    c  .    c  .    c  b    c
#         ....    ....    dddd    dddd    dddd
#        e    f  .    f  e    .  .    f  .    f
#        e    f  .    f  e    .  .    f  .    f
#         gggg    ....    gggg    gggg    ....

#        5:      6:      7:      8:      9:
#         aaaa    aaaa    aaaa    aaaa    aaaa
#        b    .  b    .  .    c  b    c  b    c
#        b    .  b    .  .    c  b    c  b    c
#         dddd    dddd    ....    dddd    dddd
#        .    f  e    f  .    f  e    f  .    f
#        .    f  e    f  .    f  e    f  .    f
#         gggg    gggg    ....    gggg    gggg


def analyze_line_A(a):
    if len(a) != 10:
        raise Exception(f'Invalid line: %s' % a)
    number_map = {x:None for x in range(10)}
    number_map[690] = []
    number_map[235] = []
    for i in a:
        if len(i) == 2 : number_map[1] = set(i)
        elif len(i) == 4 : number_map[4] = set(i)
        elif len(i) == 3 : number_map[7] = set(i)
        elif len(i) == 7 : number_map[8] = set(i)
        elif len(i) == 6 : number_map[690].append(set(i))
        elif len(i) == 5 : number_map[235].append(set(i))
        else:
            raise Exception("Error in analyze_line_A")
    number_map['a'] = set.symmetric_difference(number_map[1],number_map[7])
    number_map['cf'] = set.intersection(number_map[1],number_map[7])
    number_map[6],number_map['c'] = get_6(number_map)
    number_map[690].remove(number_map[6]) # 690 only contains 69
    number_map['f'] = set.symmetric_difference(number_map['c'], number_map['cf'])
    number_map[5] = get_5(number_map)
    number_map[235].remove(number_map[5]) # 235 only contains 23
    # Still need [0,2,3,9]
    number_map[3] = get_3(number_map)
    number_map[235].remove(number_map[3])
    number_map[2] = number_map[235][0]
    number_map[9] = get_9(number_map)
    number_map[690].remove(number_map[9])
    number_map[0] = number_map[690][0]

    return_map = {"".join(sorted(number_map[i])):i for i in range(10)}
    return return_map
def analyze_line_B(b, numbers):
    value = ''
    for line in b:
        value += str(numbers["".join(sorted(line))])
    return value
    

def get_9(numbers):
    data = numbers[690]
    for line in data:
        if numbers[4].issubset(line):
            return line
def get_3(numbers):
    # 2 and 3 
    data = numbers[235]
    for line in data:
        if numbers['f'].issubset(line):
            return line
def get_5(numbers):
    data = numbers[235]
    for line in data:
        if numbers['c'].issubset(line):
            pass
        else:
            return line

def get_6(numbers):
    data = numbers[690]
    six = c = None
    for line in data:
        if analyze_6(line, numbers[1]):
            six = line
            c = analyze_6(line, numbers[1])
    return six, {c}
    
def analyze_6(data, one):
    
    """Returns segment c if True else False"""
    for segment in one:
        if segment not in data:
            return segment
    return False
def analyze_9(data,seven):
    for segment in seven:
        if segment not in data:
            return False
    return True
def analyze_069(data, numbers, seg_numbers):
    zero,six,nine = None
    for line in data:
        if analyze_6(line, numbers[1]):
            six = line
            numbers[6] = six
            seg_numbers[six] = 6
    data.remove(six)
    for line in data:
        if analyze_9(line, numbers[7]):
            nine = line
            numbers[9] = nine
            seg_numbers[nine] = 9
    data.remove(nine)
    

def analyze_part_one(b):
    count = 0
    for line in b:
        if len(line) == 2 or len(line) == 3:
            count += 1
        elif len(line) == 4 or len(line) == 7:
            count += 1
    return count
def part_one(data):
    count = 0
    for line in data:
        a,b = line.split(' | ')
        a = a.split(' ')
        b = b.split(' ')
        count += analyze_part_one(b)
    print("Part one count:", count)

def part_two(data):
    # data = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
    total = 0
    for line in data:
        A, B = line.split(' | ')
        numbers = analyze_line_A(A.split(' '))
        value = analyze_line_B(B.split(' '), numbers)
        total += int(value)
    print(total)

if __name__ == '__main__':
    data = ''
    with open('/home/tyrda/LocalProgramming/AdventofCode2021/Day08/input.txt') as f:
    # with open('/home/tyrda/LocalProgramming/AdventofCode2021/Day08/test.txt') as f:
        data = f.readlines()
        data = [d.strip() for d in data]
    
    # part_one(data)
    part_two(data)
