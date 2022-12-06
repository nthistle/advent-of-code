import queue

with open("input.txt") as file:
    inp = file.read().strip()

mat = [[[c] for c in line] for line in inp.split("\n")]
mat_copy = lambda : [[a.copy() for a in b] for b in mat]

for x, line in enumerate(mat):
    for y, c in enumerate(line):
        if c[0] in "EG":
            c.extend([x,y,200,0])

def simulate_combat(mat, elf_sc=False, elf_power=3):
    alive_units = [x for line in mat for x in line if x[0] in "EG"]
    dirs = [(-1,0),(0,-1),(0,1),(1,0)] # in reading order

    rd = 0
    combat_done = False
    while not combat_done:
        alive_units.sort(key = lambda u : 10000 * u[1] + u[2])
        for unit in alive_units[:]:
            if unit not in alive_units:
                # Omae wa mou shindeiru
                continue
            
            ## List of target enemies
            targets = [u for u in alive_units if u[0] != unit[0]]
            target_locs = {(u[1],u[2]):u for u in targets}

            ## Check whether combat has ended
            if len(targets) == 0:
                combat_done = True
                break
            
            ## First check for adjacent enemies
            target_enemy = None
            for d in dirs:
                if (unit[1]+d[0],unit[2]+d[1]) in target_locs:
                    target_enemy = target_locs[(unit[1]+d[0],unit[2]+d[1])]

            if target_enemy == None:
                ## We're going to have to do movement
                in_range = {}
                for t in targets:
                    for d in dirs:
                        if mat[t[1]+d[0]][t[2]+d[1]] == ["."]:
                            in_range[(t[1]+d[0],t[2]+d[1])] = t

                best_step = None
                ## From each possible step,
                for d in dirs:
                    ## Do a BFS to the in-range squares
                    q = queue.Queue()
                    q.put((unit[1]+d[0],unit[2]+d[1],0))
                    if mat[unit[1]+d[0]][unit[2]+d[1]] != ["."]:
                        continue
                    seen = {(unit[1]+d[0],unit[2]+d[1])}
                    while not q.empty():
                        c = q.get()
                        if c[:2] in in_range:
                            # Can't beat this distance
                            if best_step == None or c[2] < best_step[0]:
                                best_step = (c[2], d)
                            break
                        for d2 in dirs:
                            if (c[0]+d2[0],c[1]+d2[1]) not in seen and \
                               mat[c[0]+d2[0]][c[1]+d2[1]] == ["."]:
                                seen.add((c[0]+d2[0],c[1]+d2[1]))
                                q.put((c[0]+d2[0],c[1]+d2[1],c[2]+1))

                if best_step == None:
                    ## If we're trapped and not adjacent to an enemy
                    ## already, we can't attack, so we're done
                    continue

                ## Now, make the step
                swap = mat[unit[1] + best_step[1][0]][unit[2] + best_step[1][1]]
                mat[unit[1] + best_step[1][0]][unit[2] + best_step[1][1]] = unit
                mat[unit[1]][unit[2]] = swap
                unit[1] += best_step[1][0]
                unit[2] += best_step[1][1]
                #print(swap)

            ## Check for adjacent enemies to attack
            lowest = None
            for d in dirs:
                if mat[unit[1]+d[0]][unit[2]+d[1]][0] == "EG"["GE".find(unit[0])]:
                    if lowest == None or mat[unit[1]+d[0]][unit[2]+d[1]][3] < lowest[3]:
                        lowest = mat[unit[1]+d[0]][unit[2]+d[1]]

            ## Deal damage and handle kills
            if lowest != None:
                lowest[3] -= 3 if lowest[0] == "E" else elf_power
                if lowest[3] <= 0:
                    if lowest[0] == "E" and elf_sc:
                        return False
                    alive_units.remove(lowest)
                    mat[lowest[1]][lowest[2]] = ["."]
        rd += 1
    return (rd - 1) * sum(u[3] for u in alive_units)

print("Part 1:", simulate_combat(mat_copy()))
low = 3
high = 50
while high > low:
    mid = (high+low)//2
    if simulate_combat(mat_copy(), True, mid):
        high = mid
    else:
        low = mid + 1

print("Part 2:", simulate_combat(mat_copy(), elf_power=low))
