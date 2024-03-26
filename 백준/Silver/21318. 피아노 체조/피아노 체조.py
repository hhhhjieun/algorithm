# 피아노 체조
import sys

N = int(sys.stdin.readline())
grade = list(map(int, sys.stdin.readline().strip().split()))

res = [0] * N

for i in range(N-1):
    if grade[i+1] < grade[i]:
        res[i] = 1

prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + res[i - 1]

Q = int(sys.stdin.readline())

for _ in range(Q):
    x, y = map(int, sys.stdin.readline().split())
    print(prefix_sum[y - 1] - prefix_sum[x - 1])
