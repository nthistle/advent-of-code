import string
from aoc_tools import *
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

with open("input.txt") as f:
    s = f.read().strip()
print("\n".join(x[:60] for x in s.split("\n")[:10]))


s = s.split("\n\n")

m = []
N = 1
for x in s:
    lns = x.split("\n")
    mn = nums(lns[0])[0]
    st = nums(lns[1])
    op = lns[2][len("  Operation: "):]
    tst = nums(lns[3])[0]
    iftrue = nums(lns[4])[0]
    iffalse = nums(lns[5])[0]
    N *= tst
    m.append((mn, st, op, tst, iftrue, iffalse))

mitems = [[x for x in st] for _,st,_,_,_,_ in m]
counts = [0 for _ in m]

# reproduced part 1 code
for _ in range(20):
    for i in range(len(m)):
        mnk = m[i]
        for item in mitems[i]:
            counts[i] += 1
            old = item
            new = eval(mnk[2][5:])
            if new % mnk[3] == 0:
                mitems[mnk[4]].append(new)
            else:
                mitems[mnk[5]].append(new)
        mitems[i].clear()
        
counts.sort()
print(counts[-1] * counts[-2])

mitems = [[x for x in st] for _,st,_,_,_,_ in m]
counts = [0 for _ in m]

for _ in range(10000):
    for i in range(len(m)):
        mnk = m[i]
        for item in mitems[i]:
            counts[i] += 1
            old = item
            new = eval(mnk[2][5:])
            new %= N
            if new % mnk[3] == 0:
                mitems[mnk[4]].append(new)
            else:
                mitems[mnk[5]].append(new)
        mitems[i].clear()


counts.sort()
print(counts[-1] * counts[-2])


















