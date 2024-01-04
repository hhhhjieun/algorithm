# 군사 이동
'''
유니온 파인드
우선순위 큐에 모든 경로를 넣어 넓이가 넓은 경로가 먼저 나오도록 한다
'''
import sys
import heapq


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        arr[b] = a
    else:
        arr[a] = b

    return

def find(a):
    if arr[a] != a:
        return find(arr[a])
    return a


p, w = map(int, sys.stdin.readline().split())
c, v = map(int, sys.stdin.readline().split())

arr = [i for i in range(p+1)]

q = []

for i in range(w):
    n, e, width = map(int, sys.stdin.readline().split())
    heapq.heappush(q, (-width, n, e))

while q:
    cost, start, end = heapq.heappop(q)
    cost = -cost
    union(start, end)

    if find(c) == find(v):
        result = cost
        break

print(result)