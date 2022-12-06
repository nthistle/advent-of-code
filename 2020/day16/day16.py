from collections import defaultdict
import functools
import regex
import heapq

nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

# N,E,S,W
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    s = f.read().strip().split("\n\n")

N = 20

aa,bb,cc = s

lookup = {}
ii = 0
ranges = []
for line in aa.strip().split("\n"):
    k,v = line.split(": ")
    v1,v2 = v.split(" or ")
    v11,v12 = map(int,v1.split("-"))
    v21,v22 = map(int,v2.split("-"))
    #ranges[k] = ((v11,v12),(v21,v22))
    ranges.append((v11,v12,v21,v22))
    lookup[k] = ii
    ii += 1

def any_valid(v):
    return any(a <= v <= b or c <= v <= d for a,b,c,d in ranges)

good = []
err = 0
for tick in cc.split("\n")[1:]:
    tick = list(map(int,tick.split(",")))
    for val in tick:
        if not any_valid(val):
            err += val
    if all(any_valid(v) for v in tick):
        good.append(tick)
good.append(list(map(int,bb.split("\n")[1].split(","))))

print(err)

positions = []
for i,field in enumerate(ranges):
    a,b,c,d = field
    valid = set(range(N))
    for tick in good:
        for j in range(N):
            if not (a <= tick[j] <= b or c <= tick[j] <= d):
                if j in valid:
                    valid.remove(j)
    positions.append(valid)

vals = [-1 for _ in range(N)]

def assign(i,v):
    vals[i] = v
    for p in positions:
        if v in p:
            p.remove(v)

def show():
    for i in range(N):
        print(i,":",positions[i])

while -1 in vals:
    for i in range(N):
        if len(positions[i]) == 1:
            v = next(iter(positions[i]))
            assign(i,v)

for tick in good:
    for i in range(N):
        a,b,c,d = ranges[i]
        fn = vals[i]
        if not (a <= tick[fn] <= b or c <= tick[fn] <= d):
            print(tick,i)

out = 1
for k in lookup:
    if k.startswith("departure"):
        idx = vals[lookup[k]]
        out *= good[-1][idx]
print(out)




