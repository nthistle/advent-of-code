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

r,m = s.split("\n\n")

ms = m.split("\n")
r = r.split("\n")

rs = {}
for l in r:
    a,b = l.split(": ")
    b = b.split(" | ")
    if '"' in l:
        rs[int(a)] = b[0].strip('"')
    else:
        rs[int(a)] = [[int(x) for x in y.split(" ")] for y in b]

cache = {}
def m(rn,s):
    if type(rs[rn]) is str:
        return s == rs[rn]
    if (rn,s) not in cache:
        for i in range(1,len(s)+1):
            a,b = s[:i], s[i:]
            for k in rs[rn]:
                if len(k) == 1:
                    if m(k[0],s):
                        cache[rn,s] = True
                        return True
                else:
                    c,d = k
                    if m(c,a) and m(d,b):
                        cache[rn,s] = True
                        return True
        cache[rn,s] = False
    return cache[rn,s]

import itertools

pos = {}
def p(rn):
    if rn in pos:
        return pos[rn]
    if type(rs[rn]) is str:
        pos[rn] = [rs[rn]]
        return pos[rn]
    pos[rn] = []
    for vd in rs[rn]:
        pos[rn].extend([''.join(nl) for nl in itertools.product(*[p(nr) for nr in vd])])
    return pos[rn]


##c = 0
##for mi in ms:
##    if m(0, mi):
##        c += 1
##print(c)

c = 0
r0 = p(0)
for mi in ms:
    if mi in r0:
        c += 1
print(c)


r42 = p(42)
r31 = p(31)

c = 0
for mi in ms:
    if len(mi)%8 != 0:
        continue
    bc = [mi[i:i+8] for i in range(0,len(mi),8)]
    dx = 0
    c42 = 0
    while dx < len(bc) and bc[dx] in r42:
        dx += 1
        c42 += 1
    c31 = 0
    while dx < len(bc) and bc[dx] in r31:
        dx += 1
        c31 += 1
    if dx == len(bc) and c31 < c42 and c31 > 0:
        c += 1
print(c)
