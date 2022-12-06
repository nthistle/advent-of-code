with open("input.txt") as file:
    inp = file.read().strip()

inp = inp.split("\n")

count3 = sum(any(s.count(c) == 3 for c in s) for s in inp)
count2 = sum(any(s.count(c) == 2 for c in s) for s in inp)
print("Part 1:",count2*count3)
for s1 in inp:
    for s2 in inp:
        if sum(s1[i] == s2[i] for i in range(len(s1))) == len(s1)-1:
            print("Part 2:","".join(s1[i] for i in range(len(s1)) if s1[i] == s2[i]))
            break
