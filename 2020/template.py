from collections import defaultdict
import functools
import regex
import heapq

nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

# N,E,S,W
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    s = f.read().strip().split("\n")
