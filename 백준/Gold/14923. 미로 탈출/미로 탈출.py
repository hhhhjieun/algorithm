# 미로탈출
import sys
from collections import deque

def escape(y, x):
    q = deque()
    q.append((y, x, 0, 1))

    visited = [[[False for _ in range(2)] for _ in range(M)] for _ in range(N)]
    visited[y][x][1] = True

    while q:
        i, j, time, magic = q.popleft()

        if (i, j) == (Ey - 1, Ex - 1):
            return time

        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj][magic]:
                    continue

                if arr[ni][nj] == 1 and magic == 1:
                    visited[ni][nj][0] = True
                    q.append((ni, nj, time + 1, magic - 1))

                elif arr[ni][nj] == 0:
                    visited[ni][nj][magic] = True
                    q.append((ni, nj, time + 1, magic))

    return -1


N, M = map(int, sys.stdin.readline().split())
Hy, Hx = map(int, sys.stdin.readline().split())
Ey, Ex = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(escape(Hy-1, Hx-1))
