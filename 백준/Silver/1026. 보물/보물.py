import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort()

total = 0
for i in range(N):
    total += A[i] * B[N-1-i]

print(total)