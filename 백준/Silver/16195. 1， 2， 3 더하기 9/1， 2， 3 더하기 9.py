import sys

T = int(sys.stdin.readline())

d = [[0] * 1001 for _ in range(1001)]
d[1][1] = 1
d[2][1] = 1
d[2][2] = 1
d[3][1] = 1
d[3][2] = 2
d[3][3] = 1

for i in range(4, 1001):
        for j in range(2, i+1):
            d[i][j] += (d[i-1][j-1] % 1000000009 + d[i-2][j-1] % 1000000009 + d[i-3][j-1] % 1000000009) % 1000000009


for _ in range(T):
  n, m = map(int, sys.stdin.readline().split())

  ans = 0
  for i in range(1, m + 1):
    ans = (ans % 1000000009 + d[n][i] % 1000000009) % 1000000009
  print(ans)
