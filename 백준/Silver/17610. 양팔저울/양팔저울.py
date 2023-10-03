# 양팔 저울
import sys


def recur(cnt, total):
    global n

    if total > n:
        return

    if cnt == k:
        if 0 < total <= n:
            nums[total] = 1

    else:
        recur(cnt+1, total+weight[cnt])
        recur(cnt+1, total-weight[cnt])
        recur(cnt+1, total)


k = int(sys.stdin.readline())
weight = list(map(int, sys.stdin.readline().split()))

n = sum(weight)

weight.sort()

nums = [0] * (n+1)
recur(0, 0)
# print(nums)
nums.remove(0)

ans = 0

for i in range(len(nums)):
    if nums[i] == 0:
        ans += 1

print(ans)

