# 파일 합치기3
'''
작은거부터 계속 더해나가?
'''
import sys
import heapq

T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    files = list(map(int, sys.stdin.readline().split()))

    ans = 0
    q = []

    for file in files:
        heapq.heappush(q, file)

    while len(q) > 1:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        ans += (a+b)
        heapq.heappush(q, a+b)

    print(ans)