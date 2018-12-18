with open("input.txt") as file:
    inp = file.read().strip()

mat = [list(line) for line in inp.split("\n")]

in_range = lambda c : c[0] in range(len(mat)) and c[1] in range(len(mat[c[0]]))
dirs = [(i,j) for i in range(-1,2) for j in range(-1,2) if i != 0 or j != 0]

inf = [[[0,0,0] for c in line] for line in mat]

def update(v, adj):
    if v == ".":
        if adj[1] >= 3:
            return "|"
    elif v == "|":
        if adj[2] >= 3: 
            return "#"
    elif v == "#":
        if adj[2] == 0 or adj[1] == 0:
            return "."
    return v

for time in range(10):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            inf[i][j] = [0,0,0]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            idx = ".|#".find(mat[i][j])
            for d in dirs:
                if in_range((i+d[0],j+d[1])):
                    inf[i+d[0]][j+d[1]][idx] += 1
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = update(mat[i][j], inf[i][j])
time += 1

mats = "".join("".join(row) for row in mat)
print("Part 1:", sum(c == "|" for c in mats) * sum(c == "#" for c in mats))

seen_states = {"".join("".join(row) for row in mat):0}

while time < 1000000000:
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            inf[i][j] = [0,0,0]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            idx = ".|#".find(mat[i][j])
            for d in dirs:
                if in_range((i+d[0],j+d[1])):
                    inf[i+d[0]][j+d[1]][idx] += 1
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = update(mat[i][j], inf[i][j])
    time += 1
    mats = "".join("".join(row) for row in mat)
    if mats in seen_states:
        break
    seen_states[mats] = time
    seen_states[time] = mats

cycle_length = time - seen_states[mats]
mats = seen_states[time - cycle_length + ((1000000000 - time) % cycle_length)]

print("Part 2:", sum(c == "|" for c in mats) * sum(c == "#" for c in mats))
