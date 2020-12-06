from collections import Counter
from _helper import read_grouped_input

def readinput(filename):
    output = []
    temp = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            if line == '':
                output.append(temp)
                temp = []
            else:
                temp.append([char for char in line])
        output.append(temp)
    return output

def part1(input_data):
    total = 0
    for group in input_data:
        total = total + len(set([letter for subgroup in group for letter in subgroup]))
    return total

def part2(input_data):
    total = 0
    subgroups = 0
    for group in input_data:
        counter = Counter([letter for subgroup in group for letter in subgroup])
        total = total + len([letter for letter in counter.keys() if counter[letter] == len(group)])
    return total
    
input_data = readinput("day6-test.txt")
print("test.part1: %d " % part1(input_data))
print("test.part2: %d " % part2(input_data))
    
input_data = readinput("day6.txt")
print("real.part1: %d " % part1(input_data))
print("real.part2: %d " % part2(input_data))