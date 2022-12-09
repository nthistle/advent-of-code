from aoc_tools import *

with open("input.txt") as f:
    s = f.read().strip()

s1 = s
i = 0
while len(set(s1[:4])) != 4:
    s1 = s1[1:]
    i += 1
print(i+4)

s2 = s
i = 0
while len(set(s2[:14])) != 14:
    s2 = s2[1:]
    i += 1
print(i+14)


# alternate approach for part 2

cur_window = {}

# mjqjpqmgbljsphdztnvjfqwrcgsmlb
# XXXXXXXXXXXXXX
# to roll the window over one
#  XXXXXXXXXXXXXX (remove m, add d)

# first we need to populate cur_window with the first 14
for i in range(14):
    if s[i] not in cur_window:
        cur_window[s[i]] = 0
    cur_window[s[i]] += 1

# roll until cur_window has 14 unique elements
next_idx = 14
while len(cur_window.keys()) < 14:
    # roll the window by 1
    
    # adding next_idx
    if s[next_idx] not in cur_window:
        cur_window[s[next_idx]] = 0
    cur_window[s[next_idx]] += 1
    
    # delete next_idx - 14
    cur_window[s[next_idx - 14]] -= 1

    if cur_window[s[next_idx - 14]] == 0:
        del cur_window[s[next_idx - 14]]

    next_idx += 1

print(next_idx)


























