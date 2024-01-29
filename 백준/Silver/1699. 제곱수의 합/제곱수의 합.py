# 제곱수의 합
import sys

N = int(sys.stdin.readline())

dp = [i for i in range(N + 1)]

for i in range(2, N + 1):
    for j in range(1, i + 1):
        ans = j * j
        if ans > i:
            break

        if dp[i] > dp[i - ans] + 1:
            dp[i] = dp[i - ans] + 1

print(dp[N])