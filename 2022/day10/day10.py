import string
from aoc_tools import *
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

with open("input.txt") as f:
    s = f.read().strip()
# print("\n".join(x[:60] for x in s.split("\n")[:10]))

mark_cycles = [20, 60, 100, 140, 180, 220]
marked_signal_strengths = []
cycles_elapsed = 0
reg = 1

for line in s.split("\n"):
    if line.startswith("noop"):
        cycles_elapsed += 1
        if cycles_elapsed in mark_cycles:
            marked_signal_strengths.append(cycles_elapsed * reg)
    else:
        # add operation takes 2 cycles, only updates signal strength AFTER
        cycles_elapsed += 1
        if cycles_elapsed in mark_cycles:
            marked_signal_strengths.append(cycles_elapsed * reg)
        cycles_elapsed += 1
        if cycles_elapsed in mark_cycles:
            marked_signal_strengths.append(cycles_elapsed * reg)
        value = int(line.split(" ")[1])
        reg += value

print(sum(marked_signal_strengths))


cycles_elapsed = 0
reg = 1

crt = ["." for _ in range(240)]

for line in s.split("\n"):
    if line.startswith("noop"):
        pixel_x = (cycles_elapsed) % 40
        if abs(reg - pixel_x) <= 1:
            crt[cycles_elapsed % 240] = "#"
        else:
            crt[cycles_elapsed % 240] = "."
        cycles_elapsed += 1
    else:
        pixel_x = cycles_elapsed % 40
        if abs(reg - pixel_x) <= 1:
            crt[cycles_elapsed % 240] = "#"
        else:
            crt[cycles_elapsed % 240] = "."
        cycles_elapsed += 1
        pixel_x = cycles_elapsed % 40
        if abs(reg - pixel_x) <= 1:
            crt[cycles_elapsed % 240] = "#"
        else:
            crt[cycles_elapsed % 240] = "."
        cycles_elapsed += 1
        
        value = int(line.split(" ")[1])
        reg += value

print("\n".join("".join(crt[i:i+40]) for i in range(0,240,40)))
