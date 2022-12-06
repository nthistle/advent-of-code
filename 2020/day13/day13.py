import functools

with open("input.txt") as f:
    s = f.read().strip().split("\n")

ts = int(s[0])
v = s[1].split(",")
nums = set(int(x) for x in v if x != "x")

c = ts
while all(c % n != 0 for n in nums):
    c += 1

for n in nums:
    if c % n == 0:
        print(n * (c - ts))

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def _crt(n1, n2, r1, r2):
    d, m1, m2 = egcd(n1, n2)
    return (r1 * m2 * n2 + r2 * m1 * n1) % (n1 * n2)

def crt(mods, ress):
    return functools.reduce(
        lambda p1, p2 : (p1[0] * p2[0], _crt(p1[0], p2[0], p1[1], p2[1]))
        , zip(mods, ress))[1]

mods = []
ress = []

for i,x in enumerate(v):
    if x == "x":
        continue
    mods.append(int(x))
    ress.append(-i)

print(crt(mods, ress))
