import string
from collections import defaultdict
from aoc_tools import *
import functools
import sys
#sys.setrecursionlimit(10000000)
dirs = ((0,1),(1,0),(0,-1),(-1,0))
dirs3 = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))

with open(r"input.txt") as f:
    s = f.read().strip()
#print("\n".join(x[:60] for x in s.split("\n")[:6]))


x = [y.split(": ") for y in s.split("\n")]
x = [(v,(e if v != "root" else
         e[:5] + "==" + e[6:]
         )) for v,e in x if v != "humn"]

for a,b in x:
    if a=="root":
        print(a,b)

try: raise Exception("hi")
except Exception as e: print(e)

def attempt(humn):
    mx = x.copy()
    root = -100
    while root == -100:
        nx = []
        for v,e in mx:
            try:
                if v != "root":
                    exec(f"{v} = ({e})")
                    #print("SET", v, eval(v))
                else:
                    root = eval(e)
                    #print("SET ROOT", root)
            except:
                nx.append((v,e))
        mx = nx
        try:
            print(rvrh, hzgl)
        except:
            pass
    return eval("rvrh"), eval("hzgl")

##dist = lambda x, y : (x - y) ** 2
##
##cur = 0
##lr = .1
##while True:
##    grad = dist(*attempt(cur + .1)) - dist(*attempt(cur))
##    cur -= lr * grad / .1
##    print(cur)

dist = lambda x, y : abs(x - y)
cur = 0
inc = int(1e12)
while True:
    for _ in range(4):
        if dist(*attempt(cur + inc)) < dist(*attempt(cur)):
            cur += inc
        elif dist(*attempt(cur - inc)) < dist(*attempt(cur)):
            cur -= inc
    inc = int(inc * 0.75)
    print(cur)

vals = {"humn": "x"}
while len(vals) < len(x):
    for v,e in x:
        if v in vals:
            continue
        ne = e
        for m1,m2 in vals.items():
            ne = ne.replace(m1, f"({m2})")
        if "x" in ne:
            vals[v] = ne
        else:
            try:
                vals[v] = eval(ne)
            except:
                pass
    print(len(vals))

print(vals["root"].replace(".0",""))
# now feed into sage
# sage: x = var('x')
# sage: solve((((((92540050790154) - ((9) * ((((((280) + ((((((((2) * ((264) + (((516) + ((((660) + ((2) * (((2) * ((530) + (((((313) + ((((((3) * ((615) + ((((8) * ((915) + (((((246) + ((4) * ((((483) + ((((((((80) + ((((((8) * (((((3) * ((789) + (((107) + (((x) - (745)) / (3))) * (11)))) - (695)) / (4)) - (486))) + (570)) / (5)) - (757)) / (3))) * (5)) + (411)) * (2)) - (885)) + (552)) + (802))) / (2)) - (686)))) / (5)) - (175)) / (3)))) - (66)) / (2)))) - (319)) * (2)) + (133)) + (570))) / (2)) - (955)) / (2)))) - (768)))) / (3)) - (223))) / (5)))) - (933)) / (5)) + (765)) * (9)) - (193)) * (2))) / (2)) + (689)) / (6)) - (230)))) * (2)) + (138)) / (12)) == (5697586809113), x)
# [x == 3453748220116]







































