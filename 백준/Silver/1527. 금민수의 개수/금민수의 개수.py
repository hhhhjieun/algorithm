# 금민수의 개수
'''
중복 순열
'''
import sys
from itertools import product

A, B = map(int, sys.stdin.readline().split())

a = len(str(A))
b = len(str(B))

ans = 0
for i in range(a, b + 1):
    tmp = list(product([4, 7], repeat=i))
    # print(tmp)
    for num in tmp:
        k = int(''.join(map(str, num)))
        # print(k)
        if A <= k <= B:
            ans += 1

print(ans)