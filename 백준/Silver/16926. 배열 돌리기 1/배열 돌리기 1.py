# 배열 돌리기 1
import sys

N, M, R = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

T = min(N, M) // 2

for _ in range(R):
  for i in range(T):
    x, y = i, i
    tmp = arr[x][y]

    for j in range(i+1, N-i):
      x = j
      last = arr[x][y]
      arr[x][y] = tmp
      tmp = last

    for j in range(i+1, M-i):
      y = j
      last = arr[x][y]
      arr[x][y] = tmp
      tmp = last

    for j in range(i+1, N-i):
      x = N - j - 1
      last = arr[x][y]
      arr[x][y] = tmp
      tmp = last

    for j in range(i+1, M-i):
      y = M - j - 1
      last = arr[x][y]
      arr[x][y] = tmp
      tmp = last

for i in range(N):
  for j in range(M):
    print(arr[i][j], end=' ')
  print()