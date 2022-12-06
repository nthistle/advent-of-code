from collections import defaultdict
import functools
import regex
import heapq

nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

# N,E,S,W
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    s = f.read().strip().split("\n")

##s = """snd 1
##snd 2
##snd p
##rcv a
##rcv b
##rcv c
##rcv d""".split("\n")

regs = defaultdict(int)

def parg(arg):
    if arg.isalpha():
        return regs[arg]
    else:
        return int(arg)

last_sound = -1

ic = 0
while ic in range(len(s)):
    line = s[ic]
    opc = line[:3]
    if opc == "snd":
        last_sound = parg(line[4:])
    elif opc == "set":
        arg1,arg2 = line[4:].split(" ")
        regs[arg1] = parg(arg2)
    elif opc == "add":
        arg1,arg2 = line[4:].split(" ")
        regs[arg1] += parg(arg2)
    elif opc == "mul":
        r1,r2 = line[4:].split(" ")
        regs[r1] *= parg(r2)
    elif opc == "mod":
        r1,r2 = line[4:].split(" ")
        regs[r1] %= parg(r2)
    elif opc == "rcv":
        r1 = line[4:]
        if parg(r1) != 0:
            print(last_sound)
            break
    elif opc == "jgz":
        r1,r2 = line[4:].split(" ")
        if parg(r1) > 0:
            ic += parg(r2)
            continue
    ic += 1



class VM:
    def __init__(self, source, pid, snd_q, rcv_q):
        self.source = source
        self.pid = pid
        self.snd_q = snd_q
        self.rcv_q = rcv_q

        self.regs = defaultdict(lambda : 0)
        self.regs["p"] = self.pid
        self.ic = 0
        self.snd_ctr = 0

    def _parse(self, arg):
        if arg.isalpha():
            return self.regs[arg]
        else:
            return int(arg)

    def run(self):
        retc = -1
        num_steps = 0
        while (retc := self.step()) == 1:
            num_steps += 1
        return (num_steps, retc)

    # return code:
    # 0 = terminated
    # 1 = running
    # 2 = waiting
    def step(self):
        if self.ic not in range(len(self.source)):
            return 0
        instruction = self.source[self.ic]
        opc, args = instruction[:3], instruction[4:]
        if opc == "set":
            arg1, arg2 = args.split(" ")
            self.regs[arg1] = self._parse(arg2)
            self.ic += 1
        elif opc == "add":
            arg1, arg2 = args.split(" ")
            self.regs[arg1] += self._parse(arg2)
            self.ic += 1
        elif opc == "mul":
            arg1, arg2 = args.split(" ")
            self.regs[arg1] *= self._parse(arg2)
            self.ic += 1
        elif opc == "mod":
            arg1, arg2 = args.split(" ")
            self.regs[arg1] %= self._parse(arg2)
            self.ic += 1
        elif opc == "jgz":
            arg1, arg2 = args.split(" ")
            if self._parse(arg1) > 0:
                self.ic += self._parse(arg2)
            else:
                self.ic += 1
        elif opc == "snd":
            arg1 = args
            value = self._parse(arg1)
            self.snd_q.append(value)
            self.snd_ctr += 1
            self.ic += 1
        elif opc == "rcv":
            arg1 = args
            if len(self.rcv_q) > 0:
                self.regs[arg1] = self.rcv_q.pop(0)
                self.ic += 1
            else:
                return 2 # wait for queue
        return 1


q1 = []
q2 = []

m1 = VM(s, 0, q2, q1)
m2 = VM(s, 1, q1, q2)

s1 = s2 = 1
while s1 + s2 > 0:
    s1, _ = m1.run()
    s2, _ = m2.run()

print(m2.snd_ctr)
