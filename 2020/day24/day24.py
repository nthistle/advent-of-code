from collections import defaultdict
import functools
import regex
import heapq

nums_regex = regex.compile("^([^\\d]*?)((?P<nums>\\-?\\d+)([^\\d]*?))*$")

# N,E,S,W
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    s = f.read().strip("\n")

s = s.split("\n")

# False = White
tiles = defaultdict(lambda : False)

for ln in s:
    cur = [0,0,0]
    while len(ln)>0:
        if ln[0] == 'e' or ln[0] == 'w':
            if ln[0] == 'e':
                cur[1] += 1
            else:
                cur[1] -= 1
            ln = ln[1:]
        else:
            tk = ln[:2]
            ln = ln[2:]
            if tk == 'se':
                cur[2] += 1
            elif tk == 'ne':
                cur[0] += 1
            elif tk == 'nw':
                cur[2] -= 1
            elif tk == 'sw':
                cur[0] -= 1
    cur[0] += cur[1]
    cur[2] += cur[1]
    cur[1] = 0
    tiles[tuple(cur)] = not tiles[tuple(cur)]

nbs = [(1,0,0),(-1,0,0),(0,0,1),(0,0,-1),(1,0,1),(-1,0,-1)]

print(sum(tiles.values()))

def upd(tiles):
    ntiles = defaultdict(lambda : False)

    cnt = defaultdict(lambda : 0)
    for x,y,z in tiles:
        if tiles[x,y,z]:
            for dx,dy,dz in nbs:
                nx,ny,nz = x+dx,y+dy,z+dz
                cnt[nx,ny,nz] += 1

    check = set(cnt.keys()).union(set(tiles.keys()))
    for x,y,z in check:
        if tiles[x,y,z]:
            if cnt[x,y,z] == 0 or cnt[x,y,z] > 2:
                ntiles[x,y,z] = False
            else:
                ntiles[x,y,z] = True
        else:
            if cnt[x,y,z] == 2:
                ntiles[x,y,z] = True
            else:
                pass
    return ntiles

tiles = tiles
for _ in range(100):
    tiles = upd(tiles)
            
