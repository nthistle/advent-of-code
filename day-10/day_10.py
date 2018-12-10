with open("input.txt") as file:
    inp = file.read().strip()

vals = [(int(line[10:16]),int(line[18:24]),int(line[36:38]),int(line[40:42])) for line in inp.split("\n")]

rough_tx = sum(-x[0]/x[2] for x in vals)/len(vals)
rough_ty = sum(-x[1]/x[3] for x in vals)/len(vals)

def calc_coords(v,t):
    return [(x[0]+t*x[2],x[1]+t*x[3]) for x in v]

rough_t = (rough_tx + rough_ty)/2

dirs = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]

def make_map(c):
    x_min = min(map(lambda x : x[0], c))
    x_max = max(map(lambda x : x[0], c))
    y_min = min(map(lambda x : x[1], c))
    y_max = max(map(lambda x : x[1], c))
    tmap = [[0 for i in range(y_max-y_min+1)] for j in range(x_max-x_min+1)]
    for co in c:
        tmap[co[0]-x_min][co[1]-y_min] += 1
    adj_count = 0
    for co in c:
        aco = (co[0]-x_min,co[1]-y_min)
        for d in dirs:
            aco_d = (aco[0]+d[0],aco[1]+d[1])
            if aco_d[0] >= 0 and aco_d[1] >= 0 and aco_d[0] < len(tmap) and aco_d[1] < len(tmap[aco_d[0]]):
                if tmap[aco_d[0]][aco_d[1]] > 0:
                    adj_count += 1
                    break
    return tmap, adj_count/len(c)

print("Part 1:")
for t in range(int(rough_t-10),int(rough_t+10)):
    mp, frac = make_map(calc_coords(vals, t))
    if frac == 1.0:
        print("\n".join("".join(" " if mp[j][i] == 0 else str(mp[j][i]) for j in range(len(mp))) for i in range(len(mp[0]))))
        print("Part 2:",t)

