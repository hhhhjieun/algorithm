# 소가 길을 건너간 이유5
'''
N : 신호등 총 개수
K : 연속한 개수
B : 고장난 신호등 개수
'''

import sys

N, K, B = map(int, sys.stdin.readline().split())

lights = [1] * (N+1)

for _ in range(B):
    failure = int(sys.stdin.readline())
    lights[failure-1] = 0

cnt = 0
for i in range(K):
    if lights[i] == 0:
        cnt += 1

tmp = cnt
for i in range(1, N-K+1):
    if lights[i-1] == 0:
        tmp -= 1
    if lights[i+K-1] == 0:
        tmp += 1

    cnt = min(cnt, tmp)

print(cnt)


