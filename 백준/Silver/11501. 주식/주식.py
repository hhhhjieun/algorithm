import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 T
for test in range(T):
    N = int(input()) # 날 수 N
    arr = list(map(int, input().split()))

    result = 0
    last_max = arr[-1]
    sum_v = 0

    for i in range(N - 1, -1, -1):
        tmp = arr[i]
        if tmp > last_max:
            result += sum_v
            last_max = tmp
            sum_v = 0
        else:
            sum_v += (last_max - tmp)

        if i == 0:
            result += sum_v
    print(result)