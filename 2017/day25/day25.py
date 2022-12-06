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

s = s.split("\n\n")

start, diag = s[0].split("\n")
start = start[-2]
diag, = nums(diag)

t = {}
for ti in s[1:]:
    st, _, wr0, mv0, ns0, _, wr1, mv1, ns1 = ti.split("\n")
    st = st[-2]
    wr0 = int(wr0[-2])
    mv0 = (+1 if "right" in mv0 else -1)
    ns0 = ns0[-2]
    wr1 = int(wr1[-2])
    mv1 = (+1 if "right" in mv1 else -1)
    ns1 = ns1[-2]
    t[st] = ((wr0,mv0,ns0),(wr1,mv1,ns1))

tape = defaultdict(lambda : 0)
cur_loc = 0
cur_st = start

for _ in range(diag):
    read = tape[cur_loc]
    wr,mv,ns = t[cur_st][read]
    tape[cur_loc] = wr
    cur_loc += mv
    cur_st = ns

print(sum(tape.values()))





