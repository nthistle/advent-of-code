with open("input.txt") as file:
    inp = file.read()[:-1]
    
mat = [list(line) for line in inp.split("\n")]
carts = []
cart_types = {"^":"|","v":"|",">":"-","<":"-"}
dir_types = {"^":(0,-1),"v":(0,1),">":(1,0),"<":(-1,0)}
dir_change = {"^":"<^>","v":">v<",">":"^>v","<":"v<^"}
dir_tch = {"^/" :">", ">/":"^", "v/":"<", "</":"v",
           "^\\":"<",">\\":"v","v\\":">","<\\":"^"}

for y,line in enumerate(mat):
    for x,c in enumerate(line):
        if c in cart_types:
            carts.append([c,0,x,y])
            
for cart in carts:
    mat[cart[3]][cart[2]] = cart_types[cart[0]]

already_moved = []
not_moved = carts

ich = 0
first_col = True
while True:
    ich += 1
    not_moved.sort(key=lambda c : 100000*c[3] + c[2])
    col_coords = {}
    for cart in not_moved:
        col_coords[(cart[2],cart[3])] = None
    while len(not_moved) > 0:
        cart = not_moved.pop(0)
        col_coords.pop((cart[2],cart[3]))
        cart[2] += dir_types[cart[0]][0]
        cart[3] += dir_types[cart[0]][1]
        if mat[cart[3]][cart[2]] in "/\\":
            cart[0] = dir_tch[cart[0]+mat[cart[3]][cart[2]]]
        elif mat[cart[3]][cart[2]] == "+":
            cart[0] = dir_change[cart[0]][cart[1]%3]
            cart[1] += 1
        has_col = False
        if (cart[2],cart[3]) in col_coords:
            if first_col:
                print("Part 1:",*cart[2:])
                first_col = False
            has_col = True
        if not has_col:
            col_coords[(cart[2],cart[3])] = None
            already_moved.append(cart)
        else:
            loc_col = False
            i = 0
            while i < len(not_moved) and not loc_col:
                if not_moved[i][2:] == cart[2:]:
                    loc_col = True
                    not_moved.pop(i)
                i += 1
            if not loc_col:
                i = 0
                while i < len(already_moved) and not loc_col:
                    if already_moved[i][2:] == cart[2:]:
                        loc_col = True
                        already_moved.pop(i)
                    i += 1
        
    not_moved = already_moved
    already_moved = []

    if len(not_moved) == 1:
        print("Part 2:",*not_moved[0][2:])
        break
