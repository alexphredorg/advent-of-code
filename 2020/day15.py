def game(numbers, turns):
    d = {}
    last = numbers[0]
    for i in range(1, len(numbers)):
        d[last] = i - 1
        last = numbers[i]

    for i in range(len(numbers), turns):
        if last in d:
            v = (i - 1) - d[last]
        else:
            v = 0
        numbers.append(v)
        d[last] = i - 1
        last = v
    return numbers[-1]

assert(game([0,3,6], 2020) == 436)
assert(game([1,3,2], 2020) == 1)
assert(game([2,1,3], 2020) == 10)
assert(game([1,2,3], 2020) == 27)
assert(game([2,3,1], 2020) == 78)
assert(game([3,2,1], 2020) == 438)
assert(game([3,1,2], 2020) == 1836)
print(game([0,13,16,17,1,10,6], 2020))
print(game([0,13,16,17,1,10,6], 30000000))