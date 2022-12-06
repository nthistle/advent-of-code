with open("input.txt") as f:
    s = f.read().strip().split("\n")

weights = {}
children = {}

seen = set()

for p in s:
    pn = p[:p.find(" ")]
    pw = int(p[p.find("(")+1:p.find(")")])
    weights[pn] = pw
    if "->" in p:
        children[pn] = p[p.find("->")+3:].split(", ")
        seen.update(children[pn])

root = None
for p in weights:
    if p not in seen:
        root = p
print(root)

def find(c):
    w = weights[c]
    if c in children:
        cw = [find(n) for n in children[c]]
        if -1 in cw:
            return -1
        w += sum(cw)
        if len(set(cw)) != 1:
            for i in range(len(cw)):
                if cw[i] != cw[i-1] and cw[i] != cw[i-2]:
                    print(weights[children[c][i]] - cw[i] + cw[i-1])
            return -1
    return w

find(root)
