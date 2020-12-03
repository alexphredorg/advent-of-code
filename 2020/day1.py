with open('day1.txt', 'r') as f:
    values = f.readlines()

values = list(map(lambda x: int(x), values))
valuesDict = dict.fromkeys(values)

#for value in values:
#    if (2020 - value) in valuesDict:
#        print(value * (2020 - value))
#        exit()

for value1 in values:
    for value2 in values:
        for value3 in values:
            if value1 + value2 + value3 == 2020:
                print(value1 * value2 * value3)
                exit()