with open("input.txt") as f:
    s = f.read().strip().split("\n")

v = [int(x) for x in s]
idx = 0

steps = 0
while idx in range(len(v)):
    v[idx] += 1
    idx += v[idx] - 1
    steps += 1

print(steps)


v = [int(x) for x in s]
idx = 0

steps = 0
while idx in range(len(v)):
    j = v[idx]
    if j >= 3:
        v[idx] -= 1
    else:
        v[idx] += 1
    idx += j
    steps += 1

print(steps)
