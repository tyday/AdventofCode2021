# Advent of Code /home/tyrda/LocalProgramming/AdventofCode2021/Day14/input.txt
#
# Created: 12-18-2021 09:26:44
# Creator: Ty Day

from os import getrandom


def get_pairs(temp):
    pairs = []
    for i in range(len(temp)-1):
        pairs.append(temp[i] + temp[i+1])
    return pairs

def part_one(template, rules, steps):
    # pairs = get_pairs(template)
    # print(pairs)
    temp = template
    for i in range(steps):
        print("step:", i+1, "length:", len(temp))
        pairs = get_pairs(temp)
        last_letter = pairs[-1][-1]
        for j in range(len(pairs)):
            if pairs[j] in rules:
                pairs[j] = pairs[j][0] + rules[pairs[j]]
        temp = "".join(pairs) + last_letter
    # print(temp)
    print("Part one")
    print("length:", len(temp))
    element_dict = get_elements(temp)
    print("max - min", max_minus_min(element_dict))
    print()

def part_two(template, rules, steps):
    temp = template
    first_letter = template[0]
    pair_dict = get_pair_dict(temp)
    for i in range(steps):
        pair_dict_items = list(pair_dict.items())
        for pair, val in pair_dict_items:
            if val > 0:
                if pair in rules:
                    lett1 = pair[0]
                    lett2 = rules[pair]
                    lett3 = pair[1]
                    pair1 = lett1 + lett2
                    pair2 = lett2 + lett3
                    pair_dict[pair] = pair_dict.get(pair,0) - val
                    pair_dict[pair1] = pair_dict.get(pair1,0) + val
                    pair_dict[pair2] = pair_dict.get(pair2,0) + val
        # print(pair_dict)



    letter_dict = {first_letter:1}
    for pair in pair_dict:
        letter_dict[pair[1]] = letter_dict.get(pair[1],0) + pair_dict[pair]
    print("Part Two")
    # print(pair_dict)
    # print(letter_dict)
    print("max - min", max_minus_min(letter_dict))
    

def get_pair_dict(template):
    pairs = get_pairs(template)
    pair_dict = {}
    for pair in pairs:
        pair_dict[pair] = pair_dict.get(pair, 0) + 1
    return pair_dict


def get_rules(rules_list):
    rules = {}
    for rule in rules_list:
        idx,val = rule.split(' -> ')
        rules[idx] = val
    return rules
def get_elements(template):
    element_dict = {}
    for letter in template:
        if letter in element_dict:
            element_dict[letter] += 1
        else:
            element_dict[letter] = 1
    return element_dict

def max_minus_min(elements):
    max_value = max(elements.values())
    min_value = min(elements.values())
    return max_value - min_value

if __name__ == '__main__':
    data = ''
    with open('/home/tyrda/LocalProgramming/AdventofCode2021/Day14/input.txt') as f:
        data = f.read().strip()
        data = data.split('\n')
    
    # print(data)
    template = data[0]
    # rules = [rule.split(' -> ') for rule in data[2:]]
    rules = get_rules(data[2:])
    
    part_one(template,rules,10)
    part_two(template,rules,40)