with open("input.txt") as file:
    inp = file.read().strip()

def react(poly):
    i = 0
    while i < len(poly)-1:
        if abs(ord(poly[i]) - ord(poly[i+1])) == 32:
            poly = poly[:i] + poly[i+2:]
            i = max(0, i-1)
        else:
            i += 1
    return poly

poly = react(inp)
print("Part 1:",len(poly))
print("Part 2:",min(len(react(poly.replace(c,"").replace(c.upper(),""))) for c in set(poly.lower())))
