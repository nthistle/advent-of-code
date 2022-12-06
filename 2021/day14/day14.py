from collections import defaultdict, Counter
import regex
import itertools

nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    a, b = f.read().strip().split("\n\n")
b = b.split("\n")
rules = {}
for x in b:
    z,y = x.split(" -> ")
    rules[z] = y
    
def apply(s):
    out = ""
    for a,b in zip(s,s[1:]):
        out += a
        out += rules[a+b]
    out += s[-1]
    return out

def apply(d):
    nd = defaultdict(int)
    for px,py in d.keys():
        r = rules[px+py]
        nd[px,r] += d[px,py]
        nd[r,py] += d[px,py]
    return nd

d = defaultdict(int)
for x,y in zip(a,a[1:]):
    d[x,y] += 1

for _ in range(40):
    d = apply(d)

c = defaultdict(int)
for x,y in d.keys():
    c[x] += d[x,y]
    c[y] += d[x,y]

print(max(c.values()) - min(c.values()))
    
## A B C

# AB : 1
# BC : 1
