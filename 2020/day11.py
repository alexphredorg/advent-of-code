from _helpers import timer
import sys

def read_input(filename):
    with open(filename, 'r') as f:
        data = [x.rstrip() for x in f.readlines()]
    return pad_input(data)

# pads our data range with unusable spaces around the edge
# needed for count_occupied_adjacent to work
def pad_input(data):
    newdata = [ '.' * (len(data[0]) + 2) ]
    for row in data:
        newdata.append( '.' + row + '.' )
    newdata.append(newdata[0])
    return newdata

# run one step of the game, returning a data map the 
# same size as the input, but with updates to occupied
# seats
def step(data, countfn, full_threshold, seat_view_map = None):
    newdata = [ data[0] ]
    xlen = len(data[0])
    for y in range(1, len(data) - 1):    
        row = list(data[y])
        for x in range(1, xlen):
            if data[y][x] == 'L' and countfn(data, x, y, seat_view_map) == 0:
                row[x] = '#'
            elif data[y][x] == '#' and countfn(data, x, y, seat_view_map) >= full_threshold:
                row[x] = 'L'
        newdata.append(''.join(row))
    newdata.append(newdata[0])
    return newdata

# count occupied seats adjacent.  Has no bounds checking, so don't run this right
# on a border location
def count_occupied_adjacent(data, x, y, ignored):
    c = sum(data[y + iy].count('#', x-1, x+2) for iy in range(-1, 2))
    if data[y][x] == '#': c -= 1
    return c

# for a given seat in our input data at location x, y move in direction dx/dy for up to maxrange steps
# until we find the border or a seat.  Border returns None, seat returns the location of that seat
def next_seat_in_dir(data, x, y, dx, dy, maxrange):
    if dx == 0 and dy == 0: return None
    xlen = len(data[0])
    ylen = len(data)
    for i in range(0, maxrange):
        x += dx
        y += dy
        if x < 0 or y < 0 or x >= xlen or y >= ylen: return None
        if data[y][x] != '.': return (x, y)

# Build a seat map for each of the 9 directions (including self) for a seat at point x,y
def build_seat_view_map(data, x, y, maxrange):
    return [ next_seat_in_dir(data, x, y, dx, dy, maxrange) for dy in range(-1, 2) for dx in range(-1, 2)]
    
# use the seat_view_map to count occupied seats around a location
def count_occupied_inview(data, x, y, seat_view_map):
    view_map = seat_view_map[y][x]
    viewable = [ data[view_map[i][1]][view_map[i][0]] for i in range(0, 9) if view_map[i] != None ]
    c = sum(v == '#' for v in viewable)
    return c

@timer
def part1old(data):
    newdata = None
    while(newdata != data):
        if newdata != None: data = newdata
        newdata = step(data, count_occupied_adjacent, 4)
    return sum(row.count('#') for row in newdata)

@timer
def part2broken(data, maxrange = sys.maxsize, occupied_limit = 5):
    seat_view_map = []
    for y in range(0, len(data)):
        row_map = []
        for x in range(0, len(data[0])):
            row_map.append(build_seat_view_map(data, x, y, maxrange))
        seat_view_map.append(row_map)

    newdata = None
    while(newdata != data):
        if newdata != None: data = newdata
        newdata = step(data, count_occupied_inview, occupied_limit, seat_view_map)
    return sum(row.count('#') for row in newdata)

@timer
def part2(data, maxrange = sys.maxsize, occupied_limit = 5):
    seat_view_map = []
    for y in range(0, len(data)):
        row_map = []
        for x in range(0, len(data[0])):
            row_map.append(build_seat_view_map(data, x, y, maxrange))
        seat_view_map.append(row_map)

    newdata = None
    while(newdata != data):
        if newdata != None: data = newdata
        newdata = step(data, count_occupied_inview, occupied_limit, seat_view_map)
    return sum(row.count('#') for row in newdata)

data = read_input('day11-test.txt')
print("part1-test: %d" % part2(data, 1, 4))        
print("part1old-test: %d" % part1old(data))
print("part2-test: %d" % part2(data))
data = read_input('day11.txt')
print("part1-real: %d" % part2(data, 1, 4))     
print("part1old-real: %d" % part1old(data))
print("part2-real: %d" % part2(data))        

