# 가장 큰 증가하는 부분 수열
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))

dp = [0] * N
dp[0] = arr[0]

for i in range(1, N):
  for j in range(i):
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], dp[j] + arr[i])
    else:
      dp[i] = max(dp[i], arr[i])

print(max(dp))