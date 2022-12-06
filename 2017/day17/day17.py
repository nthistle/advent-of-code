from collections import defaultdict
import functools
import regex

nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

inp = 329

buf = [0]

cur = 0

for v in range(1,2017+1):
    cur = (cur + inp) % len(buf)
    buf.insert(cur + 1, v)
    cur += 1

print(buf[buf.index(2017)+1])


after_0 = 0
cur = 0
buf_len = 1
for v in range(1,50000000+1):
    cur = (cur + inp) % buf_len
    buf_len += 1
    if cur == 0:
        after_0 = v
    cur += 1

print(after_0)
