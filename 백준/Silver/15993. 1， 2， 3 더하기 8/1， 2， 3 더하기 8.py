import sys
MOD = 1000000009
dp = [[0 for _ in range(2)] for _ in range(100001)]
dp[1][1] = 1
dp[2][0] = 1  # Even
dp[2][1] = 1  # Odd
dp[3][0] = 2
dp[3][1] = 2
for i in range(4, 100001):
    dp[i][0] = (dp[i-1][1] + dp[i-2][1] + dp[i-3][1]) % MOD
    dp[i][1] = (dp[i-1][0] + dp[i-2][0] + dp[i-3][0]) % MOD

n = int(sys.stdin.readline())
results = []
for _ in range(n):
    t = int(sys.stdin.readline())
    odd = dp[t][1] % MOD
    even = dp[t][0] % MOD
    results.append((odd, even))

for result in results:
    print(f"{result[0]} {result[1]}")
