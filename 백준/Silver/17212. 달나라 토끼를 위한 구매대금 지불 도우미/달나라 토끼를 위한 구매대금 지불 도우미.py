# 달나라 토끼
'''
1, 2, 5, 7

1 2 3 4 5 6 7   8 9 10 11 12 13 14   15 16 17 18 19 20 21
1 1 2 2 1 2 1   2 2  2 3  2  3  2    3  3  3  4  3  4  3

'''
import sys

n = int(sys.stdin.readline())
dp = [i for i in range(n+1)]

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i >= 2:
        dp[i] = min(dp[i], dp[i - 2] + 1)
    if i >= 5:
        dp[i] = min(dp[i], dp[i - 5] + 1)
    if i >= 7:
        dp[i] = min(dp[i], dp[i - 7] + 1)

print(dp[n])
