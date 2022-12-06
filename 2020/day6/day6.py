with open("input.txt") as f:
    s = f.read().strip().split("\n\n")

print(sum(len(set(r.replace("\n",""))) for r in s))

import string

cc = 0
for r in s:
    p = r.split("\n")
    for c in string.ascii_lowercase:
        if all(c in pi for pi in p):
            cc += 1
print(cc)


print(sum(1 for c in string.ascii_lowercase for r in s if all(c in pi for pi in r.split("\n"))))
