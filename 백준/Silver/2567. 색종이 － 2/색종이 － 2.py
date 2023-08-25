import sys

N = int(sys.stdin.readline())

canvas = [[0] * 101 for _ in range(101)]

# 색종이 배치
for _ in range(N):
    left, under = map(int, sys.stdin.readline().split())
    for i in range(under, under + 10):
        for j in range(left, left + 10):
            canvas[i][j] += 1

# 길이
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

length = 0

for i in range(101):
    for j in range(101):
        if canvas[i][j] >= 1:
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]

                if 0 <= ni <= 101 and 0 <= nj <= 101:
                    if canvas[ni][nj] == 0:
                        length += 1

print(length)