# 구간 나누기2
'''
구간의 점수 : 구간에 속한 수의 최댓값과 최솟값의 차이
'''
import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

def interval(m):
    max_i = min_i = arr[0]
    cnt = 1
    for i in range(1, N):
        max_i = max(arr[i], max_i)
        min_i = min(arr[i], min_i)

        # 값이 m 보다 크다면 구간을 더 나눠
        if max_i - min_i > m:
            cnt += 1
            # 구간의 최대최소값 갱신
            max_i = arr[i]
            min_i = arr[i]
    return cnt


# 점수
start, end = 0, max(arr)
result = 0

while start <= end:
    mid = (start + end) // 2

    if interval(mid) <= M:
        end = mid - 1
        result = mid
    else:
        start = mid + 1

print(result)