

with open("input.txt") as f:
    s = f.read()

a = [int(x) for x in s.strip().split("\n")]

print(sum(1 for x,y in zip(a,a[1:]) if y > x))

sliding = [x+y+z for x,y,z in zip(a,a[1:],a[2:])]

print(sum(1 for x,y in zip(sliding,sliding[1:]) if y > x))
