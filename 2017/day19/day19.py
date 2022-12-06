from collections import defaultdict
import functools
import regex
import heapq

# N,E,S,W
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

with open("input.txt") as f:
    s = f.read().strip("\n").split("\n")

g = [list(r) for r in s]

x = 0
y = g[0].index("|")
cdir = 1

st = 0
path = ""
while "Z" not in path:
    while g[x][y] in "|-":
        dx, dy = dirs[cdir]
        x += dx
        y += dy
        st += 1
    if g[x][y].isalpha():
        path += g[x][y]
        x += dx
        y += dy
        st += 1
    elif g[x][y] == "+":
        for ndir in (1,-1):
            ndir = (cdir + ndir) % 4
            dx, dy = dirs[ndir]
            if g[x+dx][y+dy] != " ":
                cdir = ndir
                x += dx
                y += dy
                st += 1
                break
print(path)
print(st)
