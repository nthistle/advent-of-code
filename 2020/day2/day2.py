with open("input.txt") as f:
    s = f.read().strip().split("\n")

c = 0
for ln in s:
    r,lt,pw = ln.split(" ")
    lt = lt[0]
    rl,rh = map(int,r.split("-"))
    if rl <= pw.count(lt) <= rh:
        c += 1

print(c)


c = 0
for ln in s:
    r,lt,pw = ln.split(" ")
    lt = lt[0]
    rl,rh = map(int,r.split("-"))
    if (pw[rl-1] == lt) ^ (pw[rh-1] == lt):
        c += 1

print(c)
