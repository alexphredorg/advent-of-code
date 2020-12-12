def read_input(filename):
    with open(filename, 'r') as f:
        data = [x.rstrip() for x in f.readlines()]
    return data


def part1(commands):
    d = 90
    ns = 0
    ew = 0
    degtoverb = { 0: 'N', 90: 'E', 180: 'S', 270: 'W' }
    isa = {
        'L': lambda ns, ew, d, arg: (ns, ew, (d - arg) % 360),
        'R': lambda ns, ew, d, arg: (ns, ew, (d + arg) % 360),
        'F': lambda ns, ew, d, arg: isa[degtoverb[d % 360]](ns, ew, d, arg),
        'N': lambda ns, ew, d, arg: (ns - arg, ew, d),
        'S': lambda ns, ew, d, arg: (ns + arg, ew, d),
        'E': lambda ns, ew, d, arg: (ns, ew - arg, d),
        'W': lambda ns, ew, d, arg: (ns, ew + arg, d)}

    for command in commands:
        verb = command[0]
        arg = int(command[1:])
        (ns, ew, d) = isa[verb](ns, ew, d, arg)
    return abs(ns) + abs(ew)

print(part1(read_input("day12.txt")))

def rotate(r, arg):
    if arg >= 90:
        wp_ew = r["wp_ns"]
        wp_ns = -r["wp_ew"]
        r["wp_ew"] = wp_ew
        r["wp_ns"] = wp_ns
        arg -= 90
        if arg != 0: rotate(r, arg)
    elif arg <= -90:
        wp_ns = r["wp_ew"]
        wp_ew = -r["wp_ns"]
        r["wp_ew"] = wp_ew
        r["wp_ns"] = wp_ns
        arg += 90
        if arg != 0: rotate(r, arg)

def forward(r, arg):
    r["ship_ns"] = r["ship_ns"] + (r["wp_ns"] * arg)
    r["ship_ew"] = r["ship_ew"] + (r["wp_ew"] * arg)

def update(r, key, arg):
    r[key] = r[key] + arg

def part2(commands):
    d = 90
    ns = 0
    ew = 0

    # registers
    r = {
        "wp_ns": -1,
        "wp_ew": -10,
        "ship_ns": 0,
        "ship_ew": 0,
    }

    isa = {
        'L': lambda r, arg: rotate(r, -arg),
        'R': lambda r, arg: rotate(r, arg),
        'F': lambda r, arg: forward(r, arg),
        'N': lambda r, arg: update(r, "wp_ns", -arg),
        'S': lambda r, arg: update(r, "wp_ns", arg),
        'E': lambda r, arg: update(r, "wp_ew", -arg),
        'W': lambda r, arg: update(r, "wp_ew", arg)
    }

    for command in commands:
        verb = command[0]
        arg = int(command[1:])
        isa[verb](r, arg)
        #print(verb, arg, r)
    return abs(r["ship_ns"]) + abs(r["ship_ew"])

print(part2(read_input("day12.txt")))

