import string
from aoc_tools import *
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

with open("input.txt") as f:
    s = f.read().strip()
            
best = 10000
for sx2 in range(41):
    for sy2 in range(81):
        #print("\n".join(x[:60] for x in s.split("\n")[:10]))

        g = [list(x) for x in s.split("\n")]
        n = len(g)
        m = len(g[0])

        sx,sy = [(i,j) for i in range(n) for j in range(m) if g[i][j] == "S"][0]
        tx,ty = [(i,j) for i in range(n) for j in range(m) if g[i][j] == "E"][0]

        g[sx][sy] = "a"
        g[tx][ty] = "z"

        if g[sx2][sy2] != "a":
            continue

        g = [[ord(c) - ord("a") for c in r] for r in g]

        from collections import deque

        dst = defaultdict(lambda : 1000000)
        dst[sx2,sy2] = 0

        q = deque([(sx2,sy2)])
        ans = 100000
        while len(q) > 0:
            cx,cy = q.popleft()
            if (cx,cy) == (tx,ty):
                ans = dst[tx,ty]
                if (sx2,sy2) == (sx,sy):
                    print(ans)
                break
            for dx,dy in dirs:
                nx,ny = cx+dx,cy+dy
                if nx in range(n) and ny in range(m):
                    if g[cx][cy] >= g[nx][ny] - 1:
                        ndst = dst[cx,cy] + 1
                        if ndst < dst[nx,ny]:
                            q.append((nx,ny))
                            dst[nx,ny] = ndst
        best = min(best,ans)
print(best)






















































