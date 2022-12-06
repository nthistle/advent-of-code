def xor(vals):
    out = 0
    for val in vals:
        out ^= val
    return out

def knot_hash(s):
    lengths = [ord(c) for c in s] + [17,31,73,47,23]
    cur = list(range(256))
    offset = 0
    skip = 0
    for _ in range(64):
        for length in lengths:
            cur = cur[length:] + cur[:length][::-1]
            cur = cur[skip:] + cur[:skip]
            offset = (offset + length + skip) % len(cur)
            skip = (skip + 1) % len(cur)
    offset = (-offset) % len(cur)
    cur = cur[offset:] + cur[:offset]
    return "".join(hex(xor(cur[i:i+16])+256)[3:] for i in range(0,256,16))

key = "ugkiagan"

def count_bits(v):
    c = 0
    while v:
        c += 1
        v = v & (v - 1)
    return c

hashes = [int(knot_hash(f"{key}-{i}"),16) for i in range(128)]

print(sum(count_bits(khash) for khash in hashes))

grid = [list(bin(khash)[2:].rjust(128, "0")) for khash in hashes]

def dfs(cur, seen):
    if cur[0] not in range(128) or cur[1] not in range(128):
        return
    if grid[cur[0]][cur[1]] != '1':
        return
    if cur in seen:
        return
    seen.add(cur)
    x,y = cur
    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
        dfs((x+dx,y+dy), seen)

count = 0
seen = set()
for i in range(128):
    for j in range(128):
        if (i,j) not in seen and grid[i][j] == '1':
            dfs((i,j), seen)
            count += 1
print(count)
