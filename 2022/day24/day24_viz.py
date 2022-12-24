import string
from collections import defaultdict
from aoc_tools import *
import functools
import sys
import numpy as np
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

import numpy as np
import cv2

FACTOR = 5
buf = np.zeros((N+2, M+2, 3), dtype=np.uint8)
nbuf = np.zeros((FACTOR * (N+2),
                 FACTOR * (M+2),
                 3), dtype=np.uint8)
    
def upsamp(buf):
    for i in range(nbuf.shape[0]):
        for j in range(nbuf.shape[1]):
            nbuf[i,j] = buf[i//FACTOR,j//FACTOR]
    
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
clip_writer = cv2.VideoWriter("viz.mp4", fourcc, 24, nbuf.shape[:2][::-1])

occupied = set()
st = (0,1)
gl = (26,120)
dist = defaultdict(lambda : float("inf"))
q = deque()
q.append((st, 0))
dist[st] = 0
dups = set()
maxdist = -1
most = 0
while True:
    (cx,cy),cd = q.popleft()
    if (cx,cy)==gl:
        print(cx,cy,cd)
        break
    if cd > maxdist:
        # PAINT
        print(cd, maxdist)
        per = defaultdict(int)
        for x,y,_ in blizz_locs:
            per[x,y] += 1
        frontier = set()
        frontier.add((cx,cy))
        for (x,y),_ in q:
            frontier.add((x,y))
        for i in range(N+2):
            for j in range(M+2):
                if g[i][j] == "#":
                    buf[i][j] = (255,255,255)
                else:
                    buf[i][j] = (0,0,0)
                    num_t = per[i,j]
                    if num_t > 0:
                        if num_t > most:
                            most = num_t
                            print("new max",most)
                        c = min(255, 100 + 40 * num_t)
                        buf[i][j] = (c,c,c)
                    elif (i,j) in frontier:
                        buf[i][j] = (0,255,0)
        upsamp(buf)
        clip_writer.write(nbuf)
        
        maxdist = cd
        nxt()
        occupied = set()
        for i,j,_ in blizz_locs:
            occupied.add((i,j))
    for dx,dy in dirs + ((0,0),):
        nx,ny = cx + dx, cy + dy
        if (nx,ny) not in occupied and nx in range(1,1+N) and ny in range(1,1+M) or \
           (nx,ny) == st or (nx,ny) == gl:
            if (nx,ny,cd) not in dups:
                dups.add((nx,ny,cd))
                q.append(((nx,ny), cd + 1))
            

clip_writer.release()














































