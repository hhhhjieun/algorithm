import sys

N = int(sys.stdin.readline())

canvas = [[0] * 101 for _ in range(101)]

# 색종이 배치
for _ in range(N):
    left, under = map(int, sys.stdin.readline().split())
    for i in range(under, under + 10):
        for j in range(left, left + 10):
            canvas[i][j] += 1

area = 0
for i in range(101):
    for j in range(101):
        if canvas[i][j] >= 1:
            area += 1

print(area)