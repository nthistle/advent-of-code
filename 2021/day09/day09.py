from collections import defaultdict, Counter
import regex

nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    s = f.read().strip().split("\n")

g = [[int(x) for x in list(y)] for y in s]

c = 0
start = set()
for i in range(len(g)):
    for j in range(len(g[i])):
        valid = True
        for dx,dy in ((-1,0),(1,0),(0,1),(0,-1)):
            nx = i + dx
            ny = j + dy
            if nx in range(len(g)) and ny in range(len(g[i])):
                if g[nx][ny] <= g[i][j]:
                    valid = False
                    break
        if valid:
            c += 1 + g[i][j]
            start.add((i,j))
print(c)

seen={}
def dfs(i,j,c):
    if i not in range(len(g)) or j not in range(len(g[i])):
        return
    if g[i][j] == 9:
        return
    if (i,j) in seen:
        return
    seen[i,j] = c
    for dx,dy in ((-1,0),(1,0),(0,1),(0,-1)):
        x,y = i + dx, j + dy
        dfs(x,y,c)

cur = 0
for i,j in start:
    dfs(i,j,cur)
    cur += 1

sizes = []
for i in range(cur):
    sizes.append(sum(1 for x in seen if seen[x] == i))

sizes.sort()
