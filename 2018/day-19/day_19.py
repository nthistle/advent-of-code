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

reg = [0,0,0,0,0,0]
ip = 0
ip_reg = prog[0][1]
prog = prog[1:]
while ip in range(len(prog)):
    reg[ip_reg] = ip
    op_dict[prog[ip][0]](reg, *prog[ip][1:])
    ip = reg[ip_reg]
    ip += 1

print("Part 1:",reg[0])

reg = [1,0,0,0,0,0]
ip = 0
for k in range(30): # enough to generate the input
    reg[ip_reg] = ip
    op_dict[prog[ip][0]](reg, *prog[ip][1:])
    ip = reg[ip_reg]
    ip += 1

acc = 0
n = max(reg) # janky, but works
# in practice I identified this by hand

for k in range(1,n+1):
    if n % k == 0:
        acc += k
print("Part 2:",acc)
