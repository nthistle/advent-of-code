from aoc_tools import *

with open("input.txt") as f:
    s = f.read()

s = s.strip().split("\n\n")

s = [[int(x) for x in y.split("\n")] for y in s]

print(max(sum(z) for z in s))

s.sort(key = lambda x : sum(x), reverse=True)

print(sum(sum(z) for z in s[:3]))
