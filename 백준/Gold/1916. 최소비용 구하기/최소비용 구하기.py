import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    f, t, w = map(int, input().split())
    graph[f].append([t, w])


def dijkstra(start, end):
    distance = [float('inf')] * (N + 1)

    pq = []
    heapq.heappush(pq, [0,start])
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if distance[next_node] > new_cost:
                distance[next_node] = new_cost
                heapq.heappush(pq,[new_cost, next_node])
    return distance[end]


print(dijkstra(*map(int, sys.stdin.readline().split())))