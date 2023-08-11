import sys

# 1과 연결되어 있는 개수
def dfs(s, N, adj_m):
    stack = []
    result = []
    visited = [False] * (N+1)
    visited[s] = True
    
    while True:
        for w in range(1, N+1):
            if adj_m[s][w] == 1 and visited[w] is False:
                stack.append(s)
                s = w
                visited[w] = True
                result.append(s)
                break

        else:
            if stack:
                s = stack.pop()
            else:
                break

    return len(result)


N = int(sys.stdin.readline())  # 컴퓨터 수
E = int(sys.stdin.readline())  # 네트워크 수
adj_m = [[0] * (N+1) for _ in range(N+1)]  # 네트워크 연결 정보

for _ in range(E):
    v1, v2 = map(int, sys.stdin.readline().split())
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

result = dfs(1, N, adj_m)
print(result)