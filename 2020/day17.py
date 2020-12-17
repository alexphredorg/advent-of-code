from collections import Counter
from itertools import chain
import functools
import operator

class four_d_map:
    # w list of 3d maps
    # z list of 2d maps
    # y list of 1d rows
    # x strings
    map_data = []
    grow_w = True

    def __init__(self, two_d_map_data, grow_w):
        self.grow_w = grow_w
        self.map_data = [ [ two_d_map_data ] ]
    
    def get_value(self, x, y, z, w): return self.map_data[w][z][y][x]
    def wlen(self): return len(self.map_data)
    def zlen(self): return len(self.map_data[0])
    def ylen(self): return len(self.map_data[0][0])
    def xlen(self): return len(self.map_data[0][0][0])

    def create_empty_z(self):
        new_z = []
        for y in range(0, self.ylen()): new_z.append('.' * (self.xlen()))
        return new_z
    
    def create_empty_w(self):
        new_w = []
        for z in range(0, self.zlen()): new_w.append(self.create_empty_z())
        return new_w

    def pad_2d_map(self, map_data):
        new_map_data = [ '.' * (len(map_data[0]) + 2) ]
        for row in map_data:
            new_map_data.append( '.' + row + '.' )
        new_map_data.append(new_map_data[0])
        return new_map_data

    def pad_map(self):
        zlen = self.zlen()
        for w in range(0, self.wlen()): 
            for z in range(0, zlen): 
                self.map_data[w][z] = self.pad_2d_map(self.map_data[w][z])
            self.map_data[w].insert(0, self.create_empty_z())
            self.map_data[w].append(self.create_empty_z())
        if self.grow_w:
            self.map_data.insert(0, self.create_empty_w())
            self.map_data.append(self.create_empty_w())

    def print_layer(self, w, z, prefix=""):
        for y in range(0, len(self.map_data[w][z])):
            print(prefix + self.map_data[w][z][y])

    def print_map(self):
        for w in range(0, self.wlen()):
            for z in range(0, self.zlen()):
                print("w,z = %d,%d:" % (w, z))
                self.print_layer(w, z, prefix="  ")

    def count_neighbors(self, x, y, z, w):
        neighbors = []
        for dw in range(-1, 2):
            for dz in range(-1, 2):
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        #print(x + dx, y + dy, z + dz)
                        if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                            v = self.get_value(x, y, z, w)
                        elif 0 <= x + dx < self.xlen() and 0 <= y + dy < self.ylen() and 0 <= z + dz < self.zlen() and 0 <= w + dw < self.wlen():
                            #print(x + dx, y + dy, z + dz, w + dw, self.xlen(), self.ylen(), self.zlen(), self.wlen())
                            neighbors.append(self.get_value(x + dx, y + dy, z + dz, w + dw))
        return (Counter(neighbors), v)

    def step(self):
        new_map = []
        self.pad_map()
        for w in range(0, self.wlen()):
            new_z = []
            for z in range(0, self.zlen()):
                new_y = []
                for y in range(0, self.ylen()):
                    new_row = []
                    for x in range(0, self.xlen()):
                        (c, v) = self.count_neighbors(x, y, z, w)
                        active = c['#']
                        #print(v, active, x, y, z)
                        if v == '.' and active == 3:
                            new_row.append('#')
                        elif v == '#' and 2 <= active <= 3:
                            new_row.append('#')
                        else:
                            new_row.append('.')
                    assert(len(new_row) == self.xlen())
                    new_y.append(''.join(new_row))
                new_z.append(new_y)
            new_map.append(new_z)
        self.map_data = new_map

    def count(self):
        return Counter(functools.reduce(operator.concat, [y for w in self.map_data for z in w for y in z]))

def read_input(filename):
    with open(filename, 'r') as f:
        data = [x.rstrip() for x in f.readlines()]
    return data

def run(grow_w):
    map = four_d_map(read_input("day17.txt"), grow_w)
    for i in range(0, 6):
        map.step()
        print("cycle ", i, map.count())

print("part1:")
run(grow_w=False)
print("\npart2:")
run(grow_w=True)