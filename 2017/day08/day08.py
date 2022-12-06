with open("input.txt") as f:
    s = f.read().strip().split("\n")

from collections import defaultdict

reg = defaultdict(lambda : 0)

m = 0
for ins in s:
    cmd, cnd = ins.split(" if ")
    cnd_r, cnd_op, cnd_cmp = cnd.split(" ")
    if eval(str(reg[cnd_r]) + cnd_op + cnd_cmp):
        cmd_r, cmd_op, cmd_arg = cmd.split(" ")
        if cmd_op == "inc":
            reg[cmd_r] += int(cmd_arg)
        elif cmd_op == "dec":
            reg[cmd_r] -= int(cmd_arg)
        m = max(m, reg[cmd_r])

print(max(reg.values()))
print(m)
