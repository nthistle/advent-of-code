
with open("input.txt") as file:
    inp = file.read().strip()

inp = [int(x) for x in inp.split("\n")]
print("Part 1:",sum(inp))

reached = set()
rsum = 0

while rsum not in reached:
    for val in inp:
        reached.add(rsum)
        rsum += val
        if rsum in reached:
            print("Part 2:",rsum)
            break
