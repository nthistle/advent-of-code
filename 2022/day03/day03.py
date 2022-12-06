from aoc_tools import *

with open("input.txt") as f:
    s = f.read().strip()

s = s.split("\n")

import string
p = lambda c : ord(c) - ord('a') + 1 if c in string.ascii_lowercase else (
    ord(c) - ord("A") + 27)


r = 0
for c in s:
    c1 = c[:len(c)//2]
    c2 = c[len(c)//2:]
    z = set(c1) & set(c2)
    assert len(z) == 1
    r += p(list(z)[0])

print(r)



r = 0
for i in range(0,len(s),3):
    z = set(s[i]) & set(s[i+1]) & set(s[i+2])
    assert len(z) == 1
    r += p(list(z)[0])

print(r)
