
def get_input():
    with open("input.txt") as f:
        s = f.read().strip()
    lines = s.split("\n")
    print(f"num lines = {len(lines)}")
    total_length = sum(len(line) for line in lines)
    print(f"avg line length = {round(total_length/len(lines),2)}")
    return s

def grid(s, split = None):
    if split is None:
        split = lambda line : list(line)
    s = s.split("\n")
    n = len(s)
    g = [split(line) for line in s]
    m = len(g[0])
    return n, m, g
    
