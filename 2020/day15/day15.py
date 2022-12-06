s = list(map(int,"5,2,8,16,18,0,1".split(",")))

speak = []
for i in s:
    speak.append(i)

while len(speak) < 2020:
    last = speak[-1]
    if last not in speak[:-1]:
        speak.append(0)
    else:
        speak.append(speak[:-1][::-1].index(last) + 1)

print(speak[-1])

def say(last, i, n):
    if n not in last:
        last[n] = (-1, i)
    else:
        pr = last[n][1]
        last[n] = (pr, i)
    return n

last = {}
prev = -1
for i in range(30000000):
    if i < len(s):
        prev = say(last, i, s[i])
    else:
        if last[prev][0] == -1:
            prev = say(last, i, 0)
        else:
            newn = last[prev][1] - last[prev][0]
            prev = say(last, i, newn)

print(prev)
        
