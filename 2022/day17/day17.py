import string
from collections import defaultdict
from aoc_tools import *
import functools
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

with open(r"lukeinput.txt") as f:
    s = f.read().strip()
print("\n".join(x[:60] for x in s.split("\n")[:6]))

#s = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

pieces = [
    
    [[1,1,1,1],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]],
    
    [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [0,0,0,0]],
    
    [[0,0,1,0],
     [0,0,1,0],
     [1,1,1,0],
     [0,0,0,0]],
    
    [[1,0,0,0],
     [1,0,0,0],
     [1,0,0,0],
     [1,0,0,0]],

    [[1,1,0,0],
     [1,1,0,0],
     [0,0,0,0],
     [0,0,0,0]],
]

pieces = [
    
    [[1,0,0,0],
     [1,0,0,0],
     [1,0,0,0],
     [1,0,0,0]],
    
    [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [0,0,0,0]],
    
    [[0,0,1,0],
     [0,0,1,0],
     [1,1,1,0],
     [0,0,0,0]],
    
    [[1,1,1,1],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]],

    [[1,1,0,0],
     [1,1,0,0],
     [0,0,0,0],
     [0,0,0,0]],
]

plow = [
    3, 1, 1, 0, 2
    ]

# maxy + 3 + 4 - zerosbot = 6?


global px,py,grid,pid

grid = defaultdict(int)

# px,py are going to be top left of the 4x4 piece grid

# 0,0 bottom left
# down is 0,-1
# right is 1,0
# left is -1,0

pid = 0
px,py = 0,0

maxy = -1
px = 2
py = maxy + 3 + 4 - plow[pid]

# NOTE: MAXY STARTS -1

def movepiece(dx,dy):
    global px,py,grid,pid
    npx,npy = px + dx, py + dy
    for i in range(4):
        for j in range(4):
            if pieces[pid][i][j] == 0: continue
            rpx = npx + i
            rpy = npy - j
            if rpx not in range(7):
                return False
            if rpy < 0:
                return False
            if grid[rpx,rpy] != 0:
                return False
    # piece can move!
    px += dx
    py += dy
    return True


# if you have some function f : X -> X

# observe a sequence {a_n} where a_n = f(a_{n-1})

# a: 1 -> 3 -> 8 -> 4 -> 9 -> 14 -> 8 -> 4 -> ...

# what's the 1,000,000,000 term in this sequence?



def movedown():
    global px,py,grid,pid
    if not movepiece(0,-1):
        for i in range(4):
            for j in range(4):
                if pieces[pid][i][j] == 0: continue
                rpx = px + i
                rpy = py - j
                assert grid[rpx,rpy] == 0
                grid[rpx,rpy] = 1
        return False
    return True

def gen_top_view():
    global grid
    maxys = [-17 for _ in range(7)]
    for (x,y),v in grid.items():
        if v == 1:
            maxys[x] = max(maxys[x], y)
    v = max(maxys)
    return tuple(m - v for m in maxys)

seen = {}

nump = 0
additional = 0
while nump < 1000000000000:
#while nump < 2022:
    for vid,c in enumerate(s):
        if c == "<":
            movepiece(-1,0)
        elif c == ">":
            movepiece(1,0)
        if not movedown():
            # piece is now locked, add new one
            maxy = 0
            for (_,y),v in grid.items():
                if v == 1:
                    maxy = max(maxy, y)
            pid = (pid + 1) % len(pieces)
            px = 2
            py = maxy + 3 + 4 - plow[pid]
            nump += 1
            #if nump >= 2022:
            #    break
            if nump >= 1000000000000:
                break
            ### ADD TO SEEN
            topv = gen_top_view()
            #pid
            #vid
            if (topv,pid,vid) in seen:
                oldnump,oldmaxy = seen[topv,pid,vid]
                print("!",nump,oldnump)
                # if we place another (nump - oldnump) pieces, we arrive
                # in the same configuration, with extra height (maxy - oldmaxy)
                repeat = (1000000000000 - nump) // (nump - oldnump)
                nump += (nump - oldnump) * repeat
                additional += repeat * (maxy - oldmaxy)
                # just so we don't print again
                seen = {}
                
            seen[topv,pid,vid] = (nump,maxy)
##        print("\n".join("".join("#" if grid[x,y] == 1 else "." \
##                                for x in range(7)) \
##                        for y in range(20,-1,-1)))
##        _ = input()

maxy = 0
for (_,y),v in grid.items():
    if v == 1:
        maxy = max(maxy, y)
        
# print(maxy + 1)
print(maxy + 1 + additional)


# on a piece lockin, the state is described by
# ("top of the tower") ~= 7 ints of depths from looking from above
# pid
# vent sequence location













































