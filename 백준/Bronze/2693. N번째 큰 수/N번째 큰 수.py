T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = len(arr)

    for i in range(N - 1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    result = arr[N - 3]

    print(result)