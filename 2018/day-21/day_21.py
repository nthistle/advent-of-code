import time

with open("input.txt") as file:
    inp = file.read().strip()

prog = inp.split("\n")
prog = [c.split(" ") for c in prog]
prog = [[c[0],*map(int,c[1:])] for c in prog]

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

op_dict = {op.__name__:op for op in ops}

st = time.time()

reg = [1,0,0,0,0,0]
ip = 0
ip_reg = prog[0][1]
prog = prog[1:]
ctr = 0
flag = False
check_seq = []
cc = 0
while ip in range(len(prog)):
    reg[ip_reg] = ip
    if ip == 28:
        print("Part 1:",reg[2])
        break
    op_dict[prog[ip][0]](reg, *prog[ip][1:])
    ip = reg[ip_reg]
    ip += 1
    ctr += 1

seen_checks = set()
last_check = 0
r2, r3, r5 = 2208870, 0, 65536
while True:
    if r5 < 256:
        if r2 in seen_checks:
            print("Part 2:",last_check)
            break
        seen_checks.add(r2)
        last_check = r2
        r5 = r2 | 65536
        r2 = 2238642
    else:
        r5 //= 256
    r3 = r5 & 255
    r2 += r3
    r2 &= 16777215
    r2 *= 65899
    r2 &= 16777215
