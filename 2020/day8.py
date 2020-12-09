from _helpers import timer

def read_program(filename):
    prog = []
    with open(filename, 'r') as f:
        for c, line in enumerate(f):
            parts = line.rstrip().split(' ')
            prog.append((parts[0], int(parts[1])))
    return prog

def run_program(prog, fix_ip = None, fix_opcode = None):
    ip = 0
    acc = 0
    visited_ips = set()
    while ip < len(prog):
        (opcode, operand) = prog[ip]
        if fix_ip == ip: opcode = fix_opcode 
        visited_ips.add(ip)
        #print("%d:%s %d" % (ip, opcode, operand))
        if opcode == "nop":
            ip += 1
        elif opcode == "acc":
            acc += operand
            ip += 1
        elif opcode == "jmp":
            if ip + operand in visited_ips: return (False, ip, acc, visited_ips)
            ip += operand
    return (True, ip, acc, visited_ips)

@timer
def run(prog):
    (success, ip, acc, visited_ips) = run_program(prog)
    if not success: print("Looped at ip %d, acc = %d" % (ip, acc))
    idx = 0
    fixes = 0
    opcode_history = list(visited_ips)
    while not success:
        fix_ip = opcode_history[idx]
        if prog[fix_ip][0] == "nop":
            (success, ip, acc, ignored) = run_program(prog, fix_ip, "jmp")
            fixes += 1
        elif prog[fix_ip][0] == "jmp":
            (success, ip, acc, ignored) = run_program(prog, fix_ip, "nop")
            fixes += 1
        idx += 1
    #print("Took %d attempted fixes (out of %d possible)" % (fixes, len(opcode_history)))
    return acc

prog = read_program("day8-test.txt")
acc = run(prog)
print("Successful run, acc = %d" % acc)
