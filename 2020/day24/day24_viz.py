from collections import defaultdict
import numpy as np

with open("input.txt") as f:
    s = f.read().strip("\n")

def minmax(iterable,default=None):
    iterator = iter(iterable)
    min_val = (default if default is not None else next(iterator))
    max_val = min_val
    try:
        while True:
            item = next(iterator)
            min_val = min(min_val, item)
            max_val = max(max_val, item)
    except StopIteration:
        pass
    return min_val, max_val

mask = [[0,0,0,1,1,0,0,0],
        [0,1,1,1,1,1,1,0],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [0,1,1,1,1,1,1,0],
        [0,0,0,1,1,0,0,0]]

outl = [[0,0,0,1,1,0,0,0],
        [0,1,1,0,0,1,1,0],
        [1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,1],
        [0,1,1,0,0,1,1,0],
        [0,0,0,1,1,0,0,0]]

def draw_tiles(minx,maxx,miny,maxy,tiles,buf=None,border=True):
    img = defaultdict(lambda : 255)
    for t in tiles:
        x,y = t
        rx,ry = (7*x-7*y,4*(x+y))
        for i in range(len(mask)):
            for j in range(len(mask[i])):
                if mask[i][j]:
                    img[rx+i,ry+j] = (0 if tiles[t] else 255)

    if border:
        mintx,maxtx = -13,13#minmax(map(lambda x : x[0], tiles.keys()))
        minty,maxty = -13,13#minmax(map(lambda x : x[0], tiles.keys()))
        for x in range(mintx-(maxtx-mintx),maxtx+(maxtx-mintx)):
            for y in range(minty-(maxty-minty),maxty+(maxty-minty)):
                rx,ry = (7*x-7*y,4*(x+y))
                for i in range(len(mask)):
                    for j in range(len(mask[i])):
                        if outl[i][j]:
                            img[rx+i,ry+j] = 0

    if buf is None:
        buf = np.zeros((maxx-minx+1,maxy-miny+1,3), dtype=np.uint8)
    for i in range(minx,maxx+1):
        for j in range(miny,maxy+1):
            buf[i-minx,j-miny,:] = img[i,j]

    return buf


s = s.split("\n")

# False = White
tiles = defaultdict(lambda : False)

import cv2

buf = draw_tiles(-98,106,-111,118,tiles)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
clip_writer = cv2.VideoWriter("vis.mp4", fourcc, 24, buf.shape[:2][::-1])
clip_writer.write(buf)

for ln in s:
    cur = [0,0]
    while len(ln)>0:
        if ln[0] == 'e' or ln[0] == 'w':
            if ln[0] == 'e':
                cur[0] += 1
                cur[1] += 1
            else:
                cur[0] -= 1
                cur[1] -= 1
            ln = ln[1:]
        else:
            tk = ln[:2]
            ln = ln[2:]
            if tk == 'se':
                cur[1] += 1
            elif tk == 'ne':
                cur[0] += 1
            elif tk == 'nw':
                cur[1] -= 1
            elif tk == 'sw':
                cur[0] -= 1
    tiles[tuple(cur)] = not tiles[tuple(cur)]
    draw_tiles(-98,106,-111,118,tiles,buf=buf)
    clip_writer.write(buf)

for _ in range(23):
    clip_writer.write(buf)

clip_writer.release()

nbs = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)]

print(sum(tiles.values()))

#minx,maxx = minmax(map(lambda x : x[0], img.keys()))
#miny,maxy = minmax(map(lambda x : x[1], img.keys()))
##minx,maxx = (-98, 106)
##miny,maxy = (-111, 118)
