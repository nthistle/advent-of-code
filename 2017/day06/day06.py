import re

with open("input.txt") as f:
    s = re.sub("\\s+"," ",f.read().strip()).split(" ")

s = [int(x) for x in s]

seen = {}

count = 0
while tuple(s) not in seen:
    seen[tuple(s)] = count
    idx = max(range(len(s)), key = lambda i : (s[i], -i))
    value = s[idx]
    s[idx] = 0
    per, rem = value // len(s), value % len(s)
    for i in range(len(s)):
        s[i] += per
        if (i - idx - 1) % len(s) < rem:
            s[i] += 1
    count += 1

print(count)
print(count - seen[tuple(s)])
