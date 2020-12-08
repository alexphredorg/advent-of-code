import string

def readinput(filename):
    binary_trans = str.maketrans("fbrlFBRL", "01100110")
    with open(filename, 'r') as f:
        seat_labels = f.readlines()
    seat_ids = list(map(lambda x: int(x.translate(binary_trans), 2), seat_labels))
    return seat_ids

def find_missing_seat(seat_set, max_value):
    seats = [x for x in range(0, max_value) if x not in seat_set and x+1 in seat_set and x-1 in seat_set]
    return seats[0]

seat_ids = readinput("day5.txt")
max_seat_id = max(seat_ids)
print("Max seat ID is %d " % max_seat_id)
print("Your seat is %d" % find_missing_seat(frozenset(seat_ids), max_seat_id))