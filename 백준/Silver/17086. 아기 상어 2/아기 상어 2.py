N, M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
q = []
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            q.append((i,j))
            visited[i][j] = 1

di = [1,0,-1,0,-1,-1,1,1]
dj = [0,1,0,-1,1,-1,1,-1]

while q:
    t = q.pop(0)
    for k in range(8):
        ni = t[0] + di[k]
        nj = t[1] + dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            if visited[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = visited[t[0]][t[1]] + 1

safe = 0
for i in range(N):
    for j in range(M):
        if safe < visited[i][j]:
            safe = visited[i][j]

print(safe-1)