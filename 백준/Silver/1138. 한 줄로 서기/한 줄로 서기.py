N = int(input())
arr = list(map(int, input().split()))

order = [0]*N

for i in range(N):
    m = 0
    max_cnt = arr[i]
    for j in range(N):
        if order[j] == 0:
            m = j
            break

    cnt = 0
    while cnt < max_cnt:
        m += 1
        if order[m] == 0:
            cnt += 1

    order[m] = i+1

for i in order:
    print(i, end=" ")