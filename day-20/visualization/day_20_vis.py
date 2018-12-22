import sys
import numpy as np
from PIL import Image
import cv2

from colorsys import hls_to_rgb

def rgb_to_bgr(c):
    return (np.uint8(255*c[2]),np.uint8(255*c[1]),np.uint8(255*c[0]))

## Note: After running, run `ffmpeg -i vis.mp4 Day_20_Visualization.mp4`
## to properly compress the video

with open("../input.txt") as file:
    inp = file.read().strip()

path = inp[1:-1]
mp = [["#" for i in range(2000)] for j in range(2000)]
in_map = lambda c : c[0] in range(len(mp)) and c[1] in range(len(mp[c[0]]))

drs = {"N":(-1,0),"S":(1,0),"W":(0,-1),"E":(0,1)}

stack = []

global fc
fc = 0

im = np.zeros((800,800,3),dtype=np.uint8)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
clip_writer = cv2.VideoWriter("vis.mp4", fourcc, 60, (800, 800))

col = rgb_to_bgr(hls_to_rgb( 0,0.6,1.0 ))
x_offset = 895
y_offset = 901
im_x = (1000-x_offset)
im_y = (1000-y_offset)
im[4*im_x:4*im_x+4,4*im_y:4*im_y+4] = col

def update_frame():
    global fc
    fc += 1
    if fc % 100 == 0:
        print(fc)
    if fc % 5 == 0:
        clip_writer.write(im)

def dfs(co, pto):
    stack.append((co, pto))
    seen = set()
    while len(stack) > 0:
        cur = stack.pop(-1)
        c = cur[0]
        pt = cur[1]
        if (c[0],c[1],pt) in seen:
            continue
        seen.add((c[0],c[1],pt))
        if len(cur[1]) == 0:
            continue
        if cur[1][0] == "(":
            r_s = 1
            r_i = 1
            while r_s > 0:
                if pt[r_i] == "(":
                    r_s += 1
                elif pt[r_i] == ")":
                    r_s -= 1
                r_i += 1
            group = pt[1:r_i-1]
            opts = []
            r_s2 = 0
            r_i2 = 0
            lc = 0
            while r_s2 >= 0 and r_i2 < len(group):
                if group[r_i2] == "(":
                    r_s2 += 1
                elif group[r_i2] == ")":
                    r_s2 -= 1
                if r_s2 == 0 and group[r_i2] == "|":
                    opts.append(group[lc:r_i2])
                    lc = r_i2 + 1
                r_i2 += 1
            opts.append(group[lc:])
            for poss in opts:
                stack.append((c, poss + pt[r_i:]))
        else:
            bf = pt.find("(")
            if bf == -1:
                bf = len(pt)
            cloc = [c[0],c[1]]
            for b in range(bf):
                tdr = pt[b]
                mp[cloc[0]+drs[tdr][0]][cloc[1]+drs[tdr][1]] = "|" if tdr in "WE" else "-"
                mp[cloc[0]+2*drs[tdr][0]][cloc[1]+2*drs[tdr][1]] = "."

                x_offset = 895
                y_offset = 901
                im_x = (cloc[0]+drs[tdr][0]-x_offset)
                im_y = (cloc[1]+drs[tdr][1]-y_offset)
                im[4*im_x:4*im_x+4,4*im_y:4*im_y+4] = (255,255,255)
                im_x = (cloc[0]+2*drs[tdr][0]-x_offset)
                im_y = (cloc[1]+2*drs[tdr][1]-y_offset)
                im[4*im_x:4*im_x+4,4*im_y:4*im_y+4] = (255,255,255)
                
                update_frame()
                
                cloc[0] += 2*drs[tdr][0]
                cloc[1] += 2*drs[tdr][1]
            stack.append((cloc,pt[bf:]))


def vis(n):
    print("\n".join("".join(c[1000-n:1000+n]) for c in mp[1000-n:1000+n]))

mp[1000][1000] = "X"

dfs((1000,1000), path)
print("DFS done")

for i in range(30):
    update_frame()

#now find farthest
cur = (1000,1000)
import queue
q = queue.Queue()
q.put((cur,0))
furthest = 0
far_count = 0
itc = 0
while not q.empty():
    if itc % 3 == 0:
        update_frame()
    cur = q.get()
    if cur[1] > furthest:
        furthest = cur[1]
    if cur[1] >= 1000:
        far_count += 1
    dist = cur[1]
    cur = cur[0]
    mp[cur[0]][cur[1]] = "v"
    for d in [(-1,0),(1,0),(0,-1),(0,1)]:
        if mp[cur[0]+d[0]][cur[1]+d[1]] in "-|": #traversable
            if mp[cur[0]+2*d[0]][cur[1]+2*d[1]] != "v":
                mp[cur[0]+2*d[0]][cur[1]+2*d[1]] = "v"
                q.put(((cur[0]+2*d[0],cur[1]+2*d[1]),dist+1))

                col = rgb_to_bgr(hls_to_rgb( (dist+1)/4000,0.6,1.0 ))
                x_offset = 895
                y_offset = 901
                im_x = (cur[0]+d[0]-x_offset)
                im_y = (cur[1]+d[1]-y_offset)
                im[4*im_x:4*im_x+4,4*im_y:4*im_y+4] = col
                im_x = (cur[0]+2*d[0]-x_offset)
                im_y = (cur[1]+2*d[1]-y_offset)
                im[4*im_x:4*im_x+4,4*im_y:4*im_y+4] = col
    itc += 1

for i in range(60):
    update_frame()

clip_writer.release()

print("Part 1:",furthest)
print("Part 2:",far_count)
