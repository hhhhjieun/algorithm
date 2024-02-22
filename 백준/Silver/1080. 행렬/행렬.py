import sys

N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

cnt = 0
ans = 0


def change(i, j, arr):
    for y in range(i, i+3):
        for x in range(j, j+3):
            arr[y][x] = 1 - arr[y][x]


for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            change(i, j, A)
            cnt += 1

for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            ans = -1

if ans == -1:
    print(-1)
else:
    print(cnt)
