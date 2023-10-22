# 스카이라인
'''
높이만 판단?
'''
import sys

n = int(sys.stdin.readline())

height = []
result = 0

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    # 이전 높이가 있을 때, 그 높이가 y보다 클 때까지 pop
    while len(height) > 0 and height[-1] > y:
        result += 1
        height.pop()

    # 같다면 continue
    if len(height) > 0 and height[-1] == y:
        continue

    # 작으면 append
    height.append(y)

# 남아있는 높이 계산
while len(height) > 0:
    if height[-1] > 0:
        result += 1
    height.pop()

print(result)


