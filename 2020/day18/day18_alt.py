with open("input.txt") as f:
    s = f.read().strip().split("\n")


# + => +
# * => -
class P1:
    def __init__(self, v):
        self.v = v

    def __add__(self, o):
        return P1(self.v + o.v)

    def __sub__(self, o):
        return P1(self.v * o.v)

ans = 0
for l in s:
    l = "".join("P1("+x+")" if x.isdigit() else x for x in l)
    l = l.replace("*","-")
    ans += eval(l).v
print(ans)

# + => *
# * => +
class P2:
    def __init__(self, v):
        self.v = v

    def __add__(self, o):
        return P2(self.v * o.v)

    def __mul__(self, o):
        return P2(self.v + o.v)

ans = 0
for l in s:
    l = "".join("P2("+x+")" if x.isdigit() else x for x in l)
    l = l.replace("*","?").replace("+","*").replace("?","+")
    ans += eval(l).v
print(ans)


