from collections import Counter
from _helpers import grouped_reader

def part1(input_data):
    total = 0
    for group in input_data:
        total = total + len(set([letter for subgroup in group for letter in subgroup]))
    return total

def part2(input_data):
    total = 0
    for group in input_data:
        counter = Counter([letter for subgroup in group for letter in subgroup])
        total = total + len([letter for letter in counter.keys() if counter[letter] == len(group)])
    return total
    
input_data = grouped_reader("day6-test.txt", lambda x: [char for char in x])
print("test.part1: %d " % part1(input_data))
print("test.part2: %d " % part2(input_data))
    
input_data = grouped_reader("day6.txt", lambda x: [char for char in x])
print("real.part1: %d " % part1(input_data))
print("real.part2: %d " % part2(input_data))