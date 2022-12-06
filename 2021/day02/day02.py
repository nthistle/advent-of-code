with open("input.txt") as f:
    s = f.read().strip().split("\n")

# part 1
horiz = 0
depth = 0
for line in s:
    op,x = line.split(" ")
    x = int(x)
    if op == "forward":
        horiz += x
    elif op == "down":
        depth += x
    elif op == "up":
        depth -= x

print(horiz*depth)

horiz = 0
depth = 0
aim = 0
for line in s:
    op,x = line.split(" ")
    x = int(x)
    if op == "forward":
        horiz += x
        depth += aim * x
    elif op == "down":
        aim += x
    elif op == "up":
        aim -= x
        
print(horiz*depth)
