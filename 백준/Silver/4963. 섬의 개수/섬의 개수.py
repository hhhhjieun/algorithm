import sys
sys.setrecursionlimit(100000)


# 상, 하, 좌, 우, 대각선
dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, 1, -1, 1, -1]


def island(i, j):
    for k in range(8):
        ny = i + dy[k]
        nx = j + dx[k]

        if 0 <= ny < h and 0 <= nx < w:
            if land[ny][nx] == 1:
                land[ny][nx] = 0
                island(ny, nx)


w, h = map(int, input().split())

while w != 0 and h != 0:
    # w : 너비, h : 높이

    land = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if land[i][j] == 1:
                island(i, j)
                cnt += 1

    print(cnt)

    w, h = map(int, input().split())