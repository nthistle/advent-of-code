from collections import defaultdict
import functools
import regex
import heapq

nums_regex = regex.compile("^([^\\d]*?)((?P<nums>\\-?\\d+)([^\\d]*?))*$")

# N,E,S,W
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    s = f.read().strip("\n")

ins = s.split("\n")

regs = defaultdict(lambda : 0)
reg_names = "abcdefgh"

#regs['a'] = 1

tc = 0
ic = 0
mulc = 0
while ic in range(len(ins)):
    #print(("%05d @ %02d:  " % (tc,ic)) + "\t".join(str(regs[r]) for r in reg_names))
    opc,x,y = ins[ic].split(" ")
    #if ic == 24:
    #    print(("%08d @ %02d:  " % (tc,ic)) + "\t".join(str(regs[r]) for r in reg_names))
    if opc == "set":
        regs[x] = (regs[y] if y in reg_names else int(y))
    elif opc == "sub":
        regs[x] -= (regs[y] if y in reg_names else int(y))
    elif opc == "mul":
        regs[x] *= (regs[y] if y in reg_names else int(y))
        mulc += 1
    elif opc == "jnz":
        if (regs[x] if x in reg_names else int(x)) != 0:
            ic += (regs[y] if y in reg_names else int(y)) - 1
    ic += 1
    tc += 1
    #if tc == 10:
    #    regs['b'] = 12
    #    regs['c'] = 216
#print(regs['h'])
print(mulc)

# part 2 is counting # of composite numbers in range(109300, 126300+17, 17)
primes = []
cur = 2
while cur <= int(0.5 + (126300 ** 0.5)):
    if all(cur % p != 0 for p in primes):
        primes.append(cur)
    cur += 1

out = 0
for n in range(109300, 126300+17, 17):
    if any(n % p == 0 for p in primes):
        out += 1
print(out)
