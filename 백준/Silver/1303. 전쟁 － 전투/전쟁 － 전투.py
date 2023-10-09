# 전쟁 - 전투
'''
w : 아군
b : 적군
상하좌우
N 명이 뭉쳐있을 때 N**2의 위력
'''
import sys
from collections import deque

def army_merge(y, x, color):
    result = 1
    q = deque()
    q.append((y, x))

    while q:
        i, j = q.popleft()

        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < M and 0 <= nj < N and army[ni][nj] == color:
                result += 1
                q.append((ni, nj))
                army[ni][nj] = 'O'

    return result


N, M = map(int, sys.stdin.readline().split())
army = [list(sys.stdin.readline().strip()) for _ in range(M)]

w_total = 0
b_total = 0

for i in range(M):
    for j in range(N):
        if army[i][j] == 'W':
            army[i][j] = 'O'
            w_tmp = army_merge(i, j, 'W')
            # print(w_tmp)
            w_total += w_tmp ** 2

        elif army[i][j] == 'B':
            army[i][j] = 'O'
            b_tmp = army_merge(i, j, 'B')
            # print(b_tmp)
            b_total += b_tmp ** 2

        else:
            continue


print(w_total, b_total)


