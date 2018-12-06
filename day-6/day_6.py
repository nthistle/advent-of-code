with open("input.txt") as file:
    inp = file.read().strip()

coords = [list(map(int, line.split(","))) for line in inp.split("\n")]
coords = list(map(lambda v : (v[0]+25,v[1]+25), coords))

region = [[(800,None) for i in range(400)] for j in range(400)]

valid = set(range(len(coords)))

in_range = lambda c : c[0] in range(400) and c[1] in range(400)

def gen_dist(loc, radius):
    dist = []
    for i in range(0,radius+1):
        dist.append((loc[0]+i,loc[1]+radius-i))
        dist.append((loc[0]-i,loc[1]+radius-i))
        dist.append((loc[0]+i,loc[1]-radius+i))
        dist.append((loc[0]-i,loc[1]-radius+i))
    return [d for d in set(dist) if in_range(d)]
    
for i, co in enumerate(coords):
    print(i)
    for r in range(800):
        for c in gen_dist(co, r):
            if r < region[c[0]][c[1]][0]:
                region[c[0]][c[1]] = (r, i)
            elif r == region[c[0]][c[1]][0]:
                region[c[0]][c[1]] = (r, None)

for i in range(400):
    print(i)
    if region[i][0][1] in valid:
        valid.remove(region[i][0][1])
    if region[i][399][1] in valid:
        valid.remove(region[i][399][1])
    if region[0][i][1] in valid:
        valid.remove(region[0][i][1])
    if region[399][i][1] in valid:
        valid.remove(region[399][i][1])

counters = {v:0 for v in valid}

for i in range(400):
    print(i)
    for j in range(400):
        if region[i][j][1] in counters:
            counters[region[i][j][1]] += 1

print("Part 1:",max(counters.values()))

region = [[0 for i in range(400)] for j in range(400)]

for i, co in enumerate(coords):
    print(i)
    for r in range(800):
        for c in gen_dist(co, r):
            region[c[0]][c[1]] += r

print("Part 2:",sum(sum(v < 10000 for v in line) for line in region))
