import string
from aoc_tools import *
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

with open("input.txt") as f:
    s = f.read().strip()


g = [list(x) for x in s.split("\n")]
n = len(g)
m = len(g[0])

sx,sy = [(i,j) for i in range(n) for j in range(m) if g[i][j] == "S"][0]
tx,ty = [(i,j) for i in range(n) for j in range(m) if g[i][j] == "E"][0]

g[sx][sy] = "a"
g[tx][ty] = "z"

g = [[ord(c) - ord("a") for c in r] for r in g]

from collections import deque

dst = defaultdict(lambda : 1000000)

part = 2
# part 1:
if part == 1:
    q = deque([(sx,sy)])
# part 2:
else:
    q = deque([(i,j) for i in range(n) for j in range(m) if g[i][j] == 0])

for x,y in q:
    dst[x,y] = 0
    
ans = 100000
while len(q) > 0:
    cx,cy = q.popleft()
    if (cx,cy) == (tx,ty):
        ans = dst[tx,ty]
        print(ans)
        break
    for dx,dy in dirs:
        nx,ny = cx+dx,cy+dy
        if nx in range(n) and ny in range(m):
            if g[cx][cy] >= g[nx][ny] - 1:
                ndst = dst[cx,cy] + 1
                if ndst < dst[nx,ny]:
                    q.append((nx,ny))
                    dst[nx,ny] = ndst






















































