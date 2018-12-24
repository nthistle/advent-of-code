with open("input.txt") as file:
    inp = file.read().strip().replace("points with","points () with")

types = ['slashing', 'fire', 'bludgeoning', 'radiation', 'cold']

def parse_dmg(ss):
    dtype = ss[ss.rfind(" ")+1:]
    dnum = int(ss[:ss.rfind(" ")])
    return [0 if ty != dtype else dnum for ty in types]

def parse_res(ss):
    tp = [1, 1, 1, 1, 1]
    for p in ss.split("; "):
        if len(p) == 0:
            continue
        mul = 1
        if p[:4] == "weak":
            mul = 2
            p = p[8:]
        elif p[:6] == "immune":
            mul = 0
            p = p[10:]
        for dt in p.split("&"):
            tp[types.index(dt)] = mul
    return tp

vals = inp.split("\n\n")
immune = vals[0]
infect = vals[1]
immune = [s.replace(", ","&").replace(" units each with ",",").replace(" hit points (",",").replace(") with an attack that does ",",").replace(" damage at initiative ",",") for s in immune.split("\n")[1:]]
infect = [s.replace(", ","&").replace(" units each with ",",").replace(" hit points (",",").replace(") with an attack that does ",",").replace(" damage at initiative ",",") for s in infect.split("\n")[1:]]

def info(v):
    v = v.split(",")
    dmg = parse_dmg(v[3])
   # return [int(v[0]),int(v[1]),parse_res(v[2]),dmg,int(v[4]),int(v[0])*max(dmg)]
    return [int(v[0]),int(v[1]),parse_res(v[2]),dmg,int(v[4]),0]

immune = list(map(info, immune))
infect = list(map(info, infect))


def calc_dmg(ak,df):
    return sum(a*b for a,b in zip(ak[3],df[2]))

##DEBUG
#immune.append([935, 10231, [0, 1, 1, 1, 0], [0, 0, 103, 0, 0], 50, 0])

def run_combat(immune,infect):

    itc = 0
    while len(immune) > 0 and len(infect) > 0:
        #if itc % 10 == 0:
        #    print(itc, len(immune),len(infect))
        itc += 1
        # targeting
        for i in immune:
            i[-1] = i[0] * max(i[3])
        for i in infect:
            i[-1] = i[0] * max(i[3])
        immune.sort(key=lambda v : 1000*(-v[-1])-v[-2])
        infect.sort(key=lambda v : 1000*(-v[-1])-v[-2])
        
        im_tgs = []
        for ak in immune:
            best_choice = (0, 100000000, 0, None) # damage we'd do, eff power of target, tg_init, target_idx
            #best_choice = (-10000, 0, 0, None) # damage we'd do, eff power of target, tg_init, target_idx
            for idx, df in enumerate(infect):
                if idx in im_tgs:
                    continue
                tc = (calc_dmg(ak, df), df[-1], df[-2], idx)
                if tc > best_choice:
                    best_choice = tc
            im_tgs.append(best_choice[3])
            
        if_tgs = []
        for ak in infect:
            best_choice = (0, 100000000, 0, None) # damage we'd do, eff power of target, tg_init, target_idx
            #best_choice = (-10000, 0, 0, None) # damage we'd do, eff power of target, tg_init, target_idx
            for idx, df in enumerate(immune):
                if idx in if_tgs:
                    continue
                tc = (calc_dmg(ak, df), df[-1], df[-2], idx)
                if tc > best_choice:
                    best_choice = tc
            if_tgs.append(best_choice[3])

        all_units = []
        for i,v in enumerate(immune):
            all_units.append([0, i, v])
        for i,v in enumerate(infect):
            all_units.append([1, i, v])

        all_units.sort(key=lambda v : -v[2][-2])
        
        alive_immune = immune[:]
        alive_infect = infect[:]

        #print(infect[0])

        total_deathtoll = 0

        for unit in all_units:
            if unit[0] == 0: # it's immune
                if unit[2] not in alive_immune:
                    continue
                if im_tgs[unit[1]] is None:
                    continue
                taken_damage = unit[2][0] * calc_dmg(unit[2],infect[im_tgs[unit[1]]])
                death_toll = (taken_damage)//infect[im_tgs[unit[1]]][1]
                #print("immune dealing dmg =",taken_damage,"killing",death_toll)
                infect[im_tgs[unit[1]]][0] -= death_toll
                total_deathtoll += death_toll
                if infect[im_tgs[unit[1]]][0] <= 0:
                    alive_infect.remove(infect[im_tgs[unit[1]]])
            else: # it's infect
                if unit[2] not in alive_infect:
                    continue
                if if_tgs[unit[1]] is None:
                    continue
                taken_damage = unit[2][0] * calc_dmg(unit[2],immune[if_tgs[unit[1]]])
                death_toll = (taken_damage)//immune[if_tgs[unit[1]]][1]
                #print("infect dealing dmg =",taken_damage,"killing",death_toll)
                immune[if_tgs[unit[1]]][0] -= death_toll
                total_deathtoll += death_toll
                if immune[if_tgs[unit[1]]][0] <= 0:
                    alive_immune.remove(immune[if_tgs[unit[1]]])

        ## Stalemate
        if total_deathtoll == 0:
            return False
        
        immune = alive_immune
        infect = alive_infect

    return tuple(map(lambda w : sum(v[0] for v in w), [infect,immune]))

def dcopy(m):
    if type(m) is list:
        return [dcopy(d) for d in m]
    else:
        return m
    
def rboost(b):
    im_copy = dcopy(immune) #[ccopy(c) for c in immune]
    if_copy = dcopy(infect) #[ccopy(c) for c in infect]
    for i in im_copy:
        i[3][max(enumerate(i[3]),key=lambda v : v[1])[0]] += b
    return run_combat(im_copy, if_copy)

print("Part 1:",run_combat(dcopy(immune),dcopy(infect))[0])

low = 1
high = 100
while high > low:
    mid = (high+low)//2
    res = rboost(mid)
    if res == False or res[1] == 0:
        low = mid + 1
    else:
        high = mid

print("Part 2:",rboost(high)[1])
