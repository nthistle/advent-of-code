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

d = []
for l in s:
    ing, a = l.split(" (")
    a = a.strip("()")[len("contains "):]
    d.append((ing.split(" "), a.split(", ")))

n = defaultdict(set)
an = defaultdict(list)
for i,a in d:
    for al in a:
        an[al].append(i)
        for ii in i:
            n[ii].add(al)

poss = defaultdict(list)
np = set()
for i,a in n.items():
    good = True
    for al in a:
        # does i appear in all of an[a]
        if all(i in anl for anl in an[al]):
            good = False
            poss[i].append(al)
    if good:
        np.add(i)

c = 0
for i,a in d:
    for ii in i:
        if ii in np:
            c += 1
print(c)

while any(len(v) != 1 for v in poss.values()):
    for k in poss:
        if len(poss[k]) == 1: # remove it from all others
            v = next(iter(poss[k]))
            for k2,v2 in poss.items():
                if k == k2:
                    continue
                if v in v2:
                    poss[k2].remove(v)

ing = list(poss.items())
ing.sort(key = lambda x : x[1])
print(",".join(x[0] for x in ing))
