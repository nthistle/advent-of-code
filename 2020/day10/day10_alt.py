import numpy as np
import time

with open("input.txt") as f:
    s = f.read().strip()

nums = [int(x) for x in s.split("\n")]
nums.append(0)
nums.append(max(nums)+3)
#nums.sort()
m#nums[4] = 5

st = time.time()

f = lambda i, j : j > i and nums[j] - nums[i] <= 3
m = np.fromfunction(np.vectorize(f), (len(nums), len(nums)), dtype=np.int64).astype(np.int64)
m[len(nums)-1, len(nums)-1] = 1

aux = np.eye(len(nums))

aux = np.linalg.matrix_power(m, len(nums))
#ans = 0
#for _ in range(len(nums)):
#    aux = aux @ m
#    ans += aux[0, len(nums) - 1]

et = time.time()

ans = aux[0, len(nums) - 1]

print(ans)
print(et - st)
