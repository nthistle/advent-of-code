from collections import defaultdict, Counter
import regex
import itertools

nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    s = f.read().strip().split("\n")

g = [[int(x) for x in y] for y in s]


n = len(g)
m = len(g[0])

ng = []
for i in range(n):
    cm = g[i]
    nr = []
    for _ in range(5):
        nr.extend(cm)
        cm = [cmx + 1 if cmx < 9 else 1 for cmx in cm]
    ng.append(nr)

first = [ngr[:] for ngr in ng]
for _ in range(4):
    # add 1
    first = [[x + 1 if x < 9 else 1 for x in r] for r in first]
    for row in first:
        ng.append(row)

part2 = True
if part2:
    g = ng
    n = len(ng)
    m = len(ng[0])

import heapq

pq = []

heapq.heappush(pq, (0, (0,0)))
dist = {}
dist[0,0] = 0
while True:
    d, (x,y) = heapq.heappop(pq)
    if (x,y) == (n-1,m-1):
        print(d)
        break
    for dx,dy in ((-1,0),(0,1),(0,-1),(1,0)):
        nx,ny = x+dx,y+dy
        if nx not in range(n) or ny not in range(m):
            continue
        nd = d + g[nx][ny]
        if (nx,ny) not in dist or nd < dist[nx,ny]:
            dist[nx,ny] = nd
            heapq.heappush(pq, (nd, (nx, ny)))
