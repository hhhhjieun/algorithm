# 불 모으기
'''
빨간색 - 왼/오
파란색 - 왼/오
'''
import sys
N = int(sys.stdin.readline())

balls = list(sys.stdin.readline().strip())

result = 1000000000


def right_move(target, other):
    global result
    cnt_target = 0
    cnt_move = 0

    for i in range(N):
        if balls[i] == target:
            cnt_target += 1

        if balls[i] == other and cnt_target > 0:
            cnt_move += cnt_target
            cnt_target = 0

    result = min(result, cnt_move)


def left_move(target, other):
    global result
    cnt_target = 0
    cnt_move = 0

    for i in range(N-1, -1, -1):
        if balls[i] == target:
            cnt_target += 1

        if balls[i] == other and cnt_target > 0:
            cnt_move += cnt_target
            cnt_target = 0

    result = min(result, cnt_move)


right_move('R', 'B')
right_move('B', 'R')
left_move('R', 'B')
left_move('B', 'R')

print(result)