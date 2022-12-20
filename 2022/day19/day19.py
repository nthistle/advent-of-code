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
print("\n".join(x[:60] for x in s.split("\n")[:6]))

s = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""


mp = {"ore":0,"clay":1,"obsidian":2}
all_r = []
for jj,l in enumerate(s.split("\n")):
    r = l.split(": ")[1]
    r = r.strip(".").split(". ")
    r = [x[5:] for x in r]
    r = [x.split(" costs ") for x in r]
    r = [(rt, tuple((int(n), mp[t]) for it in recipe.split(" and ")
                    for n,t in [it.split(" ")]
                    )) for rt,recipe in r]
    all_r.append((jj + 1, r))

all_pruned_r = []
for i,(idx,r1) in enumerate(all_r):
    dominates = True
    for _,r2 in all_r[i+1:]:
        # check if r2 dominates r1
        for (_, rec1), (_, rec2) in zip(r1,r2):
            if any(qty1 < qty2 for (_,qty1),(_,qty2) in zip(rec1,rec2)):
                dominates = False
                break
    if not dominates:
        print(f"{i} is dominated!")
    else:
        all_pruned_r.append((idx,r1))

for rnum,r in all_pruned_r:
    print("checking bot", rnum)
    print(r)
    
    # dp[#ore,#clay,#obs,#geo,t] = max value we can get

    rlimits = [0,0,0]
    for _, recipe in r:
        for qty,typ in recipe:
            rlimits[typ] = max(rlimits[typ],qty)

    global bbv
    bbv = 0

    dominated_on_12 = []
    dominated_on_14 = []
    
    @functools.lru_cache(maxsize=None)
    def solve(resources, robots, t_left):
        global bbv

        if t_left == 12:
            for dresources, drobots in dominated_on_12:
                if all(dresources[i] >= resources[i] for i in range(3)) and (
                    all(drobots[i] >= robots[i] for i in range(4))):
                    print("PRUNED12!")
                    return 0
            dominated_on_12.append((resources, robots))

        if t_left == 14:
            for dresources, drobots in dominated_on_14:
                if all(dresources[i] >= resources[i] for i in range(3)) and (
                    all(drobots[i] >= robots[i] for i in range(4))):
                    print("PRUNED14!")
                    return 0
            dominated_on_14.append((resources, robots))
        
        if t_left >= 12:
            print(t_left, resources, robots)
        #global d
        #d += 1
        #if d % 10000 == 0:
        #    print(resources, robots, t_left,cb)
        # resources is 3-tuple
        # robots is 4-tuple
        new_resources = list(resources)

        bv = 0

        # if at this point, we can build 1 of every robot, we made a mistake
        if robots[1] == 0:
            # if we haven't built a clay, and we have at least enough ore to
            # build a clay or ore bot, just do it
            if resources[0] >= rlimits[0]:
                return 0
        elif robots[2] == 0:
            # if we haven't built an obsidian, and have enough to build
            if resources[0] >= rlimits[0] and resources[1] > rlimits[1]:
                return 0
        elif all(resources[i] >= rlimits[i] for i in range(3)):
            return 0
        
        v = 0
        for i in range(3):
            new_resources[i] += robots[i]
        v += robots[3]

        if t_left == 1:
            return v
        
##        max_builds = [
##            min(resources[typ]//qty for qty,typ in r[j][1])
##            for j in range(4)
##        ]

        for i in range(4):
            # can we build robot of type i?
            if all(resources[typ] >= qty for qty,typ in r[i][1]):
                # try building robot of type i?
                new_new_resources = new_resources.copy()
                
        

##        for built_num2 in range(max_builds[-1],-1,-1):
##            for built_num in itertools.product(*[range(max_build,-1,-1) for max_build in
##                                                 max_builds[:3]]):
##                built_num = built_num + (built_num2,)
##                new_new_resources = new_resources.copy()
##                for i in range(4):
##                    for qty, typ in r[i][1]:
##                        new_new_resources[typ] -= qty * built_num[i]
##                if min(new_new_resources) < 0:
##                    continue
##                
##                new_robots = list(robots)
##                for i in range(4):
##                    new_robots[i] += built_num[i]
##                bv = max(bv, v + solve(tuple(new_new_resources),
##                                       tuple(new_robots),
##                                       t_left - 1))
        if bv > bbv:
            print("MAX:",bv)
            bbv = bv
        return bv

##    ONLY_ORE = 6
##    ore_cnt = 0
##    ore_rbt = 1
##    for i in range(ONLY_ORE):
##        n = 0
##        if ore_cnt >= r[0][1][0][0]:
##            n += ore_cnt // r[0][1][0][0]
##            ore_cnt -= n * r[0][1][0][0]
##        ore_cnt += ore_rbt
##        ore_rbt += n
##    print(ore_cnt, ore_rbt)

    import time
    st = time.time()
    print(solve((0,0,0),(1,0,0,0),24))
    #print(solve((ore_cnt,0,0),(ore_rbt,0,0,0), 24 - ONLY_ORE))
    et = time.time()
    print(et - st)
    break

















































