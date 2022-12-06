with open("input.txt") as f:
    s = f.read().strip().split("\n")

print(sum(1 for p in s if p.count(" ")+1 == len(set(p.split(" ")))))

print(sum(1 for p in s if p.count(" ")+1 == \
          len(set("".join(sorted(pp)) for pp in p.split(" ")))))
