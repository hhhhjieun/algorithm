# 톱니 바퀴2
'''
방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향이다.
'''

import sys
from collections import deque


def left(idx, dir):
    if idx < 0:
        return

    if gears[idx][2] != gears[idx + 1][6]:
        left(idx - 1, -dir)
        gear2 = deque(gears[idx])
        gear2.rotate(dir)
        gears[idx] = list(gear2)


def right(idx, dir):
    if idx > T-1:
        return
    # 다르면 돌아
    if gears[idx][6] != gears[idx-1][2]:
        right(idx + 1, -dir)
        gear2 = deque(gears[idx])
        gear2.rotate(dir)
        gears[idx] = list(gear2)


T = int(sys.stdin.readline())

gears = [list(sys.stdin.readline().strip()) for _ in range(T)]

K = int(sys.stdin.readline())

for _ in range(K):
    target, direct = map(int, sys.stdin.readline().split())

    target -= 1

    left(target - 1, -direct)
    right(target + 1, -direct)

    gear2 = deque(gears[target])
    gear2.rotate(direct)
    gears[target] = list(gear2)

ans = 0
for i in range(T):
    if gears[i][0] == '1':
        ans += 1

print(ans)
