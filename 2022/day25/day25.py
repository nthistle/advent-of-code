import string
from collections import defaultdict
from aoc_tools import *
import functools
import sys
sys.setrecursionlimit(100000)
dirs = ((0,1),(1,0),(0,-1),(-1,0))
dirs3 = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))

with open(r"input.txt") as f:
    s = f.read().strip()
#print("\n".join(x[:60] for x in s.split("\n")[:6]))

m = {"2":2,"1":1,"0":0,"-":-1,"=":-2}
def conv(x):
    a = [1]
    while len(a)<len(x):
        a.append(5 * a[-1])
    a.reverse()
    return sum(ac * m[v] for ac,v in zip(a, x))
    
s = s.split("\n")
r = []
for n in s:
    r.append(conv(n))
ans = sum(r)

# just do something hacky for now
b5 = []
while ans:
    b5.append(ans % 5)
    ans //= 5

b5.reverse()
while any(n >= 3 for n in b5):
    for i in range(len(b5)):
        if b5[i] >= 3:
            b5[i-1] += 1
            b5[i] -= 5
print("".join(["0","1","2","=","-"][n] for n in b5))
print("click the button")
