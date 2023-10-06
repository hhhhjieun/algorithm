# 음식물 피하기
'''
N, M : 통로의 세로, 가로 길이
K : 음식물 쓰레기의 개수
r, c : 음식물이 떨어진 좌표
인접한 것은 붙어서 크게 됨
'''
import sys
from collections import deque


N, M, K = map(int, sys.stdin.readline().split())

trash = [[0] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    trash[r-1][c-1] = 1


def find_trash(y, x):
    global cnt

    q = deque()
    q.append((y, x))



    while q:
        i, j = q.popleft()

        for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and trash[ni][nj] == 1:
                trash[ni][nj] = 0
                cnt += 1
                q.append((ni, nj))


max_trash = 0

for i in range(N):
    for j in range(M):
        if trash[i][j] == 1:
            trash[i][j] = 0
            cnt = 1
            find_trash(i, j)
            max_trash = max(max_trash, cnt)

print(max_trash)


