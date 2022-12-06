with open("input.txt") as f:
    s = f.read().strip().split("\n")

nums = [int(x) for x in s]

def valid(nums,n):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == n:
                return True
    return False

target = -1
for i in range(25,len(nums)):
    if not valid(nums[i-25:i], nums[i]):
        target = nums[i]
        print(target)
        break

sset = {}
rsum = 0

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if sum(nums[i:j+1]) == target:
            print(min(nums[i:j+1])+max(nums[i:j+1]))

for i in range(len(nums)):
    sset[rsum] = i
    rsum += nums[i]
    if rsum - target in sset:
        lo,hi = sset[rsum-target],i
        vals = nums[lo:hi+1]
        print(min(vals)+max(vals))
        break
