with open("input.txt") as f:
    s = f.read().strip()

s = [int(x) for x in s.split("\n")]

# part 1
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]+s[j] == 2020:
            print(s[i]*s[j])

# part 2
for i in range(len(s)):
    for j in range(i+1,len(s)):
        for k in range(j+1,len(s)):
            if s[i]+s[j]+s[k] == 2020:
                print(s[i]*s[j]*s[k])


# faster version for neel
s_set = set()
for i in range(len(s)):
    if 2020 - s[i] in s_set:
        print(s[i]*(2020-s[i]))
    s_set.add(s[i])

s_set = set()
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if 2020 - s[i] - s[j] in s_set:
            print(s[i]*s[j]*(2020-s[i]-s[j]))
    s_set.add(s[i])
