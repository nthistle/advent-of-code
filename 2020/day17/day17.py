from collections import defaultdict

with open("input.txt") as f:
    s = f.read().strip("\n")
    
s = s.split("\n")
g = [list(r) for r in s]

adj = [(i,j,k) for i in range(-1,2) for j in range(-1,2) for k in range(-1,2) \
       if (i,j,k) != (0,0,0)]


c = defaultdict(lambda : False)

n = m = 8

for i in range(n):
    for j in range(m):
        c[i,j,0] = ("#" == g[i][j])

def gng(g):
    ng = defaultdict(lambda : False)
    for k in g:
        ng[k] = g[k]
    mini = min(k[0] for k in g)
    maxi = max(k[0] for k in g)
    minj = min(k[1] for k in g)
    maxj = max(k[1] for k in g)
    minz = min(k[2] for k in g)
    maxz = max(k[2] for k in g)
    for i in range(mini-1,maxi+2):
        for j in range(minj-1,maxj+2):
            for z in range(minz-1,maxz+2):
                ac = 0
                for dx,dy,dz in adj:
                    if g[i+dx,j+dy,z+dz]:
                        ac += 1
                if g[i,j,z]:
                    if ac in (2,3):
                        ng[i,j,z] = True
                    else:
                        ng[i,j,z] = False
                else:
                    if ac == 3:
                        ng[i,j,z] = True
                    else:
                        ng[i,j,z] = False
    return ng

for _ in range(6):
    c = gng(c)

print(sum(1 for k in c if c[k]))


adj = [(i,j,k,w) for i in range(-1,2) for j in range(-1,2) for k in range(-1,2) \
       for w in range(-1,2) if (i,j,k,w) != (0,0,0,0)]



c = defaultdict(lambda : False)

n = m = 8

for i in range(n):
    for j in range(m):
        c[i,j,0,0] = ("#" == g[i][j])

def gng(g):
    ng = defaultdict(lambda : False)
    for k in g:
        ng[k] = g[k]
    mini = min(k[0] for k in g if g[k])
    maxi = max(k[0] for k in g if g[k])
    minj = min(k[1] for k in g if g[k])
    maxj = max(k[1] for k in g if g[k])
    minz = min(k[2] for k in g if g[k])
    maxz = max(k[2] for k in g if g[k])
    minw = min(k[3] for k in g if g[k])
    maxw = max(k[3] for k in g if g[k])
    for i in range(mini-1,maxi+2):
        for j in range(minj-1,maxj+2):
            for z in range(minz-1,maxz+2):
                for w in range(minw-1,maxw+2):
                    ac = 0
                    for dx,dy,dz,dw in adj:
                        if g[i+dx,j+dy,z+dz,w+dw]:
                            ac += 1
                    if g[i,j,z,w]:
                        if ac in (2,3):
                            ng[i,j,z,w] = True
                        else:
                            ng[i,j,z,w] = False
                    else:
                        if ac == 3:
                            ng[i,j,z,w] = True
                        else:
                            ng[i,j,z,w] = False
    return ng

for _ in range(6):
    c = gng(c)

print(sum(1 for k in c if c[k]))
