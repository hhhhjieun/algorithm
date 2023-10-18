# 흩날리는 시험지 속에서 내 평점이 느껴진거야
'''
시험지를 현재 순서 그대로 K 개의 그룹으로 나눈 뒤
각각의 그룹에서 맞은 문제 개수의 합을 구하여
그 중 최솟값을 시험 점수로 하기로 합
이번 시험에서 받을 수 있는 최대 점수 계산
'''
import sys
N, K = map(int, sys.stdin.readline().split())
correct = list(map(int, sys.stdin.readline().split()))

# 구간을 본다
def interval(mid):
    # 구간의 개수
    cnt = 1
    i = 0
    while i < N:
        tmp = 0
        while tmp <= mid and i < N:
            tmp += correct[i]
            i += 1
        if tmp > mid:
            cnt += 1
    return cnt


# 점수를 이분탐색?
start, end = 0, 20*(10**5)
result = 0

while start <= end:
    mid = (start + end) // 2

    # 구간의 개수가 K보다 작으면 점수를 줄여라
    if interval(mid) <= K:
        end = mid - 1
        result = mid
    else:
        start = mid + 1

print(result)