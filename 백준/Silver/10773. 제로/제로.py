import sys

K = int(sys.stdin.readline())

N = [int(sys.stdin.readline()) for _ in range(K)]

arr = []
for num in N:
    if num != 0:
        arr.append(num)
    else:
        arr.pop(-1)

total = 0
for i in arr:
    total += i

print(total)