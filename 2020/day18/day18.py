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
    s = f.read().strip().split("\n")

def ev(ln):
    v = 0
    op = "+"
    i = 0
    while i < len(ln):
        t = ln[i]
        if t in "()":
            pc = 1
            j = i + 1
            while pc > 0:
                if ln[j] == "(":
                    pc += 1
                elif ln[j] == ")":
                    pc -= 1
                j += 1
            vv = ev(ln[i+1:j-1])
            if op == "+":
                v += vv
            elif op == "*":
                v *= vv
            i = j - 1
        elif t in "+*":
            op = t
        else:
            if op == "+":
                v += int(t)
            elif op == "*":
                v *= int(t)
        i += 1
    return v

ss = 0
for line in s:
    line = line.replace("(","( ").replace(")"," )").split(" ")
    ss += ev(line)
print(ss)


class Pear:
    def __init__(self, s):
        self.v = int(s)

    def __add__(self, o):
        return Pear(self.v * o.v)

    def __mul__(self, o):
        return Pear(self.v + o.v)

ss = 0
for line in s:
    line = line.replace("+","?").replace("*","+").replace("?","*")
    line = line.replace("(","( ").replace(")"," )").split(" ")
    line = ["Pear("+x+")" if x.isdigit() else x for x in line]
    line = "".join(line)
    #print(line)
    ss += eval(line).v
print(ss)
