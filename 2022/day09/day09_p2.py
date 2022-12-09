import string
from aoc_tools import *

with open("input.txt") as f:
    s = f.read().strip()

global rope
rope = [[0,0] for _ in range(10)]

sign = lambda x : 1 if x > 0 else (
    -1 if x < 0 else 0)

# i >= 1
def update(i):
    global rope
    hx,hy = rope[i-1]
    tx,ty = rope[i]
    dx = tx-hx
    dy = ty-hy
    if dx == 0 or dy == 0:
        if abs(dx) >= 2:
            rope[i][0] -= sign(dx)
        if abs(dy) >= 2:
            rope[i][1] -= sign(dy)
    elif (abs(dx),abs(dy)) != (1,1):
        rope[i][0] -= sign(dx)
        rope[i][1] -= sign(dy)


m = {
    "U":(0,1),
    "D":(0,-1),
    "R":(1,0),
    "L":(-1,0)
}

p = set()

for x in s.split("\n"):
    dr,n = x.split(" ")
    n = int(n)
    p.add(tuple(rope[-1]))
    for _ in range(n):
        dx,dy = m[dr]
        rope[0][0] += dx
        rope[0][1] += dy
        for i in range(1,10):
            update(i)
        p.add(tuple(rope[-1]))

print(len(p))
    













        
