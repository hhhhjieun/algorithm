# 연속부분최대곱
import sys

N = int(sys.stdin.readline())
numbers = [float(sys.stdin.readline().strip()) for _ in range(N)]


for i in range(1, N):
    numbers[i] = max(numbers[i], numbers[i] * numbers[i - 1])

print(f'{max(numbers):.3f}')

