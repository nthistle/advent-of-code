import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from aoc_lib import *

s = get_input()

n,m,g = grid(s)

nb = [(i,j) for i in range(-1,2) for j in range(-1,2) if (i,j) != (0,0)]

def apply(g):
    ng = [[-1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            e_n = 0
            o_n = 0
            for di,dj in nb:
                ni, nj = i + di, j + dj
                if ni in range(n) and nj in range(m):
                    if g[ni][nj] == "L":
                        e_n += 1
                    elif g[ni][nj] == "#":
                        o_n += 1
            if g[i][j] == "L":
                if o_n == 0:
                    ng[i][j] = "#"
                else:
                    ng[i][j] = "L"
            elif g[i][j] == "#":
                if o_n >= 4:
                    ng[i][j] = "L"
                else:
                    ng[i][j] = "#"
            else:
                ng[i][j] = g[i][j]
    return ng

ts = lambda gg : "\n".join("".join(v for v in r) for r in gg)

ct = 0
cg = g
while ts(cg) != ts((ng := apply(cg))):
    cg = ng
    ct += 1

print(ct)
print(sum(1 for i in range(n) for j in range(m) if cg[i][j] == "#"))


adj = {}
for i in range(n):
    for j in range(m):
        adj[i,j] = []
        for di,dj in nb:
            ni, nj = i + di, j + dj
            while ni in range(n) and nj in range(m) and g[ni][nj] == ".":
                ni += di
                nj += dj
            if ni in range(n) and nj in range(m):
                adj[i,j].append((ni,nj))


def apply(g):
    ng = [[-1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            e_n = 0
            o_n = 0
            for ni,nj in adj[i,j]:
                if ni in range(n) and nj in range(m):
                    if g[ni][nj] == "L":
                        e_n += 1
                    elif g[ni][nj] == "#":
                        o_n += 1
            if g[i][j] == "L":
                if o_n == 0:
                    ng[i][j] = "#"
                else:
                    ng[i][j] = "L"
            elif g[i][j] == "#":
                if o_n >= 5:
                    ng[i][j] = "L"
                else:
                    ng[i][j] = "#"
            else:
                ng[i][j] = g[i][j]
    return ng

cg = g
while ts(cg) != ts((ng := apply(cg))):
    cg = ng

print(sum(1 for i in range(n) for j in range(m) if cg[i][j] == "#"))
