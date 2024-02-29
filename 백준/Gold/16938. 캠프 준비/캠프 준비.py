# 캠프 준비
'''
L <= 문제 난이도의 합 <= R
X <= 가장 어려운 문제 난이도 - 가장 쉬운 문제 난이도
'''
import sys

N, L, R, X = map(int, sys.stdin.readline().split())

arr = sorted(list(map(int, sys.stdin.readline().strip().split())))

ans = 0

def camp(depth, idx, max_level, min_level, sum_level):
    global ans
    if sum_level > R:
        return
    elif depth >= 2 and L <= sum_level <= R:
        if not (max_level == None or min_level == None) and max_level - min_level >= X:
            ans += 1
    for i in range(idx, len(arr)):
        if min_level == None:
            camp(depth + 1, i + 1, arr[i], arr[i], sum_level + arr[i])
        else:
            camp(depth + 1, i + 1, arr[i], min_level, sum_level + arr[i])


camp(0, 0, None, None, 0)
print(ans)


