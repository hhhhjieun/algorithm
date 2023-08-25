import sys

N, K = map(int, sys.stdin.readline().split())  # 전체 날짜, 연속 날짜

temperatures = list(map(int, sys.stdin.readline(). split()))


# 맨처음 온도 합
tmp = 0
for i in range(K):
    tmp += temperatures[i]

# 최대합
max_tmp = tmp

for j in range(1, N-K+1):
    # 이전 값에서 맨 왼쪽 값 -
    tmp -= temperatures[j-1]
    # 맨 오른쪽 값 +
    tmp += temperatures[j + K - 1]

    if max_tmp < tmp:
        max_tmp = tmp

print(max_tmp)