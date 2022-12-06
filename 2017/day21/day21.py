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
    s = f.read().strip("\n").split("\n")

rules = {}
for ln in s:
    l,r = ln.split(" => ")
    rules[tuple(l.split("/"))] = r.split("/")

def flip(g):
    return [r[::-1] for r in g]

def rot(g):    
    n = len(g)
    m = len(g[0])
    out = [[] for _ in range(m)]
    for i in range(len(g)):
        for j in range(len(g[0])-1,-1,-1):
            out[len(g[0]) - j - 1].append(g[i][j])
    return out

def apply(block):
    for b1 in (block,flip(block)):
        for b2 in (b1,rot(b1),rot(rot(b1)),rot(rot(rot(b1)))):
            b2 = tuple("".join(r) for r in b2)
            if b2 in rules:
                return rules[b2]


cur = tuple(".#./..#/###".split("/"))
for _ in range(18):
    #print()
    #print("\n".join(cur))
    w = len(cur)
    if w % 2 == 0:
        nw = 3*(w//2)
        new = ["" for _ in range(nw)]
        for i in range(0,w,2):
            for j in range(0,w,2):
                block = tuple("".join(cur[i+di][j+dj] for dj in range(2)) \
                              for di in range(2))
                new_block = apply(block)
                for k in range(3):
                    new[3*(i//2)+k] += new_block[k]
    else:
        nw = 4*(w//3)
        new = ["" for _ in range(nw)]
        for i in range(0,w,3):
            for j in range(0,w,3):
                block = tuple("".join(cur[i+di][j+dj] for dj in range(3)) \
                              for di in range(3))
                new_block = apply(block)
                for k in range(4):
                    new[4*(i//3)+k] += new_block[k]
    cur = new

print(sum(1 for r in cur for c in r if c == "#"))







    
