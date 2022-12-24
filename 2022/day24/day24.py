import string
from collections import defaultdict
from aoc_tools import *
import functools
import sys
sys.setrecursionlimit(100000)
dirs = ((0,1),(1,0),(0,-1),(-1,0))
dirs3 = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))

with open(r"input.txt") as f:
    s = f.read()[:-1]#.strip()
print("\n".join(x[:60] for x in s.split("\n")[:6]))

g = [list(x) for x in s.split("\n")]
N = len(g) - 2
M = len(g[0]) - 2

m = {"<":(0,-1),
     ">":(0,1),
     "v":(1,0),
     "^":(-1,0)}

blizz_locs = [
    [i, j, m[g[i][j]]]
    for i in range(1,len(g)-1)
    for j in range(1,len(g[0])-1)
    if g[i][j] != "."
]

def nxt():
    for x in blizz_locs:
        i, j, (di, dj) = x
        ni = i + di
        nj = j + dj
        ni = ((ni - 1) % N) + 1
        nj = ((nj - 1) % M) + 1
        x[0] = ni
        x[1] = nj


occupied = set()
st = (0,1)
gl = (26,120)
dist = defaultdict(lambda : float("inf"))
q = deque()
q.append((st, False, False, 0))
dist[st] = 0
dups = set()
maxdist = -1
while True:
    (cx,cy),r1,r2,cd = q.popleft()
    if (cx,cy)==gl and r1 and r2:
        print(cx,cy,cd)
        break
    if cd > maxdist:
        #print(cd,maxdist)
        maxdist = cd
        nxt()
        occupied = set()
        for i,j,_ in blizz_locs:
            occupied.add((i,j))
    for dx,dy in dirs + ((0,0),):
        nx,ny = cx + dx, cy + dy
        if (nx,ny) not in occupied and nx in range(1,1+N) and ny in range(1,1+M) or \
           (nx,ny) == st or (nx,ny) == gl:
            if (nx,ny,r1,r2,cd) not in dups:
                dups.add((nx,ny,r1,r2,cd))
                if (nx,ny) == gl:
                    q.append(((nx,ny), True, r2, cd + 1))
                elif (nx,ny) == st and r1:
                    q.append(((nx,ny), r1, True, cd + 1))
                else:
                    q.append(((nx,ny), r1, r2, cd + 1))
            
















































