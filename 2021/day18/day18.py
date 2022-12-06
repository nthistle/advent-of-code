from collections import defaultdict, Counter
import regex
import itertools

nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    s = f.read().strip().split("\n")

def convert(s):
    r = []
    for c in s:
        if c == ",":
            continue
        elif c in "[]":
            r.append(c)
        else:
            r.append(int(c))
    return r

def deconv(sfnum):
    s = []
    for c in sfnum:
        s.append(str(c))
        if str(c) not in "[,":
            s.append(",")
    return eval("".join(s[:-1]))
        

def explode(sfnum):
    depth = 0
    explode_idx = -1
    for i, ch in enumerate(sfnum):
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
        else:
            if depth == 5 and explode_idx == -1:
                explode_idx = i
    if explode_idx != -1:
        left = sfnum.pop(explode_idx)
        right = sfnum[explode_idx]
        sfnum[explode_idx] = 0
        del sfnum[explode_idx + 1] # "]"
        del sfnum[explode_idx - 1] # "["
        for j in range(explode_idx - 2, -1, -1):
            if type(sfnum[j]) is int:
                sfnum[j] += left
                break
        for k in range(explode_idx, len(sfnum)):
            if type(sfnum[k]) is int:
                sfnum[k] += right
                break
        return True
    else:
        return False

def split(sfnum):
    reduce_idx = -1
    for i, ch in enumerate(sfnum):
        if type(ch) is int and ch >= 10 and reduce_idx == -1:
            reduce_idx = i
    if reduce_idx != -1:
        reduce_value = sfnum[reduce_idx]
        left = reduce_value // 2
        right = (reduce_value + 1) // 2
        sfnum[reduce_idx] = left
        sfnum.insert(reduce_idx + 1, right)
        sfnum.insert(reduce_idx + 2, "]")
        sfnum.insert(reduce_idx, "[")
        return True
    else:
        return False

def reduce(sfnum):
    while True:
        if not explode(sfnum):
            if not split(sfnum):
                break
    return sfnum

def magn(c):
    if type(c) is int:
        return c
    else:
        return 3 * magn(c[0]) + 2 * magn(c[1])

d = [convert(line) for line in s]
##cur = d.pop(0)
##for nd in d:
##    cur = ["[",*cur,*nd,"]"]
##    reduce(cur)
##print(deconv(cur))
##print(magn(deconv(cur)))

print(max( \
    magn(deconv(reduce(["[",*d[i],*d[j],"]"]))) \
    for i in range(len(d)) for j in range(len(d)) \
    if i != j))



##d = [eval(r) for r in s]
##
##cur = []
##cur.append(d.pop(0))
##cur.append(d.pop(0))

# True, left, right
##def explode(c,depth=0):
##    if depth == 4:
##        return True, True, None, c[0], c[1]
##    nc = []
##
##    addr = 0
##    mhase = False
##    writel = 0
##    for x in c:
####        print("c=",c,"x=",x,"r=",addr)
##        if type(x) is int:
##            nc.append(x + addr)
##            addr = 0
####            print("zeroing addr")
##        else:
##            if not mhase:
##                ret, hase, sv, l, r = explode(x, depth+1)
##            else:
##                ret, hase, sv, l, r = \
##                     False, mhase, x, writel, 0
##            mhase = mhase or hase
##            
##            if l > 0:
##                if len(nc) > 0:
##                    val = nc
##                    while type(val[-1]) is list:
##                        val = val[-1]
##                    val[-1] += l
##                    writel = 0
##                else:
##                    writel = l
##            
##            if not ret: # no explosion
##                cx = sv
##                while type(cx[0]) is list:
##                    cx = cx[0]
##                cx[0] += addr
##                addr = 0
##                nc.append(sv)
##            else:
####                print(nc,x,l,r)
##                # need to add l to top of nc
####                if len(nc) > 0:
####                    print("attempting to write l")
####                    val = nc
####                    while type(val[-1]) is list:
####                        val = val[-1]
####                    val[-1] += l
####                else:
####                    writel = l
##                nc.append(0)
##                #addr = r
##            addr = r
##    return False, mhase, nc, writel, addr
##
##
### hass, nc
##def split(c):
##    nc = []
##    hassp = False
##    for x in c:
##        if type(x) is list:
##            if not hassp:
##                hass, sv = split(x)
##            else:
##                hass, sv = hassp, x
##            hassp = hassp or hass
##            nc.append(sv)
##        else:
##            if not hassp and x >= 10:
##                np = [x//2, (x+1)//2]
##                hassp = True
##                nc.append(np)
##            else:
##                nc.append(x)
##    return hassp, nc
##    
##
##def reduce(c):
##    while True:
##        #print(c)
##        _, exp, c, _, _ = explode(c)
##        if not exp:
##            spl, c = split(c)
##            if not spl:
##                break
##    return c
##
##def magn(c):
##    if type(c) is int:
##        return c
##    else:
##        return 3 * magn(c[0]) + 2 * magn(c[1])

##cur = reduce(cur)
##print(cur)
##for x in d:
##    cur = reduce([cur, x])
##    print(cur)
##print(cur)
##
##print(magn(cur))              
