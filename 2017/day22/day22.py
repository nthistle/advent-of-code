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

s = [list(x) for x in s.split("\n")]

g = defaultdict(lambda : False)

n,m = len(s),len(s[0])

for i in range(n):
    for j in range(m):
        if s[i][j] == "#":
            g[i,j] = True

c = [n//2,m//2]
d = 3

cnt = 0
for _ in range(10000):
    if g[tuple(c)]:
        d = (d+1)%4
    else:
        d = (d-1)%4
        cnt += 1
        
    g[tuple(c)] = not g[tuple(c)]

    c[0] += dirs[d][0]
    c[1] += dirs[d][1]

print(cnt)

g = defaultdict(lambda : 0)

for i in range(n):
    for j in range(m):
        if s[i][j] == "#":
            g[i,j] = 2

c = [n//2,m//2]
d = 3

cnt = 0

for _ in range(10000000):
    if g[tuple(c)] == 0:
        d = (d-1)%4
    elif g[tuple(c)] == 1:
        cnt += 1
    elif g[tuple(c)] == 2:
        d = (d+1)%4
    elif g[tuple(c)] == 3:
        d = (d+2)%4

    g[tuple(c)] = (g[tuple(c)]+1)%4

    c[0] += dirs[d][0]
    c[1] += dirs[d][1]

print(cnt)

