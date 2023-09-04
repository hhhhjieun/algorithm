N = int(input())
arr = [list(map(str,input())) for _ in range(N)]

def bfs(arr):
    max_friend = 0
    for i in range(N):
        visited = [0] * N
        q = []
        q.append(i)
        visited[i] = 1
        while q:
            t = q.pop(0)
            for w in range(N):
                if arr[t][w] == 'Y' and visited[w] == 0:
                    q.append(w)
                    visited[w] = visited[t] + 1

        cnt = 0
        for i in range(N):
            if 1< visited[i] <= 3:
                cnt += 1

        if max_friend < cnt:
            max_friend = cnt

    return max_friend

print(bfs(arr))