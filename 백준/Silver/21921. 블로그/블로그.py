N, X = map(int, input().split())
arr = list(map(int, input().split()))
max_visit = 0
visit = 0
max_cnt = [0]*N
for i in range(N):
    visit += arr[i]
    if i >= X:
        visit -= arr[i-X]

    max_cnt[i] += visit

    if max_visit < visit:
        max_visit = visit

cnt = 0
for i in range(N):
    if max_cnt[i] == max_visit:
        cnt += 1

if max_visit:
    print(max_visit)
    print(cnt)
else:
    print('SAD')