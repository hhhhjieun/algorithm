# BOJ 거리
import sys

N = int(sys.stdin.readline())

boj = list(sys.stdin.readline().strip())

dp = [1000000000] * N

dp[0] = 0

for i in range(1, N):
    for j in range(i):
        if boj[j] == 'B' and boj[i] == 'O':
            dp[i] = min(dp[i], dp[j] + (i - j) ** 2)
        elif boj[j] == 'O' and boj[i] == "J":
            dp[i] = min(dp[i], dp[j] + (i - j) ** 2)
        elif boj[j] == 'J' and boj[i] == 'B':
            dp[i] = min(dp[i], dp[j] + (i - j) ** 2)

if dp[N-1] != 1000000000:
    print(dp[N-1])
else:
    print(-1)

