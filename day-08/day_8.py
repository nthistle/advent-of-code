with open("input.txt") as file:
    inp = file.read().strip()

inp = list(map(int,inp.split(" ")))
data = inp.copy()

global total_meta
total_meta = 0

def gen_node(dat):
    global total_meta
    num_child = dat.pop(0)
    num_meta = dat.pop(0)
    children = []
    for _ in range(num_child):
        children.append(gen_node(dat))
    meta = []
    for _ in range(num_meta):
        meta.append(dat.pop(0))
        total_meta += meta[-1]
    return (children, meta)

tree = gen_node(data)
print("Part 1:",total_meta)

def get_value(node):
    if len(node[0]) == 0:
        return sum(node[1])
    else:
        return sum(get_value(node[0][n-1]) for n in node[1] if n <= len(node[0]))

print("Part 2:",get_value(tree))
