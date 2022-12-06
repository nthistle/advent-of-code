with open("input.txt") as file:
    inp = file.read().strip()

inp = inp.split("\n")
states = inp[2:]
initial_state = inp[0][15:]
states = {state[:5]:state[-1:] for state in states}

cur_state = initial_state
left_idx = 0
for _ in range(20):
    cur_state = "...." + cur_state + "...."
    new_state = ""
    for i in range(len(cur_state)-4):
        new_state += states[cur_state[i:i+5]]
    new_state = new_state.rstrip(".")
    left_idx += len(new_state) - len(new_state.lstrip(".")) - 2
    cur_state = new_state.lstrip(".")

print("Part 1:",sum(left_idx + i for i, v in enumerate(cur_state) if v == "#"))

cur_gen = 20
seen_states = {}

while cur_state not in seen_states:
    seen_states[cur_state] = (cur_gen, left_idx)
    cur_state = "...." + cur_state + "...."
    new_state = ""
    for i in range(len(cur_state)-4):
        new_state += states[cur_state[i:i+5]]
    new_state = new_state.rstrip(".")
    left_idx += len(new_state) - len(new_state.lstrip(".")) - 2
    cur_state = new_state.lstrip(".")
    cur_gen += 1

cycle_length = cur_gen - seen_states[cur_state][0]
left_dif = left_idx - seen_states[cur_state][1]

left_idx = left_idx + left_dif * ((50000000000 - cur_gen) // cycle_length)
cur_gen = cur_gen + cycle_length * ((50000000000 - cur_gen) // cycle_length)

while cur_gen < 50000000000:
    cur_state = "...." + cur_state + "...."
    new_state = ""
    for i in range(len(cur_state)-4):
        new_state += states[cur_state[i:i+5]]
    new_state = new_state.rstrip(".")
    left_idx += len(new_state) - len(new_state.lstrip(".")) - 2
    cur_state = new_state.lstrip(".")
    cur_gen += 1

print("Part 2:",sum(left_idx + i for i, v in enumerate(cur_state) if v == "#"))
