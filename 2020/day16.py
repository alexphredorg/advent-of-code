from _helpers import grouped_reader
import re
from collections import Counter
from functools import reduce

def read_input(filename):
    sections = grouped_reader(filename)

    ruleParser = re.compile('^([\w\s]+):\s(\d+)-(\d+) or (\d+)-(\d+)$')
    rules = []
    for rule in sections[0]:
        m = ruleParser.match(rule)
        rules.append(((int(m.group(2)), int(m.group(3))), m.group(1)))
        rules.append(((int(m.group(4)), int(m.group(5))), m.group(1)))

    assert(sections[1][0] == "your ticket:")
    your_ticket = [int(x) for x in sections[1][1].split(',')]

    assert(sections[2][0] == "nearby tickets:")
    nearby_tickets = []
    for ticket in sections[2][1:]:
        nearby_tickets.append([int(x) for x in ticket.split(',')])
    
    return (rules, your_ticket, nearby_tickets)

def parts1and2(rules, nearby_tickets, your_ticket):
    # filter out invalid tickets
    valid_tickets = []
    invalid_list = []
    for ticket in nearby_tickets:
        invalid = 0
        for value in ticket:
            valid = 0
            for rule in rules:
                if rule[0][0] <= value <= rule[0][1]: valid += 1 
            if valid == 0:
                invalid_list.append(value) 
                invalid += 1
        if invalid == 0: valid_tickets.append(ticket)

    # d is built to contain a list of rules that were hit for
    # each value_index. 
    # key: value_index
    # value: list of possible rule names
    d = {}
    for ticket in valid_tickets:
        for value_index in range(0, len(ticket)):
            value = ticket[value_index]
            for rule in rules:
                if rule[0][0] <= value <= rule[0][1]:
                    if value_index not in d: d[value_index] = []
                    d[value_index].append(rule[1])          

    # now build hits_list to contain only the rule names that matched
    # every ticket
    # key: value_index
    # value: (count, possible rule names)
    hits_list = {}
    for (index, name_list) in d.items():
        c = Counter(name_list)
        possible = [name for (name, count) in c.items() if count == len(valid_tickets) ]
        hits_list[index] = (len(possible), possible)
    
    # rebuild d match value_index to rule name
    # by sorting hits_list to go from least number of hits to most number
    # and keeping track of which value names we already found in the used_keys set
    d = {}
    used_keys = set()
    for (index, (count, possible)) in sorted(hits_list.items(), key = lambda x: x[1]):
        for p in possible:
            if not p in used_keys:
                used_keys.add(p)
                d[index] = p

    # finally match against our ticket and look up all of the departure values
    departure_list = []
    for value_index in range(0, len(your_ticket)):
        if str(d[value_index]).startswith("departure"): departure_list.append(your_ticket[value_index])
    return(sum(invalid_list), reduce(lambda x, y: x * y, departure_list))    

(rules, your_ticket, nearby_tickets) = read_input("day16.txt")
print(parts1and2(rules, nearby_tickets, your_ticket))