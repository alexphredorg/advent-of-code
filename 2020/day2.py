import re

with open('day2.txt', 'r') as f:
    lines = f.readlines()

prog = re.compile('(\d+)-(\d+) (\w): (\w+)')
valid = 0
total = 0
for line in lines:
    m = prog.match(line)

    #mincount = int(m.group(1))
    #maxcount = int(m.group(2))
    indexone = int(m.group(1)) - 1
    indextwo = int(m.group(2)) - 1
    letter = m.group(3)
    pwd = m.group(4)
    if (pwd[indexone] == letter or pwd[indextwo] == letter) and not (pwd[indexone] == letter and pwd[indextwo] == letter):
        valid = valid + 1
    else:
        print(line)
    #filterpwd = pwd.replace(letter, '')
    #lettercount = len(pwd) - len(filterpwd)
    #if lettercount >= mincount and lettercount <= maxcount:
    #    valid = valid + 1
    #total = total + 1

print(valid)