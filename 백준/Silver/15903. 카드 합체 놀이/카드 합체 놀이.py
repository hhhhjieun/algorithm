# 카드 합체 놀이
import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    arr.sort()
    mid = (arr[0] + arr[1])
    arr[0], arr[1] = mid, mid

print(sum(arr))

