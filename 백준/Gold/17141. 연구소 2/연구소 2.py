# 연구소
'''
0은 빈칸
1은 벽
2는 바이러스를 놓을 수 있는 칸
'''
import sys
from itertools import combinations
from collections import deque


# 바이러스 유출
def spread_virus(viruss):
    global min_time

    q = deque()
    visited = [[0] * N for _ in range(N)]

    # 바이러스 시작점 push, visited 표시
    for k in range(len(viruss)):
        q.append(viruss[k])
        visited[viruss[k][0]][viruss[k][1]] = 1

    virus_cnt = 0
    while q:
        i, j = q.popleft()

        for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and lab[ni][nj] != 1 and visited[ni][nj] == 0:
                if visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    virus_cnt += 1
                q.append((ni, nj))

    # print(visited)
    if virus_cnt + wall + M == N**2:
        # print(max(visited))
        # print(max(max(visited)))
        min_time = min(min_time, max(map(max,visited))-1)
        return True
    else:
        return False


N, M = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

min_time = 1e9

virus = []
wall = 0
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append([i, j])
        elif lab[i][j] == 1:
            wall += 1

virus_virus = list(combinations(virus, M))

ans = False
for i in range(len(virus_virus)):
    viruss = virus_virus[i]
    # print(i, viruss)
    result = spread_virus(viruss)

    if result is True:
        ans = True

if ans is False:
    print(-1)
else:
    print(min_time)

