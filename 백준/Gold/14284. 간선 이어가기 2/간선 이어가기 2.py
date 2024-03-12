# 간선 이어가기 2

import sys
import heapq

INF = 1e8

def dijkstra(start):
    heapq.heappush(heap, [0, start])
    distance[start] = 0

    while heap:
        w, n = heapq.heappop(heap)
        for next, weigh in graph[n]:
            new_weigh = weigh + w
            if new_weigh < distance[next]:
                distance[next] = new_weigh
                heapq.heappush(heap, [new_weigh, next])


n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)

heap = []

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

s, t = map(int, sys.stdin.readline().split())

dijkstra(s)
print(distance[t])
