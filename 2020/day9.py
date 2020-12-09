def read_input(filename):
    with open(filename, 'r') as f:
        return [int(x.rstrip()) for x in f.readlines()]

def is_sumable(elements, value):
    for i in range(0, len(elements)):
        for j in range(i+1, len(elements)):
            if (elements[i] + elements[j]) == value: return True
    return False

def contig_sum(elements, value):
    for i in range(0, len(elements)):
        for j in range(i+1, len(elements)):
            s = sum(elements[i:j])
            if s > value: break
            if s == value: return (i, j)
    return None

def check_xmas(data, preamble = 25):
    for i in range(preamble, len(data)):
        elements = data[i-preamble:i]
        if not is_sumable(elements, data[i]):
            (start, stop) = contig_sum(data[0:i], data[i])
            sequence = data[start:stop]
            return (i, data[i], min(sequence) + max(sequence))
    return None

print(check_xmas(read_input("day9-test.txt"), 5))
print(check_xmas(read_input("day9.txt")))
