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

p = []
for l in s.split("\n"):
    p.append(tuple(map(int,l.split("/"))))

lookup = defaultdict(set)
for i,(a,b) in enumerate(p):
    lookup[a].add(i)
    lookup[b].add(i)

def recur(cur, used):
    poss = [i for i in lookup[cur] if not used[i]]
    m = 0
    for pi in poss:
        used[pi] = True
        new = (p[pi][0] if p[pi][1] == cur else p[pi][1])
        m = max(m, sum(p[pi]) + recur(new, used))
        used[pi] = False
    return m

def longest(cur, used):
    poss = [i for i in lookup[cur] if not used[i]]
    m = 0
    for pi in poss:
        used[pi] = True
        new = (p[pi][0] if p[pi][1] == cur else p[pi][1])
        m = max(m, 1 + longest(new, used))
        used[pi] = False
    return m

print(recur(0, [False for _ in range(len(p))]))
length = longest(0, [False for _ in range(len(p))])

def recur(cur, used):
    poss = [i for i in lookup[cur] if not used[i]]
    m = 0
    for pi in poss:
        used[pi] = True
        new = (p[pi][0] if p[pi][1] == cur else p[pi][1])
        m = max(m, sum(p[pi]) + recur(new, used) + 10000000 * (sum(used) == length))
        used[pi] = False
    return m

print(recur(0, [False for _ in range(len(p))]) - 10000000)
