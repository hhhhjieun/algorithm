# 수들의 합2
import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

ans = 0
start, end = 0, 1

while end <= N and start <= end:

    tmp = sum(arr[start:end])

    if tmp == M:
        ans += 1
        end += 1

    elif tmp < M:
        end += 1

    else:
        start += 1

print(ans)