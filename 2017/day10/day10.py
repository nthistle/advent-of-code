with open("input.txt") as f:
    s = f.read().strip()

v = [int(x) for x in s.split(",")]

cur = list(range(256))

offset = 0
skip = 0
for length in v:
    cur = cur[length:] + cur[:length][::-1]
    cur = cur[skip:] + cur[:skip]
    offset += length + skip
    skip += 1

offset = (-offset) % len(cur)
cur = cur[offset:] + cur[:offset]

print(cur[0]*cur[1])

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

def xor(vals):
    out = 0
    for val in vals:
        out ^= val
    return out

print("".join(hex(xor(cur[i:i+16])+256)[3:] for i in range(0,256,16)))
