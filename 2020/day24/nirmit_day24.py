from collections import defaultdict
#from tqdm import trange
import re
f = open('input.txt').read().strip().split("\n")
dirs = [(1, 0), (.5, -.5), (-.5, -.5), (-1, 0), (-.5, .5), (.5, .5)]

strs = ["e", "se", "sw", "w", "nw", "ne"]
mapping = dict(zip(strs, dirs))

tiles = defaultdict(int)

def evaluate_line(lined):
    x, y = 0, 0
    for d in lined:
        dx, dy = mapping[d]
        x += dx
        y += dy
    return (x, y)


for line in f:
    qwer = []
    i = 0
    while i < len(line):
        if line[i] in "ns":
            qwer.append(line[i:i+2])
            i+= 2
        else:
            qwer.append(line[i])
            i+= 1
    tiles[evaluate_line(qwer)] += 1

print("part 1 answer: ", sum(1 for i, v in tiles.items() if v % 2 == 1))

neighbors_to_add = set((x + dx, y + dy) for dx, dy in dirs for x,y in list(tiles.keys()))
for a in neighbors_to_add:
    if a in tiles:
        pass
    else:
        tiles[a] = 0

print("part 2: ")

import time

st = time.time()

def count_neighbors(psat, loc):
    x, y = loc
    blacks = 0
    for dx, dy in dirs:
        newx, newy = x + dx, y + dy

        if (newx, newy) in psat:
            if psat[(x + dx, y + dy)] % 2 == 1:
                blacks += 1
    
    return blacks

old = tiles
for i in range(100):
    new_day = {}
    for loc, v in old.items():
        n = count_neighbors(old, loc)
        if v % 2 == 1 and (n == 0 or n > 2):
            new_day[loc] = v + 1
        elif v % 2 == 0 and n == 2:
            new_day[loc] = v + 1
        else:
            new_day[loc] = v

    neighbors_to_add = set((x + dx, y + dy) for dx, dy in dirs for x,y in list(new_day.keys()) if new_day[x,y] % 2 == 1)
    for a in neighbors_to_add:
        if a in new_day:
            pass
        else:
            new_day[a] = 0
    old = new_day

print(time.time() - st)
print("answer: ", sum(1 for i, v in old.items() if v % 2 == 1))
