with open("input.txt") as f:
    s = f.read().strip().split(",")

coords = [0,0,0]

lookup = {
    "n"  : (0,1),
    "s"  : (0,-1),
    "ne" : (1,1),
    "sw" : (1,-1),
    "se" : (2,1),
    "nw" : (2,-1)
    }

dist = lambda c : sum(abs(ci) for ci in c)

def rule1(coords, freq):
    coords[0] -= freq
    coords[2] -= freq
    coords[1] += freq

def rule2(coords, freq):
    coords[0] -= freq
    coords[1] += freq
    coords[2] -= freq

def true_dist(coords):
    rule1(coords, coords[0])
    min_dist = dist(coords)
    rule1(coords, coords[2])
    min_dist = min(min_dist, dist(coords))
    rule2(coords, -coords[1])
    return min(min_dist, dist(coords))

furthest = 0
for d in s:
    i,v = lookup[d]
    coords[i] += v
    furthest = max(furthest, true_dist(coords))

print(true_dist(coords))
print(furthest)
