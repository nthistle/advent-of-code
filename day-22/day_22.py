from heapq import *

with open("input.txt") as file:
    inp = file.read().strip().split("\n")

## This might not have been enough if the path goes really far into positive
## x, but in practice it works fine
xf = 10
yf = 2

depth = int(inp[0][7:])
target = tuple(int(c) for c in inp[1][8:].split(","))

region = [[0 for _ in range(yf*(target[1]+1))] for _ in range(xf*(target[0]+1))]
geolog = [[0 for _ in range(yf*(target[1]+1))] for _ in range(xf*(target[0]+1))]
erosio = [[0 for _ in range(yf*(target[1]+1))] for _ in range(xf*(target[0]+1))]

for i in range(xf*(target[0]+1)):
    for j in range(yf*(target[1]+1)):
        if i == 0 and j == 0:
            geolog[i][j] = 0
        elif i == target[0] and j == target[1]:
            geolog[i][j] = 0
        elif j == 0:
            geolog[i][j] = i * 16807
        elif i == 0:
            geolog[i][j] = j * 48271
        else:
            geolog[i][j] = erosio[i-1][j] * erosio[i][j-1]
            
        erosio[i][j] = (geolog[i][j] + depth) % 20183
        region[i][j] = erosio[i][j] % 3

risk_level = sum(sum(row[:target[1]+1]) for row in region[:target[0]+1])
print("Part 1:",risk_level)

in_range = lambda c : c[0] in range(len(region)) and c[1] in range(len(region[0]))
h = lambda c : abs(target[0]-c[0])+abs(target[1]-c[1])
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
pq = []
best = {((0,0),1):0}
heappush(pq, (0,0,(0,0),1) )
dist_to_target = 10000
while len(pq) > 0:
    cur = heappop(pq)
    if cur[2:] == (target, 1):
        break
        print(cur)
    for d in dirs:
        nc = (cur[2][0] + d[0], cur[2][1] + d[1])
        if in_range(nc) and region[nc[0]][nc[1]] != cur[3]:
            if (nc, cur[3]) not in best or cur[1] + 1 < best[(nc, cur[3])]:
                best[(nc, cur[3])] = cur[1] + 1
                heappush(pq, (cur[1] + 1 + h(nc), cur[1] + 1, nc, cur[3]))

    new_tool = 3 - region[cur[2][0]][cur[2][1]] - cur[3]
    if (cur[2], new_tool) not in best or cur[1] + 7 < best[(cur[2], new_tool)]:
        best[(cur[2], new_tool)] = cur[1] + 7
        heappush(pq, (cur[0] + 7, cur[1] + 7, cur[2], new_tool))

print("Part 2:",cur[1])
