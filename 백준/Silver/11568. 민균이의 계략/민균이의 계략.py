import sys

n = int(sys.stdin.readline())

card = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(n)]

for i in range(1,n):
    max_value = 0
    for j in range(i):
        if card[j] < card[i]:
            max_value = max(max_value, dp[j])
        
    dp[i] = max_value + 1

print(max(dp))