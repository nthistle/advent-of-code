with open("input.txt") as file:
    inp = file.read().strip()

steps = [(line[5],line[36]) for line in inp.split("\n")]
step_dict = {}
for step in steps:
    if step[1] in step_dict:
        step_dict[step[1]].append(step[0])
    else:
        step_dict[step[1]] = [step[0]]
    if step[0] not in step_dict:
        step_dict[step[0]] = []
        
order = ""
while len(order) < 26:
    next_poss = "^"
    for poss in step_dict:
        if len(step_dict[poss]) == 0:
            if poss < next_poss:
                next_poss = poss
    order += next_poss
    step_dict.pop(next_poss)
    for poss in step_dict:
        if next_poss in step_dict[poss]:
            step_dict[poss].remove(next_poss)

print("Part 1:",order)


import random

step_dict = {}
for step in steps:
    if step[1] in step_dict:
        step_dict[step[1]].append(step[0])
    else:
        step_dict[step[1]] = [step[0]]
    if step[0] not in step_dict:
        step_dict[step[0]] = []

current_time = 0
cur_working = [] # (letter, time_fin)
while len(step_dict) > 0:
    print(cur_working)
    i = 0
    while i < len(cur_working):
        work = cur_working[i]
        if work[1] == current_time:
            for poss in step_dict:
                if work[0] in step_dict[poss]:
                    step_dict[poss].remove(work[0])
            cur_working.pop(i)
            i -= 1
        i += 1
    to_remove = []
    for poss in step_dict:
        if len(step_dict[poss]) == 0:
            if len(cur_working) < 5:
                to_remove.append(poss)
                cur_working.append((poss, current_time + ord(poss) - 4))
    for d in to_remove:
        step_dict.pop(d)
    current_time = min(cur_working, key=lambda v:v[1])[1]

print(max(cur_working, key=lambda v:v[1])[1])

