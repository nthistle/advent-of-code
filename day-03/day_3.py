import numpy as np # lmao

with open("input.txt") as file:
    inp = file.read().strip()

inp = inp.replace("#","").replace("@ ","").replace(":","").replace(","," ").replace("x"," ").split("\n")
inp = [[int(x) for x in line.split(" ")] for line in inp]

mat = np.empty((1000,1000), dtype=np.int)

for entry in inp:
    mat[entry[1]:entry[1]+entry[3],entry[2]:entry[2]+entry[4]] += 1

print("Part 1:",(mat > 1).sum())

mat -= 1

for entry in inp:
    if mat[entry[1]:entry[1]+entry[3],entry[2]:entry[2]+entry[4]].sum() == 0:
        print("Part 2:",entry[0])
