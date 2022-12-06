with open("input.txt") as f:
    s = f.read().strip().split("\n\n")

fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]#,"cid"]

def fdr(s,lo,hi):
    if len(s) != 4:
        return False
    if any(not c.isdigit() for c in s):
        return False
    return lo <= int(s) <= hi

c = 0
for p in s:
    try:
        p = p.replace("\n"," ").split(" ")
        pd = {}
        for f in p:
            pd[f[:f.find(":")]] = f[f.find(":")+1:]
        if not fdr(pd["byr"],1920,2002):
            continue
        if not fdr(pd["iyr"],2010,2020):
            continue
        if not fdr(pd["eyr"],2020,2030):
            continue
        hgt = pd["hgt"]
        if hgt[-2:] == "cm":
            if not (150 <= int(hgt[:-2]) <= 193):
                continue
        else:
            if hgt[-2:] != "in":
                continue
            if not (59 <= int(hgt[:-2]) <= 76):
                continue
        hcl = pd["hcl"]
        if len(hcl) != 7:
            continue
        if hcl[0] != "#":
            continue
        if any(c not in "0123456789abcdef" for c in hcl[1:]):
            continue
        if pd["ecl"] not in ["amb","blu","brn","gry","grn","hzl","oth"]:
            continue
        if len(pd["pid"]) != 9:
            continue
        if any(not c.isdigit() for c in pd["pid"]):
            continue
        c += 1
    except:
        pass
    #if all(f+":" in p for f in fields):
    #    c += 1
print(c)
