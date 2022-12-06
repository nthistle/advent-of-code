import regex

nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    s = f.read().strip().split("\n")


mod = 2147483647

a, = nums(s[0])
b, = nums(s[1])

a_mult = 16807
b_mult = 48271

a_seen = {}
b_seen = {}

count = 0
mask = (1 << 16) - 1
for i in range(40_000_000):
    a = (a_mult * a) % mod
    b = (b_mult * b) % mod
    if (a & mask) == (b & mask):
        count += 1

print(count)

a, = nums(s[0])
b, = nums(s[1])

count = 0
num_generated = 0
a_next = None
b_next = None

while num_generated < 5_000_000:
    if a_next is None:
        a = (a_mult * a) % mod
        if a & (4 - 1) == 0:
            a_next = a
    if b_next is None:
        b = (b_mult * b) % mod
        if b & (8 - 1) == 0:
            b_next = b
    if a_next is not None and b_next is not None:
        num_generated += 1
        if (a_next & mask) == (b_next & mask):
            count += 1
        a_next = b_next = None

print(count)
