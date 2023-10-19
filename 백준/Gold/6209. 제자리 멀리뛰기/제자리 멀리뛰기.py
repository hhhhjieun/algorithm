# 제자리 멀리뛰기
'''
d 돌선-탈출구 거리
n개의 작은 돌섬
m개를 제거하여 점프거리의 최솟값을 최대한 크게
'''
import sys

d, n, m = map(int, sys.stdin.readline().split())
stone_island = [0] + list(int(sys.stdin.readline()) for _ in range(n)) + [d]
stone_island.sort()


distance = []
for i in range(len(stone_island)-1):
    distance.append(stone_island[i+1]-stone_island[i])


def doldari(mid):
    cnt = 0
    tmp = 0

    for i in range(len(distance)):
        tmp += distance[i]

        if tmp >= mid:
            tmp = 0

        else:
            cnt += 1

    return cnt


start, end = 0, d
result = 0

while start <= end:
    mid = (start + end) // 2

    if doldari(mid) > m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)

