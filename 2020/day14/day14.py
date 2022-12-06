from collections import defaultdict
import functools
import regex

nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    s = f.read().strip().split("\n")

mem = defaultdict(lambda : 0)

and_mask = (1<<40)-1
or_mask = 0

for line in s:
    if line.startswith("mask ="):
        bits = list(line[7:])
        and_mask = (1<<40)-1
        or_mask = 0
        for i,b in enumerate(bits[::-1]):
            if b == '0':
                and_mask &= ((1<<40)-1)^(1<<i)
            elif b == '1':
                or_mask |= (1<<i)
    else:
        a,b = nums(line)
        mem[a] = (b & and_mask) | or_mask

print(sum(mem[a] for a in mem))

mem = defaultdict(lambda : 0)

ones = []
xs = []

for line in s:
    if line.startswith("mask ="):
        bits = list(line[7:])
        ones = []
        xs = []
        for i,b in enumerate(bits[::-1]):
            if b == '1':
                ones.append(i)
            elif b == 'X':
                xs.append(i)
    else:
        a,b = nums(line)
        for mask in range(1<<len(xs)):
            vals = [((mask)>>i)&1 for i in range(len(xs))]
            write = a
            for o in ones:
                write |= (1 << o)
            for loc,v in zip(xs,vals):
                if (write >> loc) & 1:
                    write ^= (1 << loc)
                if v == 1:
                    write |= (1 << loc)
            mem[write] = b

print(sum(mem[a] for a in mem))
