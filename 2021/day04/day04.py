with open("input.txt") as f:
    s = f.read().strip().split("\n\n")

nums = s[0]
boards = s[1:]

nums = [int(x) for x in nums.split(",")]
boards = [[[int(x) for x in r.strip().split()] for r in b.split("\n")] for b in boards]

def wins(b):
    for i in range(5):
        if all(b[i][j] for j in range(5)):
            return True
        if all(b[j][i] for j in range(5)):
            return True
    return False

best = (0, None)
for b in boards:
    l = {}
    for i in range(5):
        for j in range(5):
            l[b[i][j]] = (i,j)

    bm = [[False for _ in range(5)] for _ in range(5)]

    for z,n in enumerate(nums):
        if n in l:
            x,y = l[n]
            bm[x][y] = True
        if wins(bm):
            best = max(best, (z, b))
            if z == 81:
                # sum unmarked
                su = 0
                for i in range(5):
                    for j in range(5):
                        if not bm[i][j]:
                            su += b[i][j]
                print(su * n)
            break

print(best)





