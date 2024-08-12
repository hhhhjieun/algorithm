import sys

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = 0

road = [[True] * N for _ in range(N)]

for k in range(N):  # 정점
    for i in range(N):  # 시작점
        if k != i:
            for j in range(N):  # 도착점
                if k != j and i != j:
                    if arr[i][j] == arr[i][k] + arr[k][j]:
                        road[i][j] = False
                    elif arr[i][j] > arr[i][k] + arr[k][j]:
                        result = -1

if result == 0:
    for i in range(N):
        for j in range(i, N):
            if road[i][j]:
                result += arr[i][j]

print(result)