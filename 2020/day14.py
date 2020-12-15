import re
from functools import reduce

def stringToMask(str, key):
    mask = [(2 ** (35 - i)) for i in range(0, 36) if str[i] == key]
    if len(mask) == 0:
        return 0
    else:
        return reduce(lambda x, y: x + y, mask)

def part1(filename):
    maskParser = re.compile('^mask\s=\s([X01]{36})$')
    memParser = re.compile('^mem\[(\d+)\]\s=\s(\d+)$')
    memDict = {}

    with open(filename, 'r') as f:
        zeromask = 0
        onemask = 0
        for c, line in enumerate(f):
            if line[0:4] == "mask":
                m = maskParser.match(line)
                (zeromask, onemask) = (~stringToMask(m.group(1), '0'), stringToMask(m.group(1), '1'))
            else:
                m = memParser.match(line)
                (address, value) = (int(m.group(1)), int(m.group(2)))
                value = value & zeromask | onemask
                memDict[address] = value
        print(sum(memDict.values()))

def part2(filename):
    maskParser = re.compile('^mask\s=\s([X01]{36})$')
    memParser = re.compile('^mem\[(\d+)\]\s=\s(\d+)$')
    memDict = {}

    zeromask = 0
    onemask = 0

    with open(filename, 'r') as f:
        for c, line in enumerate(f):
            if line[0:4] == "mask":
                m = maskParser.match(line)
                (zeromask, onemask) = (stringToMask(m.group(1), '0'), stringToMask(m.group(1), '1'))
                xmask = [(2 ** (35 - i)) for i in range(0, 36) if m.group(1)[i] == 'X']
            else:
                m = memParser.match(line)
                (address, value) = (int(m.group(1)), int(m.group(2)))
                address = address & zeromask | onemask
                for i in range(2 ** len(xmask)):
                    it_onemask = 0
                    it_zeromask = 0xfffffffff
                    for j in range(len(xmask)):
                        if ((2 ** j) & i):
                            it_onemask |= xmask[j]
                            it_zeromask &= ~xmask[j]
                    memDict[address & it_zeromask | it_onemask] = value
                memDict[address] = value
    print(sum(memDict.values()))

part1('day14.txt')
part2('day14.txt')