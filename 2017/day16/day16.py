from collections import defaultdict
import functools
import regex

nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    s = f.read().strip().split(",")

import time


progs = list("abcdefghijklmnop")

st = time.time()

for m in s:
    if m[0] == "s":
        x = int(m[1:])
        progs = progs[-x:] + progs[:-x]
    elif m[0] == "x":
        a,b = map(int,m[1:].split("/"))
        progs[a], progs[b] = progs[b], progs[a]
    elif m[0] == "p":
        a,b = map(progs.index,m[1:].split("/"))
        progs[a], progs[b] = progs[b], progs[a]

et = time.time()
print("".join(progs))

seen = {}

progs = list("abcdefghijklmnop")

iters = 1_000_000_000

while iters > 0:
    str_rep = "".join(progs)
    if str_rep in seen:
        cycle_length = seen[str_rep] - iters
        iters %= cycle_length
        seen = {}
    seen[str_rep] = iters
    for m in s:
        if m[0] == "s":
            x = int(m[1:])
            progs = progs[-x:] + progs[:-x]
        elif m[0] == "x":
            a,b = map(int,m[1:].split("/"))
            progs[a], progs[b] = progs[b], progs[a]
        elif m[0] == "p":
            a,b = map(progs.index,m[1:].split("/"))
            progs[a], progs[b] = progs[b], progs[a]
    iters -= 1

print("".join(progs))


