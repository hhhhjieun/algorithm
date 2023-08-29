import sys

def dfs(si, N, arr):
    stack = []
    visited = [0] * N

    while True:
        for w in range(N):

            if arr[si][w] == 1 and visited[w] == 0:
                stack.append(si)
                si = w
                visited[si] = 1
                break
        else:
            if stack:
                si = stack.pop()
            else:
                break

    return visited


N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 간선 정보


for i in range(N):
    result = dfs(i, N, arr)
    for k in result:
        print(k, end=' ')
    print()