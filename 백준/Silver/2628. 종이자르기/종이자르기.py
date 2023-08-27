'''
0 : 가로(행)
1 : 세로(열)
입력 받은 좌표를 기준으로 넓이 구하기(?)
'''
import sys

width, height = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

cut_width = [0, width]
cut_height = [0, height]

for _ in range(N):
    way, position = map(int, sys.stdin.readline().split())
    if way == 0:
        cut_height.append(position)
    else:
        cut_width.append(position)

cut_width.sort()
cut_height.sort()

position_width = []
position_height = []

for i in range(len(cut_width) - 1):
    position_width.append(cut_width[i+1] - cut_width[i])

for i in range(len(cut_height) - 1):
    position_height.append(cut_height[i+1] - cut_height[i])

result = max(position_width) * max(position_height)

print(result)