import string
from collections import defaultdict
from aoc_tools import *
import functools
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

with open(r"input.txt") as f:
    s = f.read().strip()
print("\n".join(x[:60] for x in s.split("\n")[:6]))

g = {}
f = {}
for line in s.split("\n"):
    valve = line[6:8]
    flow = nums(line)[0]
    _, r = line.split(";")
    r = r.replace("valves","valve")[len(" tunnels lead to valve "):]
    g[valve] = r.split(", ")
    f[valve] = flow

cur = "AA"

@functools.lru_cache(maxsize=None)
def maxflow(cur, opened, min_left):
    if min_left <= 0:
        return 0
    best = 0
    if cur not in opened:
        val = (min_left - 1) * f[cur]
        cur_opened = tuple(sorted(opened + (cur,)))
        for adj in g[cur]:
            if val != 0:
                best = max(best,
                    val + maxflow(adj, cur_opened, min_left - 2))
            best = max(best,
                maxflow(adj, opened, min_left - 1))
    return best

print(maxflow("AA", (), 30))



# -> (largest_min_left, result)
##cache = {}
##def maxflow2(cur, cur2, opened, min_left):
##    if min_left <= 0:
##        return 0
##    if (cur, cur2, opened) not in cache or min_left > cache[cur, cur2, opened][0]:
##        if min_left >= 13:
##            print(min_left)
##        best = 0
##        # open,open
##        # move,open
##        # open,move
##        # move,move
##        
##        if cur not in opened and f[cur] > 0:
##            if cur2 not in opened and f[cur2] > 0:
##                # consider open,open
##                val = (min_left - 1) * (f[cur] + f[cur2])
##                new_opened = tuple(sorted(opened + (cur, cur2)))
##                best = max(best, val + maxflow2(cur, cur2, new_opened, min_left - 1))
##            
##            # consider open,move
##            val = (min_left - 1) * f[cur]
##            new_opened = tuple(sorted(opened + (cur,)))
##            for adj in g[cur2]:
##                best = max(best, val + maxflow2(cur, adj, new_opened, min_left - 1))
##
##        if cur2 not in opened and f[cur2] > 0:
##            # consider move,open
##            val = (min_left - 1) * f[cur2]
##            new_opened = tuple(sorted(opened + (cur2,)))
##            for adj in g[cur]:
##                best = max(best, val + maxflow2(adj, cur2, new_opened, min_left - 1))
##
##        # consider move,move
##        for adj1 in g[cur]:
##            for adj2 in g[cur2]:
##                best = max(best, maxflow2(adj1, adj2, opened, min_left - 1))
##        
##        cache[cur, cur2, opened] = (min_left, best)
##    return cache[cur, cur2, opened][1]
##
###print(maxflow("AA", (), 30))
##print(maxflow2("AA", "AA", (), 26))


