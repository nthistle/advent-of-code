import string
from collections import defaultdict
from aoc_tools import *
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

with open(r"C:\Users\Neil\Documents\AOC2022\day15\input.txt") as f:
    s = f.read().strip()

d = [nums(r) for r in s.split("\n")]

dist = lambda x1,y1,x2,y2 : abs(y2-y1) + abs(x2-x1)

c = 0

for x in range(-9019876, 9019876):
    if x % 100_000 == 0:
        print(x)
    y = 2000000
    poss = True
    for sx,sy,bx,by in d:
        if (x,y) == (bx,by):
            poss = True
            break
        if dist(sx,sy,x,y) <= dist(sx,sy,bx,by):
            poss = False
            break
    if not poss:
        c += 1
print(c)
