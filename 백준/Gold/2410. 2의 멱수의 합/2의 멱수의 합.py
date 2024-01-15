# 2의 멱수
'''
1 1
2 2
3 2
4 4 (2+2)
5 4
6 6 (4+2)
7 6
8 10 (6+4)
9 10
10 14 (10+4)
11 14
'''

import sys

N = int(sys.stdin.readline())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

if N >= 3:
    for i in range(3, N+1):
        if i % 2 == 1:
            dp[i] = dp[i - 1]
        else:
            dp[i] = (dp[i-1] + dp[i//2]) % 1000000000

print(dp[N])
