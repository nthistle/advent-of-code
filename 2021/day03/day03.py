with open("input.txt") as f:
    s = f.read().strip().split("\n")

n = len(s[0])
r = ""
for i in range(n):
    zc = 0
    oc = 0
    for line in s:
        if line[i] == "1":
            oc += 1
        else:
            zc += 1
    if zc > oc:
        r += "0"
    else:
        r += "1"

r2 = "".join("1" if x == "0" else "0" for x in r)

print(int(r,2)*int(r2,2))

def get_a(keep_common):
    cur = s[:]
    for i in range(n):
        new = []
        zc = 0
        oc = 0
        for x in cur:
            if x[i] == "1":
                oc += 1
            else:
                zc += 1
        keep_zeros = (zc > oc) if keep_common else (oc >= zc)
        for x in cur:
            if keep_zeros:
                if x[i] == "0":
                    new.append(x)
            else:
                if x[i] == "1":
                    new.append(x)
        cur = new
        if len(cur) == 1:
            break
    return cur[0]

print(int(get_a(True),2) * int(get_a(False),2))









                
    
