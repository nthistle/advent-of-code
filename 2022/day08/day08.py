import string
from aoc_tools import *

with open("input.txt") as f:
    s = f.read().strip()

g = [[int(y) for y in x] for x in s.split("\n")]
n = len(g)
m = len(g[0])

vis = set()
for i in range(n):
    for j in range(m):
        isviz = False
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni = i + dx
            nj = j + dy
            v = True
            while ni in range(n) and nj in range(m):
                if g[ni][nj] >= g[i][j]:
                    v = False
                    break
                ni += dx
                nj += dy
            if v:
                isviz = True
                break
        if isviz:
            vis.add((i, j))

print(len(vis))

r = 0

for i in range(n):
    for j in range(m):
        vd = []
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni = i + dx
            nj = j + dy
            c = 0
            v = True
            while ni in range(n) and nj in range(m):
                if g[ni][nj] >= g[i][j]:
                    v = False
                    break
                ni += dx
                nj += dy
                c += 1
            vd.append(c + (1 if ni in range(n) and nj in range(m) else 0))
        r = max(r, vd[0]*vd[1]*vd[2]*vd[3])

print(r)
