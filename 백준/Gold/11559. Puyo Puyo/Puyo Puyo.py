# Puyo Puyo
import sys
from collections import deque

puyo = [list(sys.stdin.readline().strip()) for _ in range(12)]

def pang(y, x):
    q = deque()
    q.append((y, x))
    temp.append((y, x))

    while q:
        i, j  = q.popleft()

        for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < 12 and 0 <= nj < 6 and puyo[ni][nj] == puyo[i][j] and visited[ni][nj] == 0:
                q.append((ni, nj))
                temp.append((ni, nj))
                visited[ni][nj] = 1


def down_puyo():
    for i in range(10, -1, -1):
        for j in range(6):
            for k in range(11, i, -1):
                if puyo[i][j] != "." and puyo[k][j] == '.':
                    puyo[k][j] = puyo[i][j]
                    puyo[i][j] = "."
                    break


def pang_puyo(temp):
    for i, j in temp:
        puyo[i][j] = "."


ans = 0
while True:
    flag = False
    visited = [[0] * 6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if puyo[i][j] != '.' and visited[i][j] == 0:
                visited[i][j] = 1
                temp = []
                pang(i, j)

                if len(temp) >= 4:
                    flag = True
                    pang_puyo(temp)

    if flag is False:
        break

    down_puyo()
    ans += 1

print(ans)