dist2 = {('OT', 'IS'): 10, ('OT', 'WI'): 7, ('OT', 'QQ'): 7, ('OT', 'ZL'): 4, ('OT', 'OM'): 4, ('OT', 'NG'): 7, ('OT', 'AA'): 3, ('OT', 'YW'): 2, ('OT', 'DG'): 10, ('OT', 'MX'): 5, ('OT', 'HV'): 2, ('OT', 'GB'): 2, ('OT', 'IC'): 2, ('OT', 'VX'): 7, ('OT', 'FM'): 10, ('IS', 'OT'): 10, ('IS', 'WI'): 9, ('IS', 'QQ'): 3, ('IS', 'ZL'): 6, ('IS', 'OM'): 6, ('IS', 'NG'): 3, ('IS', 'AA'): 10, ('IS', 'YW'): 8, ('IS', 'DG'): 2, ('IS', 'MX'): 5, ('IS', 'HV'): 8, ('IS', 'GB'): 10, ('IS', 'IC'): 8, ('IS', 'VX'): 9, ('IS', 'FM'): 6, ('WI', 'OT'): 7, ('WI', 'IS'): 9, ('WI', 'QQ'): 12, ('WI', 'ZL'): 3, ('WI', 'OM'): 6, ('WI', 'NG'): 6, ('WI', 'AA'): 7, ('WI', 'YW'): 5, ('WI', 'DG'): 11, ('WI', 'MX'): 10, ('WI', 'HV'): 7, ('WI', 'GB'): 7, ('WI', 'IC'): 5, ('WI', 'VX'): 3, ('WI', 'FM'): 15, ('QQ', 'OT'): 7, ('QQ', 'IS'): 3, ('QQ', 'WI'): 12, ('QQ', 'ZL'): 9, ('QQ', 'OM'): 9, ('QQ', 'NG'): 6, ('QQ', 'AA'): 8, ('QQ', 'YW'): 9, ('QQ', 'DG'): 3, ('QQ', 'MX'): 2, ('QQ', 'HV'): 5, ('QQ', 'GB'): 7, ('QQ', 'IC'): 7, ('QQ', 'VX'): 12, ('QQ', 'FM'): 3, ('ZL', 'OT'): 4, ('ZL', 'IS'): 6, ('ZL', 'WI'): 3, ('ZL', 'QQ'): 9, ('ZL', 'OM'): 3, ('ZL', 'NG'): 3, ('ZL', 'AA'): 4, ('ZL', 'YW'): 2, ('ZL', 'DG'): 8, ('ZL', 'MX'): 7, ('ZL', 'HV'): 4, ('ZL', 'GB'): 4, ('ZL', 'IC'): 2, ('ZL', 'VX'): 6, ('ZL', 'FM'): 12, ('OM', 'OT'): 4, ('OM', 'IS'): 6, ('OM', 'WI'): 6, ('OM', 'QQ'): 9, ('OM', 'ZL'): 3, ('OM', 'NG'): 3, ('OM', 'AA'): 5, ('OM', 'YW'): 2, ('OM', 'DG'): 8, ('OM', 'MX'): 9, ('OM', 'HV'): 6, ('OM', 'GB'): 4, ('OM', 'IC'): 5, ('OM', 'VX'): 3, ('OM', 'FM'): 12, ('NG', 'OT'): 7, ('NG', 'IS'): 3, ('NG', 'WI'): 6, ('NG', 'QQ'): 6, ('NG', 'ZL'): 3, ('NG', 'OM'): 3, ('NG', 'AA'): 7, ('NG', 'YW'): 5, ('NG', 'DG'): 5, ('NG', 'MX'): 8, ('NG', 'HV'): 7, ('NG', 'GB'): 7, ('NG', 'IC'): 5, ('NG', 'VX'): 6, ('NG', 'FM'): 9, ('AA', 'OT'): 3, ('AA', 'IS'): 10, ('AA', 'WI'): 7, ('AA', 'QQ'): 8, ('AA', 'ZL'): 4, ('AA', 'OM'): 5, ('AA', 'NG'): 7, ('AA', 'YW'): 3, ('AA', 'DG'): 11, ('AA', 'MX'): 6, ('AA', 'HV'): 3, ('AA', 'GB'): 3, ('AA', 'IC'): 2, ('AA', 'VX'): 8, ('AA', 'FM'): 11, ('YW', 'OT'): 2, ('YW', 'IS'): 8, ('YW', 'WI'): 5, ('YW', 'QQ'): 9, ('YW', 'ZL'): 2, ('YW', 'OM'): 2, ('YW', 'NG'): 5, ('YW', 'AA'): 3, ('YW', 'DG'): 10, ('YW', 'MX'): 7, ('YW', 'HV'): 4, ('YW', 'GB'): 2, ('YW', 'IC'): 4, ('YW', 'VX'): 5, ('YW', 'FM'): 12, ('DG', 'OT'): 10, ('DG', 'IS'): 2, ('DG', 'WI'): 11, ('DG', 'QQ'): 3, ('DG', 'ZL'): 8, ('DG', 'OM'): 8, ('DG', 'NG'): 5, ('DG', 'AA'): 11, ('DG', 'YW'): 10, ('DG', 'MX'): 5, ('DG', 'HV'): 8, ('DG', 'GB'): 10, ('DG', 'IC'): 10, ('DG', 'VX'): 11, ('DG', 'FM'): 6, ('MX', 'OT'): 5, ('MX', 'IS'): 5, ('MX', 'WI'): 10, ('MX', 'QQ'): 2, ('MX', 'ZL'): 7, ('MX', 'OM'): 9, ('MX', 'NG'): 8, ('MX', 'AA'): 6, ('MX', 'YW'): 7, ('MX', 'DG'): 5, ('MX', 'HV'): 3, ('MX', 'GB'): 5, ('MX', 'IC'): 5, ('MX', 'VX'): 12, ('MX', 'FM'): 5, ('HV', 'OT'): 2, ('HV', 'IS'): 8, ('HV', 'WI'): 7, ('HV', 'QQ'): 5, ('HV', 'ZL'): 4, ('HV', 'OM'): 6, ('HV', 'NG'): 7, ('HV', 'AA'): 3, ('HV', 'YW'): 4, ('HV', 'DG'): 8, ('HV', 'MX'): 3, ('HV', 'GB'): 2, ('HV', 'IC'): 2, ('HV', 'VX'): 9, ('HV', 'FM'): 8, ('GB', 'OT'): 2, ('GB', 'IS'): 10, ('GB', 'WI'): 7, ('GB', 'QQ'): 7, ('GB', 'ZL'): 4, ('GB', 'OM'): 4, ('GB', 'NG'): 7, ('GB', 'AA'): 3, ('GB', 'YW'): 2, ('GB', 'DG'): 10, ('GB', 'MX'): 5, ('GB', 'HV'): 2, ('GB', 'IC'): 2, ('GB', 'VX'): 7, ('GB', 'FM'): 10, ('IC', 'OT'): 2, ('IC', 'IS'): 8, ('IC', 'WI'): 5, ('IC', 'QQ'): 7, ('IC', 'ZL'): 2, ('IC', 'OM'): 5, ('IC', 'NG'): 5, ('IC', 'AA'): 2, ('IC', 'YW'): 4, ('IC', 'DG'): 10, ('IC', 'MX'): 5, ('IC', 'HV'): 2, ('IC', 'GB'): 2, ('IC', 'VX'): 8, ('IC', 'FM'): 10, ('VX', 'OT'): 7, ('VX', 'IS'): 9, ('VX', 'WI'): 3, ('VX', 'QQ'): 12, ('VX', 'ZL'): 6, ('VX', 'OM'): 3, ('VX', 'NG'): 6, ('VX', 'AA'): 8, ('VX', 'YW'): 5, ('VX', 'DG'): 11, ('VX', 'MX'): 12, ('VX', 'HV'): 9, ('VX', 'GB'): 7, ('VX', 'IC'): 8, ('VX', 'FM'): 15, ('FM', 'OT'): 10, ('FM', 'IS'): 6, ('FM', 'WI'): 15, ('FM', 'QQ'): 3, ('FM', 'ZL'): 12, ('FM', 'OM'): 12, ('FM', 'NG'): 9, ('FM', 'AA'): 11, ('FM', 'YW'): 12, ('FM', 'DG'): 6, ('FM', 'MX'): 5, ('FM', 'HV'): 8, ('FM', 'GB'): 10, ('FM', 'IC'): 10, ('FM', 'VX'): 15}

