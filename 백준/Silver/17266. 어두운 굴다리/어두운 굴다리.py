# 어두운 굴다리
'''
개수는 고정
높이 조절
높이 H라면 왼쪽, 오른쪽으로 H만큼
'''
import sys

N = int(sys.stdin.readline())  # 굴다리 길이
M = int(sys.stdin.readline())  # 가로등 개수
lights_position = list(map(int, sys.stdin.readline().split()))

light = lights_position[0]
heights = lights_position[0]

for i in range(1, len(lights_position)):
    height = abs(light - lights_position[i])

    if height % 2 == 0:
        height //= 2
    else:
        height = (height // 2) + 1

    heights = max(heights, height)
    light = lights_position[i]

heights = max(heights, abs(N-lights_position[-1]))

print(heights)
