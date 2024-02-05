# 도로의 개수
import sys
N, M = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

dp = [[0] * (M + 2) for _ in range(N + 2)]
dp[1][1] = 1

construction_site = set()
end = set()

if K > 0:
    for _ in range(K):
        a, b, c, d = map(int, sys.stdin.readline().split())
        (a, b), (c, d) = sorted([(a + 1, b + 1), (c + 1, d + 1)])
        end.add((c, d))
        construction_site.add((a, b, c, d))

for i in range(1, N + 2):
    for j in range(1, M + 2):
        if i == 1 and j == 1:
            continue

        if (i, j) in end:
            if (i-1, j, i, j) not in construction_site:
                dp[i][j] = dp[i-1][j]
            elif (i, j-1, i, j) not in construction_site:
                dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[N+1][M+1])