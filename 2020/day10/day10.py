with open("input.txt") as f:
    s = f.read().strip()

nums = [int(x) for x in s.split("\n")]
nums.append(0)
nums.append(max(nums)+3)

nums.sort()

c3 = sum(1 for i in range(1,len(nums)) if nums[i] - nums[i-1] == 3)
c1 = sum(1 for i in range(1,len(nums)) if nums[i] - nums[i-1] == 1)

print(c1*c3)

cnts = [0]*(len(nums))

cnts[0] = 1
for i in range(1,len(cnts)):
    for j in range(0,i):
        if nums[i] - nums[j] <= 3:
            cnts[i] += cnts[j]

print(cnts[-1])
