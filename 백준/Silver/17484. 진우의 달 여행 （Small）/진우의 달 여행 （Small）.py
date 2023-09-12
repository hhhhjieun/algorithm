N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
min_v = 3600
min_list = []

def f(x, y, dir, cnt):
    global min_v
    if cnt >= min_v:
        return

    if x == N-1:
        min_v = min(min_v, cnt)
        min_list.append(min_v)

    else:
        dy = [-1, 0, 1]
        for k in range(3):
            ny = y + dy[k]
            if 0<= ny <M and dir != dy[k]:
                f(x+1, ny, dy[k], cnt + arr[x+1][ny])


for i in range(M):
    cnt = arr[0][i]
    y = i
    f(0,i,2,cnt)

print(min(min_list))