# 양치기 꿍
'''
빈 공간 .
울타리  #
늑대 v
양 k
k > v 일때만 늑대가 전부 잡아먹힘
'''
import sys
from collections import deque


def fox_sheep(y, x):
    global sheep_cnt, fox_cnt
    q = deque()
    q.append((y, x))
    visited[y][x] = 1

    sheep, fox = 0, 0

    while q:
        i, j = q.popleft()

        if arr[i][j] == 'k':
            sheep += 1
        elif arr[i][j] == 'v':
            fox += 1

        for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != '#' and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni, nj))


    if sheep > fox:
        sheep_cnt += sheep
    else:
        fox_cnt += fox


R, C = map(int, sys.stdin.readline().split())

arr = [list(sys.stdin.readline().strip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
sheep_cnt = 0
fox_cnt = 0

for i in range(R):
    for j in range(C):
        if arr[i][j] != '#' and visited[i][j] == 0:
            fox_sheep(i, j)

print(sheep_cnt, fox_cnt)