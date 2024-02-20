# 배열 복원하기
'''
A : H X W
B : (H + X) x (W + Y)
(i, j)가 두 배열 모두에 포함되지 않으면, Bi,j = 0이다.
(i, j)가 두 배열 모두에 포함되면, Bi,j = Ai,j + Ai-X,j-Y이다.
(i, j)가 두 배열 중 하나에 포함되면, Bi,j = Ai,j 또는 Ai-X,j-Y이다.
'''
import sys

H, W, X, Y = map(int, sys.stdin.readline().split())
arr_A = []
arr_B = [list(map(int, sys.stdin.readline().split())) for _ in range(H + X)]

for i in range(H):
    arr_A.append(arr_B[i][:W])

for i in range(H):
    for j in range(W):
        if i + X < H and j + Y < W:
            arr_A[i + X][j + Y] -= arr_A[i][j]

for i in range(H):
    for j in range(W):
        print(arr_A[i][j], end=' ')
    print()