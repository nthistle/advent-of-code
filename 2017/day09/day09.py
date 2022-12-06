with open("input.txt") as f:
    s = f.read().strip()

import re

s = re.sub("!.","",s)

in_g = False
g_count = 0
idx = 0
while idx < len(s):
    if in_g:
        if s[idx] == ">":
            in_g = False
        else:
            g_count += 1
    else:
        if s[idx] == "<":
            in_g = True
    idx += 1

s = re.sub("\\<.*?\\>","",s)

scores = 0
stack = []
for c in s:
    if c == "{":
        stack.append(0)
    elif c == "}":
        stack.pop(-1)
        scores += len(stack) + 1

print(scores)
print(g_count)
