with open("input.txt") as f:
    s = f.read().strip().split("\n")

import re

s = [re.sub("\\s+"," ",r).split(" ") for r in s]
s = [[int(x) for x in r] for r in s]

print(sum(max(r)-min(r) for r in s))

ans = 0
for r in s:
    for i in range(len(r)):
        for j in range(i+1,len(r)):
            if r[i] % r[j] == 0:
                ans += r[i] // r[j]
            elif r[j] % r[i] == 0:
                ans += r[j] // r[i]

print(ans)
