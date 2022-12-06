import regex

nums_regex = regex.compile("((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

# yeah, i know this should be dfs but
valid = set()
last_len = -1
while len(valid) != last_len:
    last_len = len(valid)
    for color in rules:
        if rules[color] is None:
            continue
        if any(rc == "shiny gold" for rn, rc in rules[color]):
            valid.add(color)
        if any(rc in valid for rn, rc in rules[color]):
            valid.add(color)

print(len(valid))

import sys

sys.setrecursionlimit(100000)

def ans(c):
    cnt = 1
    if rules[c] is None:
        return cnt
    for rn, rc in rules[c]:
        cnt += rn * ans(rc)
    return cnt

print(ans("shiny gold") - 1)
