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
#with open("ex.txt") as f:
    s = f.read().strip("\n")

s = s.split("\n\n")

## ORIENTATION = number on top
#  = number of counterclockwise rotations

# TOP
##0 -> 2
##1 -> 1
##2 -> 0
##3 -> 3

#      0
#    3   1
#      2

# 3 dir   (-1 % 4)
# 0 -> 3
# 1 -> 0
# 2 -> 1

# 0 dir   (+2 % 4)
# 2 -> 0
# 1 -> 3
# 3 -> 1

# 1 dir   (+1 % 4)
# 3 -> 0

# 2 dir   (=)
# 0 -> 0


# RIGHT
# 3 -> 0
# 0 -> 3
# 1 -> 2
# 2 -> 1
# {3:0,0:3,1:2,2:1}


#      3
#        0
#      1


def flip(g):
    return [r[::-1] for r in g]

def rot(g):    
    n = len(g)
    m = len(g[0])
    out = [[] for _ in range(m)]
    for i in range(len(g)):
        for j in range(len(g[0])-1,-1,-1):
            out[len(g[0]) - j - 1].append(g[i][j])
    return out

def edges(g):
    top = "".join(g[0])
    bot = ("".join(g[-1]))[::-1]
    lef = ("".join(g[i][0] for i in range(len(g))))[::-1]
    rig = "".join(g[i][-1] for i in range(len(g)))
    return top,rig,bot,lef

def order(e):
    return e if e > e[::-1] else e[::-1]

es = set()

tiles = {}
edge_lookup = defaultdict(list)
for b in s:
    lns = b.split("\n")
    n,g = lns[0],lns[1:]
    n = nums(n)[0]
    g = [list(r) for r in g]
    tiles[n] = g
    for j,edg in enumerate(edges(g)):
        edge_lookup[edg].append((n,j))

flipped = defaultdict(lambda : False)

##def dfs(cur,seen):
##    if cur in seen:
##        return
##    seen.add(cur)
##    g = tiles[cur]
##    adj = []
##    for edge in edges(g):
##        if len(edge_lookup[edge]) == 1:
##            if len(edge_lookup[edge[::-1]]) == 0:
##                continue
##            an,aj = edge_lookup[edge[::-1]][0]
##            old_g = tiles[an]
##            tiles[an] = flip(tiles[an])
##            for j,(old_edge,new_edge) in enumerate(zip(edges(old_g), edges(tiles[an]))):
##                edge_lookup[old_edge].remove((an,j))
##                edge_lookup[new_edge].append((an,j))
##            adj.append(an)
##            flipped[an] = True
##        else:
##            an,aj = [(n,j) for n,j in edge_lookup[edge] if n != cur][0]
##            adj.append(an)
##    for an in adj:
##        dfs(an,seen)

def dfs(cur,seen):
    if cur in seen:
        return
    seen.add(cur)
    g = tiles[cur]
    adj = []
    for edge in edges(g):
        if len(edge_lookup[edge]) == 1:
            if len(edge_lookup[edge[::-1]]) == 0:
                continue
            an,aj = edge_lookup[edge[::-1]][0]
            adj.append(an)
        else:
            an,aj = [(n,j) for n,j in edge_lookup[edge] if n != cur][0]
            old_g = tiles[an]
            tiles[an] = flip(tiles[an])
            for j,(old_edge,new_edge) in enumerate(zip(edges(old_g), edges(tiles[an]))):
                edge_lookup[old_edge].remove((an,j))
                edge_lookup[new_edge].append((an,j))
            adj.append(an)
            flipped[an] = True
    for an in adj:
        dfs(an,seen)

#k = 3851#next(iter(tiles))

k = 1951

seen = set()
dfs(k,seen)

prod = 1
for t in tiles:
    if sum(1 for edge in edges(tiles[t]) if len(edge_lookup[edge]+edge_lookup[edge[::-1]])==1)==2:
        prod *= t
print(prod)

#x,y,o,flipped

# o is the direction top is facing
m = {k:(0,0,0)}
used = {k}
locs = {(0,0)}


el = edge_lookup

dxdy = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}

itc = 0
while len(used)<len(tiles):
    for k in list(used):
        x,y,o = m[k]
        for j,edge in enumerate(edges(tiles[k])):
            j = (j - o) % 4
            nedges = [(n,j) for n,j in edge_lookup[edge[::-1]]]
            if len(nedges) > 0:
                mn,mo = nedges[0]
                # have a match in this direction
                dx,dy = dxdy[j]
                nx,ny = x+dx,y+dy
                if j == 0:
                    no = (mo + 2) % 4
                elif j == 1:
                    no = (mo + 1) % 4
                elif j == 2:
                    no = mo
                else:
                    no = (mo + 3) % 4
                    
                used.add(mn)
                locs.add((nx,ny))
                m[mn] = (nx,ny,no)

final = defaultdict(lambda : ' ')
for n in m:
    x,y,o = m[n]
    rx,ry = 8*x,8*y
    g = tiles[n]
    for _ in range(o):
        g = rot(g)
    for i in range(8):
        for j in range(8):
            final[rx+j,ry-i] = g[1+i][1+j]

minx,miny = min(final)
maxx,maxy = max(final)

im = [[final[i,j] for j in range(miny,maxy+1)] for i in range(minx,maxx+1)]

pattern = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
pattern = [list(r) for r in pattern.split("\n")]

used = [[False for _ in range(len(r))] for r in im]

for n_rot in range(4):
    for do_flip in (True,False):

        res = [r[:] for r in im]
        if do_flip:
            res = flip(res)
        for _ in range(n_rot):
            res = rot(res)

        this_used = [[False for _ in range(len(r))] for r in res]

        for i in range(len(res)-3+1):
            for j in range(len(res[0])-20+1):
                if all((pattern[k][l] == ' ' or pattern[k][l] == res[i+k][j+l]) \
                       for k in range(3) for l in range(20)):
                    for k in range(3):
                        for l in range(20):
                            if pattern[k][l] == '#':
                                this_used[i+k][j+l] = True

        for _ in range(4 - n_rot):
            this_used = rot(this_used)
        if do_flip:
            this_used = flip(this_used)

        for i in range(len(used)):
            for j in range(len(used[i])):
                used[i][j] = used[i][j] or this_used[i][j]

print(sum(1 for i in range(len(im)) for j in range(len(im[i])) if im[i][j] == '#' and not used[i][j]))



