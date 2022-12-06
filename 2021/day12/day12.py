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

g = defaultdict(set)
p = {}

for l in s:
    a,b = l.split("-")
    g[a].add(b)
    g[b].add(a)


def dfs(c,d,seen,path):
    if c == "end":
        return 1
    r = 0
    for a in g[c]:
        big = a[0].isupper()
        if seen[a] == 0:
            if not big:
                seen[a] += 1
            r += dfs(a,d,seen,path)
            if not big:
                seen[a] -= 1
        elif seen[a] == 1 and not d:
            if not big:
                seen[a] += 1
            r += dfs(a,True,seen,path)
            if not big:
                seen[a] -= 1
    return r

dd = defaultdict(int)
dd["start"] = 2

print(dfs("start",False,dd,["start"]))
