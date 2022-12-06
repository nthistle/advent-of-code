##from collections import defaultdict
##import functools
##import regex
##import heapq
##
##nums_regex = regex.compile("^([^\\d]*?)((?P<nums>\\-?\\d+)([^\\d]*?))*$")
##
### N,E,S,W
##dirs = [(0,1),(1,0),(0,-1),(-1,0)]
##
##def nums(s):
##    m = nums_regex.match(s)
##    vals = m.capturesdict()["nums"]
##    return [int(x) for x in vals]

with open("input.txt") as f:
    s = f.read().strip("\n")

s = s.split("\n\n")
p1 = s[0].split("\n")[1:]
p2 = s[1].split("\n")[1:]
p1 = list(map(int,p1))
p2 = list(map(int,p2))

while len(p1)>0 and len(p2)>0:
    p1a = p1.pop(0)
    p2a = p2.pop(0)
    if p1a > p2a:
        p1.extend([p1a,p2a])
    else:
        p2.extend([p2a,p1a])

print(sum((i+1)*v for i,v in enumerate(p1[::-1])))

p1 = s[0].split("\n")[1:]
p2 = s[1].split("\n")[1:]
p1 = list(map(int,p1))
p2 = list(map(int,p2))

# p1 win = True
def combat(p1,p2):
    seen = set()
    while len(p1)>0 and len(p2)>0:
        if (tuple(p1),tuple(p2)) in seen:
            return True
        seen.add((tuple(p1),tuple(p2)))
        p1a = p1.pop(0)
        p2a = p2.pop(0)
        if len(p1) >= p1a and len(p2) >= p2a:
            winner = combat(p1[:p1a], p2[:p2a])
            if winner:
                p1.extend([p1a,p2a])
            else:
                p2.extend([p2a,p1a])
        else:
            if p1a > p2a:
                p1.extend([p1a,p2a])
            else:
                p2.extend([p2a,p1a])
    return len(p1)>0

combat(p1,p2)
print(sum((i+1)*v for i,v in enumerate(p1[::-1])))

