import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from aoc_lib import *

s = get_input().split("\n")

s = """F10
N3
F7
R90
F11""".split("\n")

dirs = {"N":(0,1),"S":(0,-1),"E":(1,0),"W":(-1,0)}

lookup = {0:"E",90:"N",180:"W",270:"S"}

angle = 0
loc = [0,0]

for ln in s:
    v,nv = ln[0],int(ln[1:])
    if v in dirs:
        dx,dy = dirs[v]
        loc[0] += nv*dx
        loc[1] += nv*dy
    else:
        if v == "L":
            angle = (angle + nv) % 360
        elif v == "R":
            angle = (angle - nv) % 360
        else:
            dx,dy = dirs[lookup[angle]]
            loc[0] += nv*dx
            loc[1] += nv*dy

print(abs(loc[0])+abs(loc[1]))


wp = [10,1]

angle = 0
loc = [0,0]

for ln in s:
    v,nv = ln[0],int(ln[1:])
    if v in dirs:
        dx,dy = dirs[v]
        wp[0] += nv*dx
        wp[1] += nv*dy
    else:
        if v == "L":
            for _ in range(nv//90):
                wp = [-wp[1], wp[0]]
        elif v == "R":
            for _ in range(nv//90):
                wp = [wp[1], -wp[0]]
        else:
            for _ in range(nv):
                loc[0] += wp[0]
                loc[1] += wp[1]

print(abs(loc[0])+abs(loc[1]))
