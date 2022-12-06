with open("input.txt") as file:
    inp = file.read().strip()

cases = inp.split("\n\n")
program = cases[-1]
cases = [(eval(c[0][7:]), eval(c[2][7:]), list(map(int, c[1].split(" "))))\
         for c in [case.split("\n") for case in cases][:776]]

def addr(reg,a,b,c):
    reg[c] = reg[a] + reg[b]

def addi(reg,a,b,c):
    reg[c] = reg[a] + b

def mulr(reg,a,b,c):
    reg[c] = reg[a] * reg[b]

def muli(reg,a,b,c):
    reg[c] = reg[a] * b

def banr(reg,a,b,c):
    reg[c] = reg[a] & reg[b]

def bani(reg,a,b,c):
    reg[c] = reg[a] & b

def borr(reg,a,b,c):
    reg[c] = reg[a] | reg[b]

def bori(reg,a,b,c):
    reg[c] = reg[a] | b

def setr(reg,a,b,c):
    reg[c] = reg[a]

def seti(reg,a,b,c):
    reg[c] = a

def gtir(reg,a,b,c):
    if a > reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0

def gtri(reg,a,b,c):
    if reg[a] > b:
        reg[c] = 1
    else:
        reg[c] = 0

def gtrr(reg,a,b,c):
    if reg[a] > reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0

def eqir(reg,a,b,c):
    if a == reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0

def eqri(reg,a,b,c):
    if reg[a] == b:
        reg[c] = 1
    else:
        reg[c] = 0

def eqrr(reg,a,b,c):
    if reg[a] == reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0

ops = [addr, addi, mulr, muli, banr, bani,
       borr, bori, setr, seti, gtir, gtri,
       gtrr, eqir, eqri, eqrr]

mapping = {}
rmapping = {}

num_over_3 = 0
for case in cases:
    num_ops = 0
    the_ops = []
    for op in ops:
        cp = case[0][:]
        op(cp, *case[2][1:])
        if cp == case[1]:
            num_ops += 1
            the_ops.append(op)
    if num_ops >= 3:
        num_over_3 += 1
    the_ops = [p for p in the_ops if p not in rmapping]
    if len(the_ops) == 1:
        mapping[case[2][0]] = the_ops[0]
        rmapping[the_ops[0]] = case[2][0]
print("Part 1:",num_over_3)

regs = [0,0,0,0]
for s in program.strip().split("\n"):
    ins = [int(x) for x in s.split(" ")]
    mapping[ins[0]](regs, ins[1], ins[2], ins[3])

print("Part 2:",regs[0])
