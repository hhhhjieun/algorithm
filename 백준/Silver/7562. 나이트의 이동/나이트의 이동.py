import sys
from collections import deque

def bfs(si, sj, I):
    visited = [[0] * I for _ in range(I)]
    deq = deque()
    deq.append((si, sj))
    visited[si][sj] = 1

    while deq:
        i, j = deq.popleft()
        if i == ei and j == ej:
            return visited[i][j] - 1

        di = [-2, -2, -1, -1, 1, 1, 2, 2]
        dj = [1, -1, 2, -2, 2, -2, 1, -1]
        for k in range(8):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < I and 0 <= nj < I and visited[ni][nj] == 0:
                deq.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

    return 0


T = int(sys.stdin.readline())

for test_case in range(1, T + 1):
    I = int(sys.stdin.readline())  # 체스판 길이
    si, sj = map(int, sys.stdin.readline().split())  # 시작점
    ei, ej = map(int, sys.stdin.readline().split())  # 도착점

    arr = [[0] * I for _ in range(I)]

    result = bfs(si, sj, I)

    print(result)