T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    profit = 0
    t = arr[N-1]
    for j in range(N-2,-1,-1):
        if arr[j] < t:
            d = t - arr[j]
            profit += d
        else:
            t = arr[j]

    print(profit)