from aoc_tools import *

with open("input.txt") as f:
    s = f.read().strip()

files = {}

folders = set()

cur = []

for cmd in s.split("\n"):
    if cmd.startswith("$"):
        if cmd.startswith("$ cd"):
            r = cmd[5:]
            if r == "..":
                if len(cur) > 0:
                    cur.pop(-1)
            elif r == "/":
                cur = []
            else:
                cur.extend(r.split("/"))
    else:
        size, name = cmd.split(" ")
        if size == "dir":
            continue
        size = int(size)
        files["/".join(cur + [name])] = size
    folders.add("/".join(cur))


r = 0
fsizes = {}
for folder in folders:
    fsize = 0
    for file in files:
        if file.startswith(folder):
            fsize += files[file]
    if fsize <= 100000:
        r += fsize
    fsizes[folder] = fsize

print(r)

print(min(v for v in fsizes.values() if 70000000 - fsizes[""] + v >= 30000000))

























