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

s = s.split("\n")

inits = []
particles = []

for l in s:
    p = tuple(nums(l))
    inits.append(p)
    particles.append(p)

for _ in range(1000):
    np = []
    for p in particles:
        x,y,z,vx,vy,vz,ax,ay,az = p
        vx += ax
        vy += ay
        vz += az
        x += vx
        y += vy
        z += vz
        np.append((x,y,z,vx,vy,vz,ax,ay,az))
    particles = np

print(min(range(len(particles)), key = lambda i : sum(abs(particles[i][j]) for j in range(3))))

particles = inits

for _ in range(1000):
    np = []
    col = defaultdict(lambda : 0)
    for p in particles:
        x,y,z,vx,vy,vz,ax,ay,az = p
        vx += ax
        vy += ay
        vz += az
        x += vx
        y += vy
        z += vz
        np.append((x,y,z,vx,vy,vz,ax,ay,az))
        col[x,y,z] += 1
    nnp = []
    for p in np:
        x,y,z,_,_,_,_,_,_ = p
        if col[x,y,z] == 1:
            nnp.append(p)
    particles = nnp

print(len(particles))
