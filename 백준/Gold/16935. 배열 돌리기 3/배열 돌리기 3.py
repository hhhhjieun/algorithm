# 배열 돌리기
'''
1. 배열을 상하 반전시키는 연산
2. 배열을 좌우 반전시키는 연산
3. 오른쪽으로 90도 회전시키는 연산
4. 왼쪽으로 90도 회전시키는 연산
5, 6번 연산을 수행하려면 배열을 크기가 N/2×M/2인 4개의 부분 배열로 나눠야 한다
5. 1번 그룹의 부분 배열을 2번 그룹 위치로, 2번을 3번으로, 3번을 4번으로, 4번을 1번으로 이동시키는 연산
6. 1번 그룹의 부분 배열을 4번 그룹 위치로, 4번을 3번으로, 3번을 2번으로, 2번을 1번으로 이동시키는 연산
'''
import sys


def order1():
    new_arr = []

    for i in range(N-1, -1, -1):
        # print(arr[i])
        new_arr.append(arr[i])

    return new_arr


def order2():
    new_arr = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            new_arr[i][j] = arr[i][M-1-j]

    return new_arr


def order3(N, M):
    new_arr = [[0] * N for _ in range(M)]

    for i in range(M):
        for j in range(N):
            new_arr[i][j] = arr[N-j-1][i]

    return new_arr


def order4(N, M):
    new_arr = [[0] * N for _ in range(M)]

    for i in range(M):
        for j in range(N):
            new_arr[i][j] = arr[j][M-i-1]

    return new_arr


def order5():
    new_arr = [[0] * M for _ in range(N)]

    for i in range(N//2):
        for j in range(M//2):
            new_arr[i][j + M//2] = arr[i][j]

    for i in range(N//2):
        for j in range(M//2, M):
            new_arr[i + N//2][j] = arr[i][j]

    for i in range(N//2, N):
        for j in range(M//2, M):
            new_arr[i][j - M//2] = arr[i][j]

    for i in range(N//2, N):
        for j in range(M//2):
            new_arr[i - N//2][j] = arr[i][j]

    return new_arr


def order6():
    new_arr = [[0] * M for _ in range(N)]

    for i in range(N // 2):
        for j in range(M // 2):
            new_arr[i + N//2][j] = arr[i][j]

    for i in range(N // 2, N):
        for j in range(M // 2):
            new_arr[i][j + M//2] = arr[i][j]

    for i in range(N // 2, N):
        for j in range(M // 2, M):
           new_arr[i - N//2][j] = arr[i][j]

    for i in range(N // 2):
        for j in range(M // 2, M):
            new_arr[i][j - M//2] = arr[i][j]

    return new_arr


N, M, R = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
orders = list(map(int, sys.stdin.readline().strip().split()))

for order in orders:

    if order == 1:
        arr = order1()

    elif order == 2:
        arr = order2()

    elif order == 3:
        arr = order3(N, M)
        N, M = M, N

    elif order == 4:
        arr = order4(N, M)
        N, M = M, N

    elif order == 5:
        arr = order5()

    elif order == 6:
        arr = order6()

for i in arr:
    print(*i)
