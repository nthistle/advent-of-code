import string
from collections import defaultdict
from aoc_tools import *
import functools
import sys
#sys.setrecursionlimit(10000000)
#       RIGHT0   DOWN1  LEFT2    UP3
dirs = ((0,1),(1,0),(0,-1),(-1,0))
dirs3 = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))

with open(r"input.txt") as f:
    s = f.read()[:-1]#.strip()
print("\n".join(x[:60] for x in s.split("\n")[:6]))

grid = defaultdict(lambda : False)
g = [list(x) for x in s.split("\n")]
n = len(g)
m = len(g[0])
for i in range(n):
    for j in range(m):
        if g[i][j] == "#":
            grid[i,j] = True

# N: -1,0
# S: +1,0
# W: 0,-1
# E: 0,+1
dirs = [
    [(-1,+0),(-1,-1),(-1,+1)],
    [(+1,+0),(+1,-1),(+1,+1)],
    [(+0,-1),(-1,-1),(+1,-1)],
    [(+0,+1),(-1,+1),(+1,+1)]
]

alldirs = sum(dirs,start=[])

def nxtstate(curgrid, doff):
    ourdirs = dirs[doff:] + dirs[:doff]
    newgrid = defaultdict(list)
    stationary = set()
    for (x,y),v in list(curgrid.items()):
        if not v: continue
        bad = True
        if all(not curgrid[x+dx,y+dy] for dx,dy in alldirs):
            stationary.add((x,y))
            continue
        for dset in ourdirs:
            if all(not curgrid[x+dx,y+dy] for dx,dy in dset):
                dx,dy = dset[0]
                newgrid[x+dx,y+dy].append((x,y))
                bad = False
                break
        if bad:
            stationary.add((x,y))
    newg = defaultdict(lambda : False)
    someone_moved = False
    for x,y in stationary:
        newg[x,y] = True
    for (nx,ny),people in newgrid.items():
        if len(people) == 1:
            newg[nx,ny] = True
            someone_moved = True
        else:
            for x,y in people:
                newg[x,y] = True
    return newg, (doff + 1) % 4, someone_moved
    # rotate dirs

def pg(grid):
    minx = min(x for (x,y),v in grid.items() if v)
    maxx = max(x for (x,y),v in grid.items() if v)
    miny = min(y for (x,y),v in grid.items() if v)
    maxy = max(y for (x,y),v in grid.items() if v)
    for x in range(minx,maxx+1):
        print("".join("#" if grid[x,y] else "." for y in range(miny,maxy+1)))

doff = 0

for _ in range(10):
    grid, doff, chk = nxtstate(grid, doff)

minx = min(x for (x,y),v in grid.items() if v)
maxx = max(x for (x,y),v in grid.items() if v)
miny = min(y for (x,y),v in grid.items() if v)
maxy = max(y for (x,y),v in grid.items() if v)

print(sum(1 for x in range(minx, maxx+1) for y in range(miny, maxy+1)
          if not grid[x,y]))

rnd = 10
while True:
    grid, doff, chk = nxtstate(grid, doff)
    rnd += 1
    if not chk:
        break

print(rnd)


















































