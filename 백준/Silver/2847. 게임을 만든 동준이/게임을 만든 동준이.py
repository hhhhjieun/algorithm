T = int(input())
arr = []
for _ in range(T):
    n = int(input())
    arr.append(n)
cnt = 0
for i in range(T-1,0,-1):
    if arr[i] <= arr[i-1]:
        while arr[i] <= arr[i-1]:
            arr[i-1] -= 1
            cnt += 1

print(cnt)