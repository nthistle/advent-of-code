import string
from aoc_tools import *
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

with open("input.txt") as f:
    s = f.read().strip()
print("\n".join(x[:60] for x in s.split("\n")[:6]))

s = s.split("\n\n")
s2 = []
for x in s:
    a,b = x.split("\n")
    s2.append((eval(a),eval(b)))
s = s2

def cmp(a,b): # -1 if a < b, 0 if a = b
    if type(a) is int and type(b) is int:
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1
    elif type(a) is list and type(b) is int:
        b = [b]
    elif type(a) is int and type(b) is list:
        a = [a]

    n = len(a)
    m = len(b)
    for aa, bb in zip(a, b):
        r = cmp(aa, bb)
        if r != 0:
            return r
    if n < m:
        return -1
    elif n == m:
        return 0
    else:
        return 1

r = 0
for i,(a,b) in enumerate(s):
    if cmp(a,b) == -1:
        r += i + 1
print(r)

pkts = []
for a,b in s:
    pkts.append(a)
    pkts.append(b)

pkts.append([[2]])
pkts.append([[6]])

for i in range(len(pkts)):
    for j in range(len(pkts)-1):
        if cmp(pkts[j], pkts[j+1]) > 0:
            pkts[j], pkts[j+1] = pkts[j+1], pkts[j]

x, y = [i for i in range(len(pkts)) if pkts[i] == [[2]] or pkts[i] == [[6]]]
print((x + 1) * (y + 1))









































