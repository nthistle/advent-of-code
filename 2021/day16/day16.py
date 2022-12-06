from collections import defaultdict, Counter
import regex
import itertools

nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    s = f.read().strip()

class PackDec:
    def __init__(self, s):
        self.vals = list(s)
        self.buffer = ""
        self.i = 0 # next to add to buffer

    def get(self, n):
        r = ""
        while n > 0:
            a = self.buffer[:n]
            self.buffer = self.buffer[n:]
            r += a
            n -= len(a)
            if len(self.buffer) == 0:
                self.i += 1
                self.buffer = bin(16 + int(self.vals[self.i - 1],16))[3:]
        return r

    def align(self):
        if len(self.buffer) < 4:
            self.buffer = ""

class BitsOnly:
    def __init__(self, s):
        self.s = s

    def get(self, n):
        a, self.s = self.s[:n], self.s[n:]
        return a

global version_sum
version_sum = 0

pd = PackDec(s)

def parse(pd):
    global version_sum
    version = int(pd.get(3),2)
    typeid = int(pd.get(3),2)
    version_sum += version

    if typeid == 4: #literal
        leadbit = pd.get(1)
        value = pd.get(4)
        while leadbit == "1":
            leadbit = pd.get(1)
            value += pd.get(4)
        return int(value, 2)
    else:
        ltid = pd.get(1)
        if ltid == "0":
            total_length = int(pd.get(15),2)
            bo = BitsOnly(pd.get(total_length))
            packs = []
            while len(bo.s) > 0:
                try:
                    packs.append(parse(bo))
                except:
                    pass
        else:
            num_packs = int(pd.get(11),2)
            packs = []
            for _ in range(num_packs):
                packs.append(parse(pd))
                
        if typeid == 0:
            return sum(packs)
        elif typeid == 1:
            r = 1
            for p in packs:
                r *= p
            return r
        elif typeid == 2:
            return min(packs)
        elif typeid == 3:
            return max(packs)
        elif typeid == 5:
            return 1 if packs[0] > packs[1] else 0
        elif typeid == 6:
            return 1 if packs[0] < packs[1] else 0
        elif typeid == 7:
            return 1 if packs[0] == packs[1] else 0
        else:
            print("uhoh")

print(parse(pd))