g2 = defaultdict(list)

keep = ['OT', 'IS', 'WI', 'QQ', 'ZL', 'OM', 'NG', 'AA', 'YW', 'DG', 'MX', 'HV', 'GB', 'IC', 'VX', 'FM']

for x in keep:
    for y in keep:
            if x == y: continue
            g2[x].append((dist2[x,y], y))

# dp/memo
# (our_loc, our_time_left, ele_loc, ele_time_left, opened_valves)

def add(open_valves, new_valve):
    return tuple(sorted(open_valves + (new_valve,)))

# no work :-(
##@functools.lru_cache(maxsize=None)
##def solve2(our_loc, our_time_left, ele_loc, ele_time_left, open_valves):
##    if our_time_left + ele_time_left > 30:
##        print(our_time_left, ele_time_left)
##    # us move, us open, ele move, ele open
##    best = 0
##    
##    for cost,adj in g2[our_loc]:
##        if our_time_left >= cost + 2: # BAD HEURISTIC
##            best = max(best, solve2(adj, our_time_left - cost,
##                                    ele_loc, ele_time_left, open_valves))
##
##    if our_time_left >= 2 and our_loc not in open_valves:
##        best = max(best, (our_time_left - 1) * f[our_loc] + solve2(
##            our_loc, our_time_left - 1, ele_loc, ele_time_left, add(open_valves, our_loc)
##            ))
##        
##    for cost,adj in g2[ele_loc]:
##        if ele_time_left >= cost + 2: # BAD HEURISTIC
##            best = max(best, solve2(our_loc, our_time_left,
##                                    adj, ele_time_left - cost, open_valves))
##
##    if ele_time_left >= 2 and ele_loc not in open_valves:
##        best = max(best, (ele_time_left - 1) * f[ele_loc] + solve2(
##            our_loc, our_time_left, ele_loc, ele_time_left - 1, add(open_valves, ele_loc)
##            ))
##        
##    return best

for cost,adj in sorted(g2["AA"]):
    print(cost,adj,f[adj])

# paths where we activate each stop
def get_paths(loc, budget, exclude=None):
    if exclude is None: exclude = set()
    if budget >= 1:
        yield (loc,)
    for cost, adj in g2[loc]:
        if adj in exclude: continue
        if budget >= cost + 2:
            for path in get_paths(adj, budget - cost - 1, exclude | {loc}):
                yield (loc,) + path

@functools.lru_cache(maxsize=None)
def value(path, time):
    result = 0
    for a,b in zip(path, path[1:]):
        # walk from a to b
        # open valve b
        time -= dist2[a,b]
        time -= 1
        result += time * f[b]
    return result#, time

# alternate part 1:
# print(max(value(path, 30) for path in get_paths("AA", 30)))

best_value = 0
ctr = 0
for i,path1 in enumerate(get_paths("AA", 26, set())):
    if i % 100 == 0:
        print(i)
    p1v = value(path1, 26)
    for path2 in get_paths("AA", 26, exclude=set(path1)):
        ctr += 1
        p2v = value(path2, 26)
        best_value = max(best_value, p1v + p2v)
print(ctr)
print(best_value)
