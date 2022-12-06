from collections import defaultdict, Counter
import regex

nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    s = f.read().strip().split("\n")

f = nums(s[0])
f = Counter(f)

def proc(x):
    n = defaultdict(int)
    for k,v in f.items():
        if k == 0:
            n[6] += v
            n[8] += v
        else:
            n[k-1] += v
    return n

for _ in range(80):
    f = proc(f)

print(sum(f.values()))

for _ in range(256-80):
    f = proc(f)

print(sum(f.values()))
