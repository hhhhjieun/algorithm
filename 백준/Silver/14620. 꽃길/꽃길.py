N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_v = 3000


def nCr2(n, r, s):
    global min_v
    if r == 0:
        ground = 0
        di = [1,0,-1,0]
        dj = [0,1,0,-1]
        visited = [[0] * N for _ in range(N)]
        for x, y in comb:
            visited[x][y] = 1
            ground += arr[x][y]
            for k in range(4):
                nx = x + di[k]
                ny = y + dj[k]
                if visited[nx][ny] == 0:
                    ground += arr[nx][ny]
                    visited[nx][ny] = 1
                else:
                    return
        if min_v > ground:
            min_v = ground



    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr2(n, r-1, i+1)

A = []
for i in range(1, N-1):
    for j in range(1, N-1):
        A.append((i,j))


m = len(A)
R = 3
comb = [0]*R
nCr2(m, R, 0)
print(min_v)