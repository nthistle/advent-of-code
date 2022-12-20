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

PART = 1

ans = 0 if PART == 1 else 1
for rnum,r in (all_r if PART == 1 else all_r[:3]):
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

    ore_recipe = r[0][1][0][0] # ore to build an ore bot
    clay_recipe = r[1][1][0][0]  # ore to build a clay bot
    obs_recipe1 = r[2][1][0][0] # ore to build obs
    obs_recipe2 = r[2][1][1][0] # clay to build obs
    geo_recipe1 = r[3][1][0][0] # ore to build geo
    geo_recipe2 = r[3][1][1][0] # clay to build geo

    
    cache = {}
    def solve(n_ore, n_clay, n_obs, r_ore, r_clay, r_obs, r_geo, t_left):
        if (n_ore, n_clay, n_obs, r_ore, r_clay, r_obs, r_geo, t_left) not in cache:
            nn_ore = n_ore + r_ore
            nn_clay = n_clay + r_clay
            nn_obs = n_obs + r_obs
            
            geo_max = 0

            if t_left == 1:
                return r_geo

            # never makes sense to have more ore robots than ore we can spend in a turn
            if r_ore > ore_recipe and r_ore > clay_recipe and r_ore > obs_recipe1 and \
               r_ore > geo_recipe1:
                return 0

            if t_left == 12:
                if any(n_ore <= n_ore2 and n_clay <= n_clay2 and n_obs <= n_obs2 and
                   r_ore <= r_ore2 and r_clay <= r_clay2 and r_obs <= r_obs2 and
                   r_geo <= r_geo2 for (n_ore2, n_clay2, n_obs2, r_ore2, r_clay2, r_obs2, r_geo2) in
                   dominated_on_12):
                    #print("pruned")
                    return 0
                else:
                    dominated_on_12.append((n_ore, n_clay, n_obs, r_ore, r_clay, r_obs, r_geo))
            
            #if r_clay == 0 and  >= ore_recipe and n_ore >= clay_recipe:
            #    return 0
            #if r_obs == 0 and n_ore >= ore_recipe and n_ore >= clay_recipe and \
            #   n_ore >= obs_recipe1 and n_clay >= obs_recipe2:
            #    return 0

            # build ore bot?
            can_build_ore = False
            can_build_clay = False
            can_build_obs = False
            can_build_geo = False
            
            if n_ore >= ore_recipe:
                can_build_ore = True
                geo_max = max(geo_max, solve(
                    nn_ore - ore_recipe, nn_clay, nn_obs,
                    r_ore + 1, r_clay, r_obs, r_geo,
                    t_left - 1))

            if n_ore >= clay_recipe:
                can_build_clay = True
                geo_max = max(geo_max, solve(
                    nn_ore - clay_recipe, nn_clay, nn_obs,
                    r_ore, r_clay + 1, r_obs, r_geo,
                    t_left - 1))

            if n_ore >= obs_recipe1 and n_clay >= obs_recipe2:
                can_build_obs = True
                geo_max = max(geo_max, solve(
                    nn_ore - obs_recipe1, nn_clay - obs_recipe2, nn_obs,
                    r_ore, r_clay, r_obs + 1, r_geo,
                    t_left - 1))

            if n_ore >= geo_recipe1 and n_obs >= geo_recipe2:
                can_build_geo = True
                geo_max = max(geo_max, solve(
                    nn_ore - geo_recipe1, nn_clay, nn_obs - geo_recipe2,
                    r_ore, r_clay, r_obs, r_geo + 1,
                    t_left - 1))

            consider = True
            if r_clay == 0 and can_build_ore and can_build_clay:
                consider = False
            if r_obs == 0 and can_build_ore and can_build_clay and can_build_obs:
                consider = False
            if can_build_ore and can_build_clay and can_build_obs and can_build_geo:
                consider = False

            if consider:
                geo_max = max(geo_max, solve(
                    nn_ore, nn_clay, nn_obs,
                    r_ore, r_clay, r_obs, r_geo,
                    t_left - 1))
            
            cache[(n_ore, n_clay, n_obs, r_ore, r_clay, r_obs, r_geo, t_left)] = geo_max + r_geo
        return cache[(n_ore, n_clay, n_obs, r_ore, r_clay, r_obs, r_geo, t_left)]

    import time
    st = time.time()
    result = solve(0,0,0,1,0,0,0,(24 if PART == 1 else 32))
    print("max geodes is", result)
    if PART == 1:
        ans += rnum * result
    else:
        ans *= result
    #print(solve((ore_cnt,0,0),(ore_rbt,0,0,0), 24 - ONLY_ORE))
    et = time.time()
    print(f"took {et - st:.2f}s")
    del solve
    del dominated_on_12
    del cache

print(ans)














































