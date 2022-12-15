import string
from collections import defaultdict
from aoc_tools import *
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

with open(r"C:\Users\Neil\Documents\AOC2022\day15\input.txt") as f:
    s = f.read().strip()
#print("\n".join(x[:60] for x in s.split("\n")[:6]))

d = [nums(r) for r in s.split("\n")]

dist = lambda x1,y1,x2,y2 : abs(y2-y1) + abs(x2-x1)

c = 0
# (sum>, sum<, x-y>, x-y<)
constraints = []

# if sx,sy = (5,5)
# z = 3
#
# 2,5 => 7
#
# 7,6 = 13
# 8,5 = 13
# 9,4 = 13
#

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
print(s.model())

###for x in range(-4619876, 4619876):
##for x in range(-9019876, 9019876):
##    if x % 100_000 == 0:
##        print(x)
##    y = 2000000
##    poss = True
##    for sx,sy,bx,by in d:
##        if (x,y) == (bx,by):
##            poss = True
##            break
##        if dist(sx,sy,x,y) <= dist(sx,sy,bx,by):
##            poss = False
##            break
##    if not poss:
##        c += 1
##print(c)





























