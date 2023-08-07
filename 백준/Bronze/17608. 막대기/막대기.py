import sys
input = sys.stdin.readline

N = int(input())

height = []
max_height = 0
max_idx = 0
for num in range(N):
    h = int(input())
    height.append(h)
    if max_height < h:
        max_height = h
        max_idx = num


# 마지막부터 체크(오른쪽에서 봄) / 가장 큰 막대까지만 보기
# 마지막의 막대의 높이보다 큰 것만 체크
cnt = 1
stick = height[-1]

for i in range(N-1, max_idx - 1, -1):
    if height[i] > stick:
        cnt += 1
        stick = height[i]

print(cnt)