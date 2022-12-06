from datetime import datetime

with open("input.txt") as file:
    inp = file.read()

inp = [(datetime.strptime(line[1:17],"%Y-%m-%d %H:%M"),line[19:]) for line in inp.strip().split("\n")]
inp.sort()

sleep = {}
cguard = None
i = 0
while i < len(inp):
    if inp[i][1].startswith("Guard #"):
        cguard = int(inp[i][1][7:inp[i][1].find(" ",7)])
    else:
        if cguard not in sleep:
            sleep[cguard] = 0
        sleep[cguard] += (inp[i+1][0] - inp[i][0]).seconds//60
        i += 1
    i += 1

sleepiest = max(sleep, key=sleep.get)

minutes = [0 for i in range(60)]
cguard = None
i = 0
while i < len(inp):
    if inp[i][1].startswith("Guard #"):
        cguard = int(inp[i][1][7:inp[i][1].find(" ",7)])
    elif cguard == sleepiest:
        for j in range(inp[i][0].minute, inp[i+1][0].minute):
            minutes[j] += 1
        i += 1
    i += 1

print("Part 1:",sleepiest * max(enumerate(minutes), key=lambda v:v[1])[0])

sleep = {}
cguard = None
i = 0
while i < len(inp):
    if inp[i][1].startswith("Guard #"):
        cguard = int(inp[i][1][7:inp[i][1].find(" ",7)])
    else:
        if cguard not in sleep:
            sleep[cguard] = [0 for i in range(60)]
        for j in range(inp[i][0].minute, inp[i+1][0].minute):
            sleep[cguard][j] += 1
        i += 1
    i += 1

guard = max(sleep, key=lambda k:max(sleep[k]))
print("Part 2:",guard * max(enumerate(sleep[guard]), key=lambda v:v[1])[0])
