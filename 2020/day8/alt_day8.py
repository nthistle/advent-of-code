import re

filename = "alt_input.txt"

with open(filename, "r") as file_reader:
    aoc_input = file_reader.read()
codes = aoc_input.split("\n")

regex_code = re.compile("^([a-z]{3}) ((\\+|-)\\d+)")

for i in range(len(codes)):
    match_code = regex_code.match(codes[i])
    codes[i] = (match_code.group(1), int(match_code.group(2)))


# Part 1
def handle_codes(codes):
    acc = 0
    i = 0
    already_visited = set()
    finished = False
    while True:
        if i in already_visited:
            break
        if i >= len(codes):
            finished = True
            break
        already_visited.add(i)

        code = codes[i]
        if code[0] == "acc":
            acc += code[1]
            i += 1
        if code[0] == "jmp":
            i += code[1]
        if code[0] == "nop":
            i += 1
    return finished, acc


print("Part 1: Loop at acc value {}".format(handle_codes(codes)[1]))

# Part 2
for i in range(len(codes)):
    if codes[i][0] == "nop" or codes[i][0] == "jmp":
        copy_codes = list()

        for copy_code in codes:
            copy_codes.append(copy_code)

        if codes[i][0] == "nop":
            copy_codes.remove(copy_codes[i])
            copy_codes.insert(i, ("jmp", codes[i][1]))

        if codes[i][0] == "jmp":
            copy_codes.remove(copy_codes[i])
            copy_codes.insert(i, ("nop", codes[i][1]))

        tup = handle_codes(copy_codes)
        if tup[0]:
            print("Part 2: working Program acc value {}".format(tup[1]))
