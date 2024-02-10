# 복권
'''
n개 중 m개 선택
m개 중 k개 이상 포함되면 당첨
m개 중 k~m 개 포함하는 경우의 수 +

'''
import sys
from itertools import combinations

N, M, K = map(int, sys.stdin.readline().split())

result = 0

lotto = [*combinations([i for i in range(N)], M)]
# print(lotto)

for i in lotto:
    cnt = 0
    for j in range(M):
        if i[j] < M:
            cnt += 1

    if cnt >= K:
        result += 1

print(result / len(lotto))