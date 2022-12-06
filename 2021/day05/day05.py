from collections import defaultdict

with open("input.txt") as f:
    s = f.read().strip().split("\n")

d = defaultdict(int)

for line in s:
    a,b = line.split(" -> ")
    x1,y1 = a.split(",")
    x2,y2 = b.split(",")
    x1=int(x1)
    y1=int(y1)
    x2=int(x2)
    y2=int(y2)
    if x1 == x2:
        x1,x2 = min(x1,x2),max(x1,x2)
        y1,y2 = min(y1,y2),max(y1,y2)
        for y in range(y1,y2+1):
            d[x1,y] += 1
    elif y1 == y2:
        x1,x2 = min(x1,x2),max(x1,x2)
        y1,y2 = min(y1,y2),max(y1,y2)
        for x in range(x1,x2+1):
            d[x,y1] += 1
    else:
        cx,cy = x1,y1
        if x2 > x1:
            dx = 1
        else:
            dx = -1
        if y2 > y1:
            dy = 1
        else:
            dy = -1
        while (cx,cy) != (x2,y2):
            d[cx,cy] += 1
            cx += dx
            cy += dy
        d[cx,cy] += 1

print(sum(1 for v in d.values() if v > 1))
    
