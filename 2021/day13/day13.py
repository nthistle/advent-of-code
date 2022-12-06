from collections import defaultdict, Counter
import regex
import itertools

nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    s, z = f.read().strip().split("\n\n")

pts = set()
for x in s.split("\n"):
    a,b = x.split(",")
    pts.add((int(a),int(b)))

folds = [("x=" in y, nums(y)) for y in z.split("\n")]
# x = is true

cur = pts
for xf,(v,) in folds:
    ncur = set()
    for a,b in cur:
        if xf:
            if a < v:
                ncur.add((a,b))
            else:
                ncur.add((v-(a-v),b))
        else:
            if b < v:
                ncur.add((a,b))
            else:
                ncur.add((a,v-(b-v)))
    cur = ncur
    print(len(cur))

print("\n".join("".join(".#"[(i,j) in cur] \
                for i in range(-1,40)) for j in range(-1,7)))
