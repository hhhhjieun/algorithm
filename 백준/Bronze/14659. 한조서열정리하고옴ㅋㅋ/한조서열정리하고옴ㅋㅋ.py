N = int(input())
arr = list(map(int, input().split()))

high = 0
cnt = 0
max_cnt = 0

for i in arr:
    if i > high:
        high = i
        cnt = 0
    else:
        cnt += 1

    if max_cnt < cnt:
        max_cnt = cnt
print(max_cnt)