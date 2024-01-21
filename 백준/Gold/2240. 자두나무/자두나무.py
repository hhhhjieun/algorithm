# 자두나무
'''
   0  1  2 (이동횟수)
0  0  0  0
1  0  1  0
2  1  1  2
3  2  1  3
4  2  3  3
5  2  4  3

dp를 2차원 배열로 생각하기
'''
import sys

T, W = map(int, sys.stdin.readline().split())

tree = [0] + list(int(sys.stdin.readline()) for _ in range(T))

dp = [[0] * (W + 1) for _ in range(T + 1)]

for i in range(T + 1):
  # 1번 나무에서 한 번도 안움직이면
  # 1번에서 떨어짐
  if tree[i] == 1:
    dp[i][0] = dp[i-1][0] + 1

  # 2번에서 떨어짐
  if tree[i] == 2:
    dp[i][0] = dp[i-1][0]

  # 1번 이상 움직임
  for j in range(1, W + 1):
    # i초에 2번에서 떨어지고, 현재 2번에 서있으면,
    if tree[i] == 2 and j % 2 == 1:
      # 이전 위치로부터 움직여서 받아 먹을 것인지, 현재에서 받을것인지 비교
      dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1

    # i초에 1번에서 떨어지고, 현재 1번에 서있으면,
    elif tree[i] == 1 and j % 2 == 0:
      dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1

    else:
      dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[T]))


