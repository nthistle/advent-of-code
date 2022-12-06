s = "219347865"

cups = list(map(int,s))

for _ in range(100):
    tc = cups[1:4]
    dest = cups[0] - 1
    if dest == 0:
        dest = 9
    while dest in tc:
        dest -= 1
        if dest == 0:
            dest = 9
    new_cups = cups[:1] + cups[4:]
    n_idx = new_cups.index(dest)
    new_cups = new_cups[:n_idx+1] + tc + new_cups[n_idx+1:]
    cups = new_cups[1:] + new_cups[:1]

print("".join(map(str,cups[cups.index(1)+1:] + cups[:cups.index(1)])))

import time
st = time.time()

class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"({self.val})"

lookup = {}

nodes = [Node(int(c)) for c in s]

cur = 10
while len(nodes) < 1000000:
    nodes.append(Node(cur))
    cur += 1

for a,b in zip(nodes,nodes[1:]):
    a.next = b

nodes[-1].next = nodes[0]

lookup = {}
for node in nodes:
    lookup[node.val] = node

cur = nodes[0]

for _ in range(10000000):
    a = cur.next
    b = a.next
    c = b.next
    cur.next = c.next
    used = {cur.val,a.val,b.val,c.val}
    cval = cur.val
    while cval in used:
        cval -= 1
        if cval == 0:
            cval = 1000000
    new_ins = lookup[cval]
    ins_nxt = new_ins.next

    new_ins.next = a
    c.next = ins_nxt

    cur = cur.next

cup1 = lookup[1]
a = cup1.next
b = a.next

et = time.time()

print(a.val * b.val)

print(round(et-st,5))
