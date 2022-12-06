with open("input.txt") as f:
    s = f.read().strip()

print(sum(int(s[i]) for i in range(len(s)) if s[i] == s[i-1]))

n = len(s)

print(sum(int(s[i]) for i in range(len(s)) if s[i] == s[(i+n//2)%n]))
