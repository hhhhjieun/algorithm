# 동전2
'''
     1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
1    1 2 3 4
5            1 2 3 4 5 2  3     2  3  3
12                           1

'''
import sys

n, k = map(int, sys.stdin.readline().split())

coins = list(int(sys.stdin.readline()) for _ in range(n))
coins.sort()

dp = [100000] * (k + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

# 못만드는 경우
if dp[k] == 100000:
    print(-1)

else:
    print(dp[k])
