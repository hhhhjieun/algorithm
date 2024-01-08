# 빚

import sys

def Sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


T = int(sys.stdin.readline())

for _ in range(T):
    N, *money = map(int, sys.stdin.readline().split())

    # 각 비용의 차이를 최소화 하기 위한 정렬
    Sort(money)

    answer = 0

    # S(1) ~ S(N)까지 구하기 위한 반복
    # S(1) ==  0 이므로 2부터 반복
    for i in range(2, N+1):
        sum_ = 0
        # 첫 0~i 까지 구간합
        for j in range(i):
            sum_ += money[j]
        min_value = money[i-1]*i - sum_

        # j~j+i 까지 구간합을 구해서 빚의 차이 계산후 최소값 갱신
        for j in range(i, N):
            sum_ = sum_ + money[j] - money[j-i]
            min_value = min_value if min_value < (money[j] * i) - sum_ else (money[j] * i) - sum_

        # S(i)의 최소값 더하기
        answer += min_value

    print(answer)