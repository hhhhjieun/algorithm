# 색종이 수
T = int(input())
canvas = [[0] * 100 for _ in range(100)]

for num in range(T):
    R = 10  # 변의 길이
    width_start, height_start = map(int, input().split())

    width_end = width_start + R
    height_end = height_start + R

    for i in range(height_start, height_end):
        for j in range(width_start, width_end):
            canvas[i][j] += 1

# 넓이 계산하기
# 값이 1 이상인 경우 계산
area = 0
for i in range(100):
    for j in range(100):
        if canvas[i][j] >= 1:
            area += 1

print(area)