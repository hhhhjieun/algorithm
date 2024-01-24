# 점프 점프
import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))

dp = [0] + [100000] * (N-1)

for i in range(N):
    if arr[i] > 0:
        for j in range(arr[i]+1):
            if i + j < N:
                dp[i+j] = min(dp[i+j], dp[i]+1)
    else:
        continue
if dp[N-1] == 100000:
    print(-1)
else:
    print(dp[N-1])