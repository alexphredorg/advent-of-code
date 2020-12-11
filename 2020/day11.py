# pads our data range with unusable spaces around the edge
def pad_input(data):
    newdata = [ '.' * (len(data[0]) + 2) ]
    for row in data:
        newdata.append( '.' + row + '.' )
    newdata.append(newdata[0])
    return newdata

def read_input(filename):
    with open(filename, 'r') as f:
        data = [x.rstrip() for x in f.readlines()]
    return pad_input(data)

def count_occupied_adjacent(data, x, y):
    c = sum(data[y + iy].count('#', x-1, x+2) for iy in range(-1, 2))
    if data[y][x] == '#': c -= 1
    return c

def step(data, countfn, full_threshold):
    newdata = [ data[0] ]
    xlen = len(data[0])
    for y in range(1, len(data) - 1):    
        row = '.'
        for x in range(1, xlen):
            if data[y][x] == 'L' and countfn(data, x, y) == 0:
                row += '#'
            elif data[y][x] == '#' and countfn(data, x, y) >= full_threshold:
                row += 'L'
            else:
                row += data[y][x]
        row += '.'
        newdata.append(row)
    newdata.append(newdata[0])
    return newdata

def part1(data):
    newdata = None
    while(newdata != data):
        if newdata != None: data = newdata
        newdata = step(data, count_occupied_adjacent, 4)
    return sum(row.count('#') for row in newdata)

def next_seat_in_dir(data, x, y, dx, dy):
    if dx == 0 and dy == 0: return None
    xlen = len(data[0])
    ylen = len(data)
    while True:
        x += dx
        y += dy
        if x < 0 or y < 0 or x >= xlen or y >= ylen: return None
        if data[y][x] != '.': return (x, y)

def build_seat_view_map(data, x, y):
    return [ next_seat_in_dir(data, x, y, dx, dy) for dy in range(-1, 2) for dx in range(-1, 2)]
    
seat_view_map = None
def count_occupied_inview(data, x, y):
    global seat_view_map
    view_map = seat_view_map[y][x]
    viewable = [ data[view_map[i][1]][view_map[i][0]] for i in range(0, 9) if view_map[i] != None ]
    c = sum(v == '#' for v in viewable)
    return c

def part2(data):
    global seat_view_map
    seat_view_map = []
    for y in range(0, len(data)):
        row_map = []
        for x in range(0, len(data[0])):
            row_map.append(build_seat_view_map(data, x, y))
        seat_view_map.append(row_map)

    newdata = None
    while(newdata != data):
        if newdata != None: data = newdata
        newdata = step(data, count_occupied_inview, 5)
    return sum(row.count('#') for row in newdata)

data = read_input('day11-test.txt')
print("part1-test: %d" % part1(data))        
print("part2-test: %d" % part2(data))
data = read_input('day11.txt')
print("part1-real: %d" % part1(data))        
print("part2-real: %d" % part2(data))        

