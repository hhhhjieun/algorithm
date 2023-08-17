import sys
sys.setrecursionlimit(100000)

T = int(input())

# 상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bugs(i, j):
    for k in range(4):
        ny = i + dy[k]
        nx = j + dx[k]
        
        if 0 <= ny < N and 0 <= nx < M:
            if cabbages[ny][nx] == 1:
                cabbages[ny][nx] = 0
                bugs(ny, nx)


for test_case in range(1, T + 1):
    # M : 가로, N : 세로, K : 배추 위치
    M, N, K = map(int, input().split())

    cabbages = [[0] * M for _ in range(N)]

    for _ in range(K):
        v1, v2 = map(int, input().split())
        cabbages[v2][v1] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if cabbages[i][j] == 1:
                bugs(i, j)
                cnt += 1

    print(cnt)