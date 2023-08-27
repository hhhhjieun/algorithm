import sys
N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
student = []

for i in range(N):
    student.insert(i-sequence[i], i+1)

for num in student:
    print(num, end=' ')