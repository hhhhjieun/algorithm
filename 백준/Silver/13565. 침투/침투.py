# 침투
'''
검은색 : 전류 차단(1)
흰색 : 전류 전달(0)
위 -> 아래
맨 윗줄에서 0번 일때 dfs
'''
import sys
from collections import deque

def find_way(y, x):
    global ans

    visited[y][x] = 1
    q = deque()
    q.append((y, x))

    while q:
        i, j = q.popleft()
        if i == M - 1:
            ans = 'YES'

        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni, nj))


M, N = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(M)]
ans = 'NO'
visited = [[0] * N for _ in range(M)]

for j in range(N):
    if arr[0][j] == 0:
        find_way(0, j)

print(ans)