import regex

nums_regex = regex.compile("((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    s = f.read().strip().split("\n")

layers = {}
for line in s:
    line = nums(line)
    layers[line[0]] = line[1]

# if depth is d
# d - 1 in each direction
# returns to top every 2d - 2

def at_top(r,t):
    return t % (2*r - 2) == 0

def v(d,t):
    t = t % (2*d - 2)
    return min(2*d - 2 - t, t)

print(sum(depth*layers[depth] for depth in layers \
          if depth % (2*layers[depth] - 2) == 0))


restrictions = []
for depth in layers:
    restrictions.append((depth, 2 * layers[depth] - 2))

i = 0
while any((i+a)%b == 0 for a,b in restrictions):
    i += 1

print(i)
