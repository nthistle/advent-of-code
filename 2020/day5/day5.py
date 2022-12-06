with open("input.txt") as f:
    s = f.read().strip().split("\n")

sids = []
for ln in s:
    a,b = ln[:7],ln[7:]
    a = int(a.replace("F","0").replace("B","1"),2)
    b = int(b.replace("L","0").replace("R","1"),2)
    sid = 8*a + b
    sids.append(sid)

print(max(sids))

sids.sort()
m = min(sids)
while m in sids:
    m += 1
print(m)
