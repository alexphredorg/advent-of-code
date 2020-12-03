def readinput(filename):
    with open(filename, 'r') as f:
        rows = f.readlines()
        rows = list(map(lambda x: x.rstrip(), rows))
    return rows

def count_trees(rows, col_increment, row_increment):
    col = 0
    trees = 0
    rowlength = len(rows[0])
    for row_index in range(0, len(rows), row_increment):
        if rows[row_index][col] == '#': trees = trees + 1
        col = (col + col_increment) % rowlength
    return trees

rows = readinput('day3-test.txt')
print("test data results: count = %d" % count_trees(rows, 3, 1))

rows = readinput('day3.txt')
increments = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
mult = 1
for i in range(0, len(increments), 1):
    trees = count_trees(rows, increments[i][0], increments[i][1])
    mult = mult * trees
    print("increment = %s  count = %d" % (str(increments[i]), trees))

print(mult)