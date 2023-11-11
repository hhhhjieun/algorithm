# 십자뒤집기
'''
* : 검은색
. : 흰색
동서남북
모든 칸이 흰색
'''

import sys
from collections import deque
import copy

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]


def convert_board(board, x, y):
    new_board = copy.deepcopy(board)

    for i in range(5):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_board[nx][ny] = '*' if new_board[nx][ny] == '.' else '.'
            # if new_board[nx][ny] == '*':
            #     new_board[nx][ny] = '.'
            # else:
            #     new_board[nx][ny] = '*'

    return new_board


def convert_to_binary(board):
    binary_str = ''

    for x in range(3):
        for y in range(3):
            binary_str += '0' if board[x][y] == '.' else'1'
            # if board[i][j] == '.':
            #     binary_str += '0'
            # else:
            #     binary_str += '1'

    return int(binary_str, 2)


def bfs(goal):
    cnt = 0
    white_board = [['.'] * 3 for _ in range(3)]
    visited = [0] * 1000

    q = deque([white_board])
    visited[convert_to_binary(white_board)] = 1

    while q:
        loop = len(q)
        for _ in range(loop):
            board = q.popleft()
            if board == goal:
                return cnt

            for i in range(3):
                for j in range(3):
                    next_board = convert_board(board, i, j)
                    binary_code = convert_to_binary(next_board)

                    if not visited[binary_code]:
                        q.append(next_board)
                        visited[binary_code] = 1

        cnt += 1


def solution(testcase):
    time = bfs(testcase)

    return time


if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        testcase = [list(sys.stdin.readline().strip()) for _ in range(3)]
        ans = solution(testcase)
        print(ans)