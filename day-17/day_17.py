import sys

sys.setrecursionlimit(5000)

with open("input.txt") as file:
    inp = file.read().strip()

dat = [list(sorted(ln.replace(",","").split(" "))) for ln in inp.split("\n")]
dat = [[x[2:].split("..") if ".." in x else [x[2:]] for x in pt] for pt in dat]
dat = [[[int(c) for c in x] for x in pt] for pt in dat]
min_x = min(d[0][0] for d in dat)
max_x = max(d[0][-1] for d in dat)
min_y = min(d[1][0] for d in dat)
max_y = max(d[1][-1] for d in dat)

area = [["." for i in range(max_y+1)] for j in range(max_x-min_x+1)]
for d in dat:
    for x_i in range(d[0][0],d[0][-1]+1):
        for y_i in range(d[1][0],d[1][-1]+1):
            area[x_i - min_x][y_i] = "#"

def dfs(loc):
    if loc[1]+1 > max_y:
        area[loc[0]][loc[1]] = "|"
        return True

    if area[loc[0]][loc[1]+1] == ".":
        area[loc[0]][loc[1]] = "|"
        path = dfs((loc[0],loc[1]+1))
        if path:
            return True
    elif area[loc[0]][loc[1]+1] == "|":
        area[loc[0]][loc[1]] = "|"
        return True

    area[loc[0]][loc[1]] = "|"
    left  = area[loc[0]+1][loc[1]] == "." and dfs((loc[0]+1,loc[1]))
    right = area[loc[0]-1][loc[1]] == "." and dfs((loc[0]-1,loc[1]))
    if not (left or right):
        area[loc[0]][loc[1]] = "~"
    elif not left:
        k_idx = loc[0]+1
        while area[k_idx][loc[1]] == "~":
            area[k_idx][loc[1]] = "|"
            k_idx += 1
        return True
    else:
        k_idx = loc[0]-1
        while area[k_idx][loc[1]] == "~":
            area[k_idx][loc[1]] = "|"
            k_idx -= 1
        return True

dfs((500-min_x, 0))

counts = {"~":0, "|":0}
for line in area:
    for m in line[min_y:]:
        if m in "~|":
            counts[m] += 1
            
print("Part 1:", counts["~"] + counts["|"])
print("Part 2:", counts["~"])
