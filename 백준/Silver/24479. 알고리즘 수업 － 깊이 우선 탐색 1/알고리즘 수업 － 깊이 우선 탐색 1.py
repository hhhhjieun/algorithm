import sys
sys.setrecursionlimit(10**9)

def dfs(N, M, R):
    global count
    visited[R] = 1
    count += 1
    cnt[R] = count
    for w in arr[R]:
        if visited[w] == 0:
            dfs(N, M, w)


N, M, R = map(int, sys.stdin.readline().split())  # N : 정점의 수 ,M : 간선의 수 ,R : 시작 정점
arr = [[] for _ in range(N+1)]  # 간선 정보
visited = [0] * (N+1)  # visited 생성
cnt = [0] * (N+1)  # 방문 순서

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(N):
    arr[i].sort()

# print(arr)  # [[], [2, 4], [3, 4], [4], [], []]
count = 0
dfs(N, M, R)

for i in range(1, N+1):
    print(cnt[i])