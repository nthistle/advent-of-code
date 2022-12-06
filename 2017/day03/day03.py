inp = 325489

s = 1
while s*s < inp:
    s += 2
s -= 2

v = s*s + 1
loc = [(s//2)+1, -(s//2)]
if v < inp:
    loc[1] += min(inp - v, s)
    v += min(inp - v, s)

if v < inp:
    loc[0] -= min(inp - v, s+1)
    v += min(inp - v, s+1)

if v < inp:
    loc[1] -= min(inp - v, s+1)
    v += min(inp - v, s+1)

if v < inp:
    loc[0] += min(inp - v, s+1)
    v += min(inp - v, s+1)

print(abs(loc[0])+abs(loc[1]))

from collections import defaultdict

grid = defaultdict(lambda : 0)
grid[0,0] = 1
loc = [0,0]

dirs = [(1,0),(0,1),(-1,0),(0,-1)]
v = 0
while v < inp:
    loc[0] += dirs[0][0]
    loc[1] += dirs[0][1]
    grid[tuple(loc)] = v = sum(grid[loc[0]+i,loc[1]+j] for i in range(-1,2) \
                           for j in range(-1,2) if (i,j) != (0,0))
    if grid[loc[0]+dirs[1][0],loc[1]+dirs[1][1]] == 0:
        dirs.append(dirs.pop(0))

print(v)
