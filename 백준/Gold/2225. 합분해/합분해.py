# 합분해
'''
0~N 까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수
순서 o, 한 개의 수 여러번 사용 가능

k/n  1   2   3   4   5   6
1    1   1   1   1   1   1
2    2   3   4   5   6   7
3    3   6  10  15  21  28
4    4  10  20  35  56  84
5    5  15  35  70 126

'''
import sys

N, K = map(int, sys.stdin.readline().split())

dp = [[0] * 201 for _ in range(201)]

# 첫번째 칸, 두번째 칸 채워주기
for i in range(201):
    dp[1][i] = 1
    dp[2][i] = i + 1

for i in range(2, 201):
    dp[i][1] = i
    for j in range(2, 201):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

print(dp[K][N])
