import string
from aoc_tools import *

with open("input.txt") as f:
    s = f.read().strip()

global hx,hy,tx,ty
hx,hy = 0,0
tx,ty = 0,0

sign = lambda x : 1 if x > 0 else (
    -1 if x < 0 else 0)

def updt():
    global hx,hy,tx,ty
    dx = tx-hx
    dy = ty-hy
    if abs(dx) >= 2:
        tx -= sign(dx)
    if abs(dy) >= 2:
        ty -= sign(dy)

def updt():
    global hx,hy,tx,ty
    dx = tx-hx
    dy = ty-hy
    if dx == 0 or dy == 0:
        if abs(dx) >= 2:
            tx -= sign(dx)
        if abs(dy) >= 2:
            ty -= sign(dy)
    elif (abs(dx),abs(dy)) != (1,1):
        tx -= sign(dx)
        ty -= sign(dy)


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
    p.add((tx,ty))
    for _ in range(n):
        dx,dy = m[dr]
        hx += dx
        hy += dy
        updt()
        p.add((tx,ty))

print(len(p))
    













        
