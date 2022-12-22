import string
from collections import defaultdict
from aoc_tools import *
import functools
import sys
#sys.setrecursionlimit(10000000)
#       RIGHT0   DOWN1  LEFT2    UP3
dirs = ((0,1),(1,0),(0,-1),(-1,0))
dirs3 = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))

with open(r"input.txt") as f:
    s = f.read()[:-1]#.strip()
print("\n".join(x[:60] for x in s.split("\n")[:6]))

g = defaultdict(lambda : "")

gs, ins = s.split("\n\n")

for i, r in enumerate(gs.split("\n")):
    for j in range(len(r)):
        if r[j] != " ":
            g[i,j] = r[j]

path = ["".join(v) for k, v in itertools.groupby(ins, str.isdigit)]

initx,inity = 0,0
while g[initx,inity] != ".":
    inity += 1


cx,cy,mdir = initx,inity,0



for z,p in enumerate(path):
    #print(z)
    if p == "R":
        mdir = (mdir + 1) % 4
    elif p == "L":
        mdir = (mdir - 1) % 4
    else:
        steps = int(p)
        dx,dy = dirs[mdir]
        for _ in range(steps):
            cx += dx
            cy += dy
            # check if off the board or blocked
            if g[cx,cy] == "#":
                cx -= dx
                cy -= dy
                break
            if g[cx,cy] == "":
                # SLOW!
                nx,ny = cx - dx, cy - dy
                while g[nx,ny] != "":
                    nx -= dx
                    ny -= dy
                nx += dx
                ny += dy
                if g[nx,ny] == "#":
                    cx -= dx
                    cy -= dy
                    break
                cx = nx
                cy = ny

print(1000 * (cx + 1) + 4 * (cy + 1) + mdir)
        
            

# right = +dir

#    5 6    .
#    4     /|\
#  2 3      |
#  1
# 50x50 cells

cx,cy,mdir = initx,inity,0

def region(cx,cy):
    rx = cx//50
    ry = cy//50
    if (rx,ry) == (0,1): return 5
    if (rx,ry) == (0,2): return 6
    if (rx,ry) == (1,1): return 4
    if (rx,ry) == (2,1): return 3
    if (rx,ry) == (2,0): return 2
    if (rx,ry) == (3,0): return 1

def nxt(cx,cy,mdir):
    dx,dy = dirs[mdir]
    r = region(cx,cy)
    invalid = (g[cx + dx, cy + dy] == "")
    if mdir == 0:
        if r == 1 and invalid:
            # bottom of 3
            d = cx - 150
            return (149, 50 + d), 3, 3
        elif r == 3 and invalid:
            # right edge of 6
            d = cx - 100
            return (49 - d, 149), 2, 6
        elif r == 4 and invalid:
            # bottom of 6
            d = cx - 50
            return (49, 100 + d), 3, 6
        elif r == 6 and invalid:
            # right edge of 3
            d = cx
            return (149 - d, 99), 2, 3
        else:
            return (cx+dx, cy+dy), mdir, None
    elif mdir == 1:
        if r == 1 and invalid:
            # top of 6
            d = cy
            return (0, 100 + d), 1, 6
        elif r == 3 and invalid:
            # right of 1
            d = cy - 50
            return (150 + d, 49), 2, 1
        elif r == 6 and invalid:
            # right of 4
            d = cy - 100
            return (50 + d, 99), 2, 4
        else:
            return (cx+dx, cy+dy), mdir, None
    elif mdir == 2:
        if r == 1 and invalid:
            # top of 5
            d = cx - 150
            return (0, 50 + d), 1, 5
        elif r == 2 and invalid:
            # left of 5
            d = cx - 100
            return (49 - d, 50), 0, 5
        elif r == 4 and invalid:
            # top of 2
            d = cx - 50
            return (100, d), 1, 2
        elif r == 5 and invalid:
            # left of 2
            d = cx
            return (149 - d, 0), 0, 2
        else:
            return (cx+dx, cy+dy), mdir, None
    elif mdir == 3: # theory: 0,3
        if r == 2 and invalid:
            # left of 4
            d = cy
            return (50 + d, 50), 0, 4
        elif r == 5 and invalid:
            # left of 1
            d = cy - 50
            return (150 + d, 0), 0, 1
        elif r == 6 and invalid:
            # bottom of 1
            d = cy - 100
            return (199, d), 3, 1
        else:
            return (cx+dx, cy+dy), mdir, None

##        
### correctness test ish
##for (x,y),v in list(g.items()):
##    if v == "": continue
##    for mdir in range(3):
##        (nx,ny),ndir,_ = nxt(x,y,mdir)
##        (nnx,nny),nndir,_ = nxt(nx,ny,(ndir + 2) % 4)
##        assert nnx == x and nny == y and (nndir + 2) % 4 == mdir

        
cx,cy,mdir = initx,inity,0

for z,p in enumerate(path):
    if p == "R":
        mdir = (mdir + 1) % 4
    elif p == "L":
        mdir = (mdir - 1) % 4
    else:
        steps = int(p)
        for _ in range(steps):
            (nx,ny),nmd,nr = nxt(cx,cy,mdir)
            if nr is not None:
                assert region(nx,ny) == nr, "new region chk"
            if g[nx,ny] == "#":
                break
            assert g[nx,ny] == "."
            cx = nx
            cy = ny
            mdir = nmd

print(1000 * (cx + 1) + 4 * (cy + 1) + mdir)

