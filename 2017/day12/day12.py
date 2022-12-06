import regex

nums_regex = regex.compile("((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    s = f.read().strip().split("\n")

g = {}
for line in s:
    line = nums(line)
    g[line[0]] = line[1:]

seen = set()
def dfs(cur):
    if cur in seen:
        return
    seen.add(cur)
    for nxt in g[cur]:
        dfs(nxt)

dfs(0)
print(len(seen))

groups = 1
for i in g:
    if i not in seen:
        dfs(i)
        groups += 1
print(groups)
