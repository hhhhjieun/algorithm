# 세수의 합
import sys
N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline().strip()) for _ in range(N)]

nums.sort()

arr_sum = set()
for x in nums:
    for y in nums:
        arr_sum.add(x+y)


def check():
    global answer
    for i in range(N-1, -1, -1):
        for j in range(i+1):
            if nums[i]-nums[j] in arr_sum:
                answer = nums[i]
                return

answer = 0
check()
print(answer)