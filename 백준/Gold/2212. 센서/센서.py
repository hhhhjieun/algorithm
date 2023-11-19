# 센서
'''
N : 센서의 개수
K : 집중국의 개수
'''
import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
positions = list(map(int, sys.stdin.readline().split()))

positions.sort()

# 집중국의 개수가 센서보다 많으면 거기다 세우면 됨
if K >= N:
    print(0)
    exit()

# 거리 차이
dist = []
for i in range(1, N):
    dist.append(positions[i] - positions[i - 1])

# 센서 거리가 가장 먼 순서대로 K-1개만 삭제
dist.sort()
for _ in range(K-1):
    dist.pop()

print(sum(dist))

