def janghoon(i, h):
    global min_v

    if h >= B:
        diff = h-B
        if min_v > diff:
            min_v = diff
        return

    else:
        for w in range(i,N):
            if visited[w] == 0:
                visited[w] = 1
                h += arr[w]
                janghoon(w, h)
                h -= arr[w]
                visited[w] = 0


T = int(input())
for tc in range(1, T+1):
    N, B = map(int,input().split())
    arr = list(map(int, input().split()))
    min_v = 10000*N

    visited = [0]*N

    janghoon(0,0)
    print(f'#{tc} {min_v}')