# 숫자 재배치
import sys
from itertools import permutations

A, B = sys.stdin.readline().split()

result = -1

per_list = []
for arr in permutations(A):
    per_list.append(list(arr))

# print(per_list)

for per in per_list:
    perm = ''.join(per)
    if perm[0] == '0':
        continue

    if int(perm) < int(B):
        result = max(result, int(perm))

print(result)
