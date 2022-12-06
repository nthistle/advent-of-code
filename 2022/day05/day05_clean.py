import copy
import re

with open("input.txt") as f:
    raw_input_string = f.read().strip()

initial_crate_config_string, operations_string = raw_input_string.split("\n\n")

stacks = []

initial_crate_config_lines = initial_crate_config_string.split("\n")
# 3 characters in between stacks
for _ in range((len(initial_crate_config_lines[-1]) + 1) // 4):
    stacks.append([])

for line in initial_crate_config_lines[-2::-1]:
    for stack, crate in zip(stacks, line[1::4]):
        if crate != " ":
            stack.append(crate)

operations = []
for line in operations_string.split("\n"):
    operations.append(
        tuple(
            map(int, re.match("^move (\\d+) from (\\d+) to (\\d+)$", line).groups())
        )
    )

# save a copy for part 2
_stacks = copy.deepcopy(stacks)

# part 1:
for cnt, src, dst in operations:
    for _ in range(cnt):
        stacks[dst - 1].append(stacks[src - 1].pop(-1))

print("".join(stack[-1] for stack in stacks))


# part 2:
stacks = _stacks

for cnt, src, dst in operations:
    stacks[dst - 1].extend(stacks[src - 1][-cnt:])
    del stacks[src - 1][-cnt:]

print("".join(stack[-1] for stack in stacks))
