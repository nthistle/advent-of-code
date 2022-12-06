from aoc_tools import *

with open("input.txt") as f:
    s = f.read()

s = [x.split(" ") for x in s.strip().split("\n")]

# A = X = Rock
# B = Y = Paper
# C = Z = Scissors

def f(s):
    r = 0
    for a, b in s:
        if b == "X":
            r += 1
            if a == "C":
                r += 6
            elif a == "A":
                r += 3
        elif b == "Y":
            r += 2
            if a == "A":
                r += 6
            elif a == "B":
                r += 3
        elif b == "Z":
            r += 3
            if a == "B":
                r += 6
            elif a == "C":
                r += 3
    return r

print(f(s))

m = {
    "AX": "Z",
    "AY": "X",
    "AZ": "Y",
    "BX": "X",
    "BY": "Y",
    "BZ": "Z",
    "CX": "Y",
    "CY": "Z",
    "CZ": "X",
}

s = [(a, m[a+b]) for a, b in s]

print(f(s))
