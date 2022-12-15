import string
from collections import defaultdict
from aoc_tools import *
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

with open(r"C:\Users\Neil\Documents\AOC2022\day15\input.txt") as f:
    s = f.read().strip()

d = [nums(r) for r in s.split("\n")]

dist = lambda x1,y1,x2,y2 : abs(y2-y1) + abs(x2-x1)

constraints = []
for sx,sy,bx,by in d:
    z = dist(sx,sy,bx,by)
    # must be the case that |ty-sy|+|tx-sx|>z
    # +,+ ty-sy+tx-sx>z
    # +,+ ty+tx>z+sx+sy
    # -,+ -ty+sy+tx-sx>z
    # -,+ tx-ty>z+sx-sy
    # +,- ty-sy-tx+sx>z
    # +,- -tx+ty>z-sx+sy
    # +,- tx-ty<-z+sx-sy
    # -,- -ty+sy-tx+sx>z
    # -,- -(tx+ty)>z-sx-sy
    # -,- tx+ty<-z+sx+sy
    constraints.append(
        (z + sx + sy, -z + sx + sy, z + sx - sy, -z + sx - sy)
    )

from z3 import *
x = Int("x")
y = Int("y")
sumxy = x + y
difxy = x - y
s = Solver()
for a,b,c,d in constraints:
    s.add(Or((sumxy > a), (sumxy < b), (difxy > c), (difxy < d)))
s.add(x >= 0)
s.add(x <= 4000000)
s.add(y >= 0)
s.add(y <= 4000000)
print(s.check())
print(s.model()[x].as_long() * 4000000 + s.model()[y].as_long())
