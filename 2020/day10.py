from collections import Counter

def read_input(filename):
    with open(filename, 'r') as f:
        data = [int(x) for x in f.readlines()]
    # prepend 0 (charging outlet) and sort the data
    data = sorted([0] + data)
    # append highest value + 3 to represent the device
    data.append(data[len(data) - 1] + 3)
    return data
    
def part1(data):
    c = Counter(data[x] - data[x - 1] for x in range(1, len(data)))
    return c[1] * c[3]

def part2(data):
    # count dict will maintain number of ways to connect to each adapter
    count = { 0 : 1 }
    for adapter in data[1:]:
        count[adapter] = sum(count[i] for i in range(adapter - 3, adapter) if i in count)
    return count[data[-1]]

d = read_input("day10-test.txt")
print("part1-test: %d" % part1(d))
print("part2-test: %d" % part2(d))
d = read_input("day10.txt")
print("part1-real: %d" % part1(d))
print("part2-real: %d" % part2(d))