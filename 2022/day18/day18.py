import string
from collections import defaultdict
from aoc_tools import *
import functools
import sys
sys.setrecursionlimit(10000000)
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

with open(r"input.txt") as f:
    s = f.read().strip()
#print("\n".join(x[:60] for x in s.split("\n")[:6]))

ok = set()
g = defaultdict(int)
for line in s.split("\n"):
    t = tuple(nums(line))
    g[t] = 1
    ok.add(t)

adj = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))

r = 0
for nx,ny,nz in ok:
    bad = False
    for dx,dy,dz in adj:
        tx = nx + dx
        ty = ny + dy
        tz = nz + dz
        if g[tx,ty,tz] == 0:
            r += 1
print(r)


# -5..25 ish for all coords

def dfs(x,y,z,c):
    stack = [(x,y,z)]
    while len(stack) > 0:
        x,y,z = stack.pop(-1)
        if x not in range(-5,25):
            continue
        if y not in range(-5,25):
            continue
        if z not in range(-5,25):
            continue
        if g[x,y,z] != 0:
            continue
        g[x,y,z] = c
        for dx,dy,dz in adj:
            stack.append((x+dx,y+dy,z+dz))


NC = 2
for i in range(-1,23):
    for j in range(-1,23):
        for k in range(-1,23):
            dfs(i,j,k,NC)
            if g[i,j,k] == NC:
                NC += 1

r = 0
for nx,ny,nz in ok:
    bad = False
    for dx,dy,dz in adj:
        tx = nx + dx
        ty = ny + dy
        tz = nz + dz
        if g[tx,ty,tz] == g[-4,-4,-4]:
            r += 1
print(r)


















































