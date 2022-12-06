from collections import defaultdict, Counter
import regex
import itertools
import numpy as np

mats = [[[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[1, 0, 0], [0, 0, -1], [0, 1, 0]], [[1, 0, 0], [0, -1, 0], [0, 0, -1]], [[1, 0, 0], [0, 0, 1], [0, -1, 0]], [[0, -1, 0], [1, 0, 0], [0, 0, 1]], [[0, 0, 1], [1, 0, 0], [0, 1, 0]], [[0, 1, 0], [1, 0, 0], [0, 0, -1]], [[0, 0, -1], [1, 0, 0], [0, -1, 0]], [[-1, 0, 0], [0, -1, 0], [0, 0, 1]], [[-1, 0, 0], [0, 0, -1], [0, -1, 0]], [[-1, 0, 0], [0, 1, 0], [0, 0, -1]], [[-1, 0, 0], [0, 0, 1], [0, 1, 0]], [[0, 1, 0], [-1, 0, 0], [0, 0, 1]], [[0, 0, 1], [-1, 0, 0], [0, -1, 0]], [[0, -1, 0], [-1, 0, 0], [0, 0, -1]], [[0, 0, -1], [-1, 0, 0], [0, 1, 0]], [[0, 0, -1], [0, 1, 0], [1, 0, 0]], [[0, 1, 0], [0, 0, 1], [1, 0, 0]], [[0, 0, 1], [0, -1, 0], [1, 0, 0]], [[0, -1, 0], [0, 0, -1], [1, 0, 0]], [[0, 0, -1], [0, -1, 0], [-1, 0, 0]], [[0, -1, 0], [0, 0, 1], [-1, 0, 0]], [[0, 0, 1], [0, 1, 0], [-1, 0, 0]], [[0, 1, 0], [0, 0, -1], [-1, 0, 0]]]
mats = [np.array(x) for x in mats]

nums_regex = regex.compile("([^\\d]*)((?P<nums>\\d+)([^\\d]*))*")

def nums(s):
    m = nums_regex.match(s)
    vals = m.capturesdict()["nums"]
    return [int(x) for x in vals]

with open("input.txt") as f:
    s = f.read().strip().split("\n\n")

##s = """--- scanner 0 ---
##404,-588,-901
##528,-643,409
##-838,591,734
##390,-675,-793
##-537,-823,-458
##-485,-357,347
##-345,-311,381
##-661,-816,-575
##-876,649,763
##-618,-824,-621
##553,345,-567
##474,580,667
##-447,-329,318
##-584,868,-557
##544,-627,-890
##564,392,-477
##455,729,728
##-892,524,684
##-689,845,-530
##423,-701,434
##7,-33,-71
##630,319,-379
##443,580,662
##-789,900,-551
##459,-707,401
##
##--- scanner 1 ---
##686,422,578
##605,423,415
##515,917,-361
##-336,658,858
##95,138,22
##-476,619,847
##-340,-569,-846
##567,-361,727
##-460,603,-452
##669,-402,600
##729,430,532
##-500,-761,534
##-322,571,750
##-466,-666,-811
##-429,-592,574
##-355,545,-477
##703,-491,-529
##-328,-685,520
##413,935,-424
##-391,539,-444
##586,-435,557
##-364,-763,-893
##807,-499,-711
##755,-354,-619
##553,889,-390
##
##--- scanner 2 ---
##649,640,665
##682,-795,504
##-784,533,-524
##-644,584,-595
##-588,-843,648
##-30,6,44
##-674,560,763
##500,723,-460
##609,671,-379
##-555,-800,653
##-675,-892,-343
##697,-426,-610
##578,704,681
##493,664,-388
##-671,-858,530
##-667,343,800
##571,-461,-707
##-138,-166,112
##-889,563,-600
##646,-828,498
##640,759,510
##-630,509,768
##-681,-892,-333
##673,-379,-804
##-742,-814,-386
##577,-820,562
##
##--- scanner 3 ---
##-589,542,597
##605,-692,669
##-500,565,-823
##-660,373,557
##-458,-679,-417
##-488,449,543
##-626,468,-788
##338,-750,-386
##528,-832,-391
##562,-778,733
##-938,-730,414
##543,643,-506
##-524,371,-870
##407,773,750
##-104,29,83
##378,-903,-323
##-778,-728,485
##426,699,580
##-438,-605,-362
##-469,-447,-387
##509,732,623
##647,635,-688
##-868,-804,481
##614,-800,639
##595,780,-596
##
##--- scanner 4 ---
##727,592,562
##-293,-554,779
##441,611,-461
##-714,465,-776
##-743,427,-804
##-660,-479,-426
##832,-632,460
##927,-485,-438
##408,393,-506
##466,436,-512
##110,16,151
##-258,-428,682
##-393,719,612
##-211,-452,876
##808,-476,-593
##-575,615,604
##-485,667,467
##-680,325,-822
##-627,-443,-432
##872,-547,-609
##833,512,582
##807,604,487
##839,-516,451
##891,-625,532
##-652,-548,-490
##30,-46,-14""".split("\n\n")

sc = []
for slines in s:
    lines = slines.split("\n")
    locs = set()
    for line in lines[1:]:
        locs.add(eval(line))
    locs = np.array([x for x in locs])
    sc.append((nums(lines[0])[0], locs))

true_locs = set()
for b in sc[0][1]:
    true_locs.add(tuple(b))

scanner_locs = set()

def reorient(beacons,sx,sy,sz,idx):
    beacons = beacons @ mats[idx] # rotate
    beacons = beacons + np.array([[sx,sy,sz]])
    return beacons

# beacons are the transposed beacons
def align(idx,beacons,already_aligned,depth=0):
    global true_locs
    #print("called at idx =",idx)
    beacon1set = set(tuple(b) for b in beacons)
    for i in range(len(sc)):
        if i not in already_aligned:
            print("-"*depth+"trying to align",idx,"with",i)
            bigbreak = False
            for orient in range(24):
                beacon2s = sc[i][1] @ mats[orient]
                for b1x,b1y,b1z in beacons:
                    for b2x,b2y,b2z in beacon2s[:18]:
                        sx,sy,sz = b1x-b2x,b1y-b2y,b1z-b2z
                        beacon2s_tr = beacon2s + np.array([[sx,sy,sz]])
                        intersect = 0
                        for b in beacon2s_tr:
                            if tuple(b) in beacon1set:
                                intersect += 1
                        if intersect >= 12:
                            print("ALIGNING! i =",i)
                            for b in beacon2s_tr:
                                true_locs.add(tuple(b))
                            already_aligned.add(i)
                            align(i,beacon2s_tr,already_aligned,depth+1)
                            bigbreak = True
                            break
                    if bigbreak:
                        break
                if bigbreak:
                    break


align(0,sc[0][1],{0})
print(len(true_locs))

scanner_locs = []
scanner_locs.append((0,0,0))

for i in range(len(sc)):
    print("locating scanner",i)
    for orient in range(24):
        beacon2s = sc[i][1] @ mats[orient]
        for b1x,b1y,b1z in true_locs:
            b2x,b2y,b2z = beacon2s[0]
            sx,sy,sz = b1x-b2x,b1y-b2y,b1z-b2z
            beacon2s_tr = beacon2s + np.array([[sx,sy,sz]])
            intersect = 0
            for b in beacon2s_tr:
                if tuple(b) in true_locs:
                    intersect += 1
            if intersect == beacon2s.shape[0]:
                scanner_locs.append((sx,sy,sz))
                print(intersect)
                print(sx,sy,sz)
                print(orient)
            

md = 0
for i in range(len(scanner_locs)):
    for j in range(i+1,len(scanner_locs)):
        d = sum(abs(scanner_locs[i][k]-scanner_locs[j][k]) for k in range(3))
        md = max(d, md)
print(md)

##for i in range(1,len(sc)):
##    print("attempting",i)
##    # try to align sc[i] to sc[0]
##    beacon1set = set(tuple(b) for b in sc[0][1])
##    for orient in range(24):
##        beacon2s = sc[i][1] @ mats[orient]
##        for b1x,b1y,b1z in sc[0][1]:
##            for b2x,b2y,b2z in beacon2s:
##                sx,sy,sz = b1x-b2x,b1y-b2y,b1z-b2z
##                beacon2s_tr = beacon2s + np.array([[sx,sy,sz]])
##                intersect = 0
##                for b in beacon2s_tr:
##                    if tuple(b) in beacon1set:
##                        intersect += 1
##                if intersect > 1:
##                    print(intersect)
                
                
            

        
