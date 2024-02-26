# 연구소
'''
1. 벽을 만든다
2. 바이러스 생성한다
3. 안전구역 계산한다.
'''
import sys
import copy
from collections import deque


def virus():
    global ans
    q = deque()
    visited = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                visited[i][j] = 1
                q.append((i, j))

            if arr[i][j] == 1:
                visited[i][j] = 1


    while q:
        y, x = q.popleft()

        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj = y + di, x + dj

            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0 and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append((ni, nj))

    safe = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                safe += 1

    ans = max(ans, safe)


def wall(cnt):
    if cnt == 3:
        virus()
        return

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt + 1)
                arr[i][j] = 0


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = 0
wall(0)

print(ans)