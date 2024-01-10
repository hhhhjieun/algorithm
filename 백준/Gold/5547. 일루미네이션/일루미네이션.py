# 일루미네이션
'''
(x, y) 오른쪽은 (x+1, y)
y가 홀수일 때, 아래는 (x, y+1)
y가 짝수일 때, 오른쪽 아래는 (x, y+1)

건물은 1
'''

import sys
from collections import deque

dir_odd = [(-1, -1), (-1, 0), (1, -1), (0, 1), (1, 0), (0, -1)]
dir_even = [(0, -1), (-1, 0), (0, 1), (1, 1), (1, 0), (-1, 1)]

# 밖
def outside():
    global house

    total = 0

    # bfs
    for i in range(H):
        for j in range(W):
            # 집이면
            if house[i][j] == 1:
                tmp = 0
                q = deque()
                q.append((i, j))
                house[i][j] = 2

                while q:
                    di, dj = q.popleft()

                    cnt = 6

                    # 짝수줄
                    if di % 2 == 0:
                        for k in range(6):
                            ni, nj = di + dir_even[k][0], dj + dir_even[k][1]
                            if 0 <= ni < H and 0 <= nj < W and house[ni][nj] > 0:
                                cnt -= 1
                                if house[ni][nj] == 1:
                                    q.append((ni, nj))
                                    house[ni][nj] = 2
                    
                    # 홀수줄
                    if di % 2 == 1:
                        for k in range(6):
                            ni, nj = di + dir_odd[k][0], dj + dir_odd[k][1]
                            if 0 <= ni < H and 0 <= nj < W and house[ni][nj] > 0:
                                cnt -= 1
                                if house[ni][nj] == 1:
                                    q.append((ni, nj))
                                    house[ni][nj] = 2

                    tmp += cnt
                total += tmp
    return  total


# 갇힌 구간
def inside():
    global house

    total = 0

    # 바깥 라인에 닿을 수 있나없나로 판단하므로 가운데만 보면됨
    for i in range(1, H - 1):
        for j in range(1, W - 1):

            if house[i][j] == 0:
                tmp = 0
                q = deque()
                q.append((i, j))
                house[i][j] = -1
                flag = 0

                while q:
                    di, dj = q.popleft()

                    cnt = 6

                    # 짝수줄
                    if di % 2 == 0:
                        for k in range(6):
                            ni, nj = di + dir_even[k][0], dj + dir_even[k][1]
                            if 0 <= ni < H and 0 <= nj < W and house[ni][nj] <= 0:
                                if ni == 0 or ni == H - 1 or nj == 0 or nj == W -1:
                                    flag = 1
                                else:
                                    cnt -= 1
                                    if house[ni][nj] == 0:
                                        q.append((ni, nj))
                                        house[ni][nj] = -1

                    # 홀수줄
                    if di % 2 == 1:
                        for k in range(6):
                            ni, nj = di + dir_odd[k][0], dj + dir_odd[k][1]
                            if 0 <= ni < H and 0 <= nj < W and house[ni][nj] <= 0:
                                if ni == 0 or ni == H - 1 or nj == 0 or nj == W - 1:
                                    flag = 1
                                else:
                                    cnt -= 1
                                    if house[ni][nj] == 0:
                                        q.append((ni, nj))
                                        house[ni][nj] = -1

                    tmp += cnt

                if flag == 0:
                    total += tmp
    return total


W, H = map(int, sys.stdin.readline().split())

house = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

result = outside() - inside()
print(result)