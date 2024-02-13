# 징검다리 건너기
import sys

N = int(sys.stdin.readline())

energy = [[0, 0]]

for _ in range(N-1):
    small, large = map(int, sys.stdin.readline().split())
    energy.append([small, large])

K = int(sys.stdin.readline())

dp = [0] * (N + 1)

if N == 1:
    print(0)
    exit()

elif N == 2:
    print(energy[1][0])
    exit()

dp[2] = energy[1][0]
dp[3] = min(energy[1][1], energy[1][0] + energy[2][0])

# K 사용
for i in range(4, N + 1):
    dp[i] = min(dp[i - 1] + energy[i - 1][0], dp[i - 2] + energy[i - 2][1])


min_energy = 9999999
for i in range(1, N - 2):
    dp2 = dp[:]
    if dp[i] + K < dp[i + 3]:
        dp2[i + 3] = dp2[i] + K
        for j in range(i + 4, N + 1):
            dp2[j] = min(dp2[j], dp2[j - 1] + energy[j - 1][0], dp2[j - 2] + energy[j - 2][1])

        min_energy = min(min_energy, dp2[-1])

if min_energy == 9999999:
    print(dp[-1])
else:
    print(min_energy)
