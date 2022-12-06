with open("input.txt") as f:
    s = f.read().strip("\n")

s = s.split("\n")

pkc,pkd = map(int,s)

mod = 20201227

loopc = 0
val = 1
while val != pkc:
    val = (7 * val) % mod
    loopc += 1

print(pow(pkd,loopc,mod))

