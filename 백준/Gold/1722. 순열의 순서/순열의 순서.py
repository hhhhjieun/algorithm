# 순열의 순서
import sys
import itertools

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x - 1)

if arr[0] == 1:
    K = arr[1]
    nums = list(range(1, N + 1))
    tmp = []

    for i in range(N, 0, -1):
        fac = factorial(i - 1)
        step = (K - 1) // fac
        tmp.append(nums[step])

        del nums[step]
        K -= fac * step
    print(*tmp)

else:
    arr2 = arr[1:]
    nums = list(range(1, N + 1))
    K = 1
    for i in range(N, 0, -1):
        fac = factorial(i - 1)
        step = nums.index(arr2[N - i])
        del nums[step]
        K += fac * step

    print(K)