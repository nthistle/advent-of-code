from collections import defaultdict, Counter
import regex
import itertools

nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    s = f.read().strip()

tx1, tx2 = 244, 303
ty1, ty2 = -91, -54

def sim(vx,vy):
    cx,cy = 0,0
    hy = 0
    while cy > -100:
        #print(cx,cy)
        cx += vx
        cy += vy
        vx = max(vx - 1, 0)
        hy = max(hy, cy)
        vy -= 1
        if 244 <= cx <= 303 and -91 <= cy <= -54:
            return hy
    return -1

