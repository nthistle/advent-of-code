from collections import defaultdict, Counter
import regex

nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    s = f.read().strip()

x = nums(s)

print(min(sum(abs(y-t) for y in x) for t in range(0,2000)))

cost = [0]
for i in range(1,2000):
    cost.append(cost[-1] + i)

print(min(sum(cost[abs(y-t)] for y in x) for t in range(0,2000)))
