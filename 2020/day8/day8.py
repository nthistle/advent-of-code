import regex

nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("alt_input.txt") as f:
    s = f.read().strip().split("\n")

ins = []
for line in s:
    i, v = line[:3], line[4:]
    if v[0] == "+":
        v = v[1:]
    v = int(v)
    ins.append((i,v))


def run(cins):
    acc = 0
    ex = set()

    cur = 0
    while cur not in ex and cur < len(cins):
        ex.add(cur)
        i, v = cins[cur]
        if i == "acc":
            acc += v
            cur += 1
        elif i == "jmp":
            cur += v
        elif i == "nop":
            cur += 1

    return (cur not in ex, acc)

print(run(ins)[1])

for i in range(len(ins)):
    if ins[i][0] == "jmp":
        nins = ins[:i] + [("nop",ins[i][1])] + ins[i+1:]
        if run(nins)[0]:
            print(run(nins)[1])
    if ins[i][0] == "nop":
        nins = ins[:i] + [("jmp",ins[i][1])] + ins[i+1:]
        if run(nins)[0]:
            print(run(nins)[1])
