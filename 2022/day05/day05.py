from aoc_tools import *

with open("input.txt") as f:
    s = f.read().strip()

s = s.split("\n")

stacks = [
    [],
    list("QSWCZVFT"),
    list("QRB"),
    list("BZTQPMS"),
    list("DVFRQH"),
    list("JGLDBSTP"),
    list("WRTZ"),
    list("HQMNSFRJ"),
    list("RNFHW"),
    list("JZTQPRB")
]


for l in s[10:]:
    l = l[5:]
    a,r = l.split(" from ")
    b,c = r.split(" to ")
    a=int(a)
    b=int(b)
    c=int(c)
    for _ in range(a):
        stacks[c].append(stacks[b].pop(-1))

print("".join(z[-1] for z in stacks[1:]))



stacks = [
    [],
    list("QSWCZVFT"),
    list("QRB"),
    list("BZTQPMS"),
    list("DVFRQH"),
    list("JGLDBSTP"),
    list("WRTZ"),
    list("HQMNSFRJ"),
    list("RNFHW"),
    list("JZTQPRB")
]


for l in s[10:]:
    l = l[5:]
    a,r = l.split(" from ")
    b,c = r.split(" to ")
    a=int(a)
    b=int(b)
    c=int(c)
    stacks[c].extend(stacks[b][-a:])
    del stacks[b][-a:]
#    for _ in range(a):
#        stacks[b].pop(-1)


print("".join(z[-1] for z in stacks[1:]))
