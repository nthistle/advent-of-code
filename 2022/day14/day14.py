import string
from collections import defaultdict
#from aoc_tools import *
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

with open(r"C:\Users\Neil\Documents\AOC2022\day14\input.txt") as f:
    s = f.read().strip()
print("\n".join(x[:60] for x in s.split("\n")[:6]))

s = s.split("\n")
s = [[tuple(nums(x)) for x in line.split(" -> ")] for line in s]
# added for pypy
#s = [[tuple(map(int,x.split(","))) for x in line.split(" -> ")] for line in s]

sand = (500,0)

# 0 -> air
# 1 -> solid
# 2 -> solid sand
grid = defaultdict(lambda : 0)
for line in s:
    for (ax,ay),(bx,by) in zip(line,line[1:]):
        dx = bx-ax
        if dx != 0:
            dx = dx // abs(dx)
        dy = by-ay
        if dy != 0:
            dy = dy // abs(dy)
        while (ax,ay) != (bx,by):
            grid[ax,ay] = 1
            ax += dx
            ay += dy
        grid[ax,ay] = 1

maxy = max(y for x,y in grid)

for x in range(-1000,1000):
    grid[x,maxy+2] = 1

part = 2

sx,sy = sand
while True:
    blocked = True
    for dx,dy in ((0,1),(-1,1),(1,1)):
        if grid[(sx+dx,sy+dy)] == 0:
            sx += dx
            sy += dy
            blocked = False
            break
    if part == 1 and sy > maxy:
        break
    if blocked:
        grid[sx,sy] = 2
        if (sx,sy) == sand:
            break
        sx,sy = sand

print(sum(1 for v in grid.values() if v == 2))





































