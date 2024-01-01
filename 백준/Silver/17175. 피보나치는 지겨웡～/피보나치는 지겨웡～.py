# 파보나치 지겨워
'''
0 1 2 3 4
1 1 3 5 9
'''
import sys

n = int(sys.stdin.readline())

dp = [1 for _ in range(n + 1)]

for i in range(2, n + 1):
    dp[i] = (dp[i-1] + dp[i-2] + 1) % 1000000007

print(dp[n])
