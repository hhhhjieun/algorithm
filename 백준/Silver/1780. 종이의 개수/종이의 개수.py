# 종이의 개수
import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

minus_cnt = 0
zero_cnt = 0
one_cnt = 0


def recur(y, x, n):
    global minus_cnt, zero_cnt, one_cnt
    
    # 자른 크기정도로 탐색
    for i in range(y, y+n):
        for j in range(x, x+n):
            if arr[i][j] != arr[y][x]:
                # 9등분하기
                for k in range(3):
                    for l in range(3):
                        recur(y+k*n//3, x+l*n//3, n//3)
                return
    
    if arr[y][x] == -1:
        minus_cnt += 1
    elif arr[y][x] == 0:
        zero_cnt += 1
    else:
        one_cnt += 1


recur(0, 0, N)
print(minus_cnt)
print(zero_cnt)
print(one_cnt)
