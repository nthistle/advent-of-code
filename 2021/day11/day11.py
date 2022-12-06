from collections import defaultdict, Counter
import regex
import itertools

nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]


with open("input.txt") as f:
    s = f.read().strip().split("\n")



grid = [[int(x) for x in y] for y in s]
N = len(grid)
M = len(grid[0])

dd = defaultdict(int)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        dd[i,j] = grid[i][j]
        
def iterate(dd):
    nd = defaultdict(int)
    flash = 0
    flashed = set()
    toflash = []
    for x,y in dd.keys():
        nd[x,y] = dd[x,y] + 1
        if nd[x,y] > 9:
            toflash.append((x,y))
            flashed.add((x,y))
    while len(toflash) > 0:
        x,y = toflash.pop(-1)
        for dx in range(-1,2):
            for dy in range(-1,2):
                if (dx,dy)==(0,0):
                    continue
                if x+dx not in range(N):
                    continue
                if y+dy not in range(M):
                    continue
                nd[x+dx,y+dy] += 1
                if nd[x+dx,y+dy] > 9:
                    if (x+dx,y+dy) not in flashed:
                        flashed.add((x+dx,y+dy))
                        toflash.append((x+dx,y+dy))
    for x,y in flashed:
        nd[x,y] = 0
    return nd, len(flashed)

c = 0
while len(set(dd.values())) > 1:
    dd, _ = iterate(dd)
    c += 1
print(c)
#f = 0
#for _ in range(100):
#    dd, fc = iterate(dd)
#    f += fc
#print(f)
