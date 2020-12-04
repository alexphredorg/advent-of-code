import re

def readinput(filename):
    with open(filename, 'r') as f:
        rows = f.readlines()
        rows = list(map(lambda x: x.rstrip(), rows))
    return rows

part2 = True

def check_height(hgt):
    l = len(hgt)
    suffix = hgt[l-2:l]
    prefix = int(hgt[0:l-2])
    if suffix == 'cm' and (prefix < 150 or prefix > 193):
        return False
    elif suffix == 'in' and (prefix < 59 or prefix > 76):
        return False
    elif suffix != 'in' and suffix != 'cm':
        return False
    return True

def check_range(val, min, max):
    if val < min or val > max:
        return False
    return True

ecl_re = re.compile('^(amb|blu|brn|gry|grn|hzl|oth)$')
pid_re = re.compile('^\d{9}$')
xyr_re = re.compile('^\d+$')
hcl_re = re.compile('^#[0-9a-fA-F]{6}$')
hgt_re = re.compile('(\d+)(in|cm)')

def evaluate(elements):
    field_count = 0
    required_fields = [
        ('ecl', ecl_re), 
        ('pid', pid_re),
        ('eyr', xyr_re, lambda x: check_range(int(x), 2020, 2030)),
        ('hcl', hcl_re),
        ('byr', xyr_re, lambda x: check_range(int(x), 1920, 2002)), 
        ('iyr', xyr_re, lambda x: check_range(int(x), 2010, 2020)),
        ('hgt', hgt_re, lambda x: check_height(x))
        ]
    for field_tuple in required_fields:
        field = field_tuple[0]
        if field in elements: 
            field_count = field_count + 1
            if part2:
                value = elements[field]
                m = field_tuple[1].match(value)
                if m == None:
                    return False
                if len(field_tuple) > 2:
                    if not field_tuple[2](value):
                        return False

    if field_count < 7:
        return False

    return True

def validate_passports(rows):
    elements = {}
    valid = 0
    prog = re.compile('(\w+):(.*)')
    for row in rows:
        if row == '':
            if evaluate(elements):
                valid = valid + 1
            elements = {}
        else:
            parts = row.split(' ')
            for part in parts:
                m = prog.match(part)
                elements[m.group(1)] = m.group(2)
    return valid

rows = readinput('day4.txt')
#116 for part2
print(validate_passports(rows))