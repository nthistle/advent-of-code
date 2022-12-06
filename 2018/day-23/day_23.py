with open("input.txt") as file:
    inp = file.read().strip()

bots = inp.split("\n")
bots = [(eval("["+b[1+b.find("<"):b.rfind(">")]+"]"),int(b[b.rfind("=")+1:])) for b in bots]
s = max(bots, key=lambda v : v[1])
cnt = 0
for b in bots:
    dist = abs(b[0][0]-s[0][0])+abs(b[0][1]-s[0][1])+abs(b[0][2]-s[0][2])
    if dist <= s[1]:
        cnt += 1
        
print("Part 1:",cnt)

from z3 import *

x,y,z = Int('x'),Int('y'),Int('z')
in_ranges = []
Abs = lambda c : If(c > 0, c, -c)
for bot in bots:
    in_ranges.append(If( (Abs(x - bot[0][0]) + Abs(y-bot[0][1])
                          + Abs(z-bot[0][2])) <= bot[1], 1, 0 ))
    
opt = Optimize()
v1 = opt.maximize(Sum(*in_ranges))
v2 = opt.minimize(Abs(x)+Abs(y)+Abs(z))
opt.check()

print("Part 2:",v2.value())
