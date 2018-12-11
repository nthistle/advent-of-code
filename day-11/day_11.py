import numpy as np

grid_serial = 6392

fuel = np.zeros((300,300))
rsum = np.zeros((301,301))

for i in range(300):
    for j in range(300):
        fuel[i,j] = (((i+11)*(j+1)+grid_serial)*(i+11))//100%10-5

for i in range(300):
    for j in range(300):
        rsum[i+1,j+1] += fuel[i,j]
        rsum[i+1,j+1] += rsum[i,j+1]
        rsum[i+1,j+1] += rsum[i+1,j]
        rsum[i+1,j+1] -= rsum[i,j]

calc_sum = lambda x,y,s,r : r[x+s,y+s]-r[x,y+s]-r[x+s,y]+r[x,y]

print("Part 1:",",".join(map(str,max(((x+1,y+1) for x in range(300-2) for y in range(300-2)), \
                    key=lambda p:calc_sum(p[0]-1,p[1]-1,3,rsum)))))
print("Part 2:",",".join(map(str,max(((x+1,y+1,s) for s in range(1,301) for x in range(300-s+1) \
                    for y in range(300-s+1)), key=lambda p:calc_sum(p[0]-1,p[1]-1,p[2],rsum)))))
