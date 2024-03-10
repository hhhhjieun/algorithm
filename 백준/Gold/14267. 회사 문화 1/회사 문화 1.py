# 회사 문화1
'''
상사가 한 직속 부하 칭찬 -> 그 부하의 모든 부하 칭찬
dp?
'''
import sys

n, m = map(int, sys.stdin.readline().split())
nums = [0] + list(map(int, sys.stdin.readline().strip().split()))

good = [0] * (n + 1)

for _ in range(m):
    i, w = map(int, sys.stdin.readline().split())
    good[i] += w


for i in range(2, n + 1):
    good[i] += good[nums[i]]

for i in good[1:]:
    print(i, end=" ")
