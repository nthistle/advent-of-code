with open("input.txt") as f:
    s = f.read().strip().split("\n")

s = [list(x) for x in s]

def ans(xd,yd):
    y,x = 0,0
    c = 0
    while y < len(s):
        if s[y][x%len(s[y])] == "#":
            c += 1
        x += xd
        y += yd
    return c

print(ans(3,1))

print(ans(1,1)*ans(3,1)*ans(5,1)*ans(7,1)*ans(1,2))
