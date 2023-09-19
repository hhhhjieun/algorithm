N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_v = 1e09

def backtracking(n, cnt, cost, start):
    global visited
    global min_v
    visited[n] = cnt+1

    if cost >= min_v:
        return

    if cnt == N-1:
        if arr[n][start]:
            cost += arr[n][start]
        else:
            return
        visited[n] = 0
        if min_v > cost:
            min_v = cost
        return



    for w in range(N):
        if w != start:
            if arr[n][w] and visited[w] == 0:
                cost += arr[n][w]
                backtracking(w, cnt + 1, cost, start)
                visited[w] = 0
                cost -= arr[n][w]



for i in range(N):
    visited = [0]*N
    backtracking(i, 0, 0, i)

print(min_v)