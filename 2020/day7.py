import re

# i hate these solutions, but they work.  they are expensive and brute force and a lot of code...
# i think there is an elegant trick that I missed.
def parse_input_part1(filename):
    bag_rule = re.compile('^(\w+\s\w+)\sbags\scontain\s(.*)$')
    bag_subrule = re.compile("^(\d+)\s(\w+\s\w+)\sbag.*$")

    with open(filename, 'r') as f:
        rules = f.readlines()

    rule_dict = {}
    for r in rules:
        m = bag_rule.match(r)
        subrules = m.group(2).strip('.').split(', ')
        for subrule in subrules:
            if m.group(1) not in rule_dict:
                rule_dict[m.group(1)] = []
            if subrule != "no other bags":
                bag_match = bag_subrule.match(subrule)
                if bag_match.group(2) not in rule_dict:
                    rule_dict[bag_match.group(2)] = []
                rule_dict[bag_match.group(2)].append(m.group(1))
    return rule_dict

def part1(rules, inner_color = "shiny gold"):
    input_colors = [ inner_color ]
    output_colors = set()
    while len(input_colors) > 0:
        color = input_colors.pop()
        if color not in output_colors:
            output_colors.add(color)
            for c in rules[color]:
                input_colors.append(c)
    output_colors.remove(inner_color)
    return output_colors

def parse_input_part2(filename):
    bag_rule = re.compile('^(\w+\s\w+)\sbags\scontain\s(.*)$')
    bag_subrule = re.compile("^(\d+)\s(\w+\s\w+)\sbag.*$")

    with open(filename, 'r') as f:
        rules = f.readlines()

    rule_dict = {}
    for r in rules:
        m = bag_rule.match(r)
        subrules = m.group(2).strip('.').split(', ')
        subrule_list = []
        for subrule in subrules:
            if subrule != "no other bags":
                bag_match = bag_subrule.match(subrule)
                subrule_list.append((int(bag_match.group(1)), bag_match.group(2)))
        rule_dict[m.group(1)] = subrule_list
    return rule_dict

def part2(rules, containing_color = "shiny gold"):
    input_colors = [ containing_color ]
    counter = 0
    while len(input_colors) > 0:
        color = input_colors.pop()
        for c in rules[color]:
            for n in range(0, c[0]):
                input_colors.append(c[1])
            counter += c[0]
    return counter


rules = parse_input_part1("day7.txt")
print(len(part1(rules)))

rules = parse_input_part2("day7.txt")
print(rules)
print(part2(rules))