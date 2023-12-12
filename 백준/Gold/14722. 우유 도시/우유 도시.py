# 우유 도시
'''
0 > 1 > 2 > 0
동, 남으로만
'''
import sys

N = int(sys.stdin.readline())

milks = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(milks)

dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # print(dp)
        if dp[i][j] % 3 == milks[i-1][j-1]:
            dp[i][j] += 1

print(dp[-1][-1])