import heapq
import sys
input = sys.stdin.readline

country = int(input())
graph = [[] for _ in range(country + 1)]

for _ in range(int(input())):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])

def dijkstra(start, end):
    costs = [float('inf') for _ in range(country + 1)]
    costs[start] = 0
    queue = []
    heapq.heappush(queue, [start, 0])
    while queue:
        cur_destination, cur_cost = heapq.heappop(queue)
        if costs[cur_destination] < cur_cost :
            continue
        for new_destination, new_cost in graph[cur_destination]:
            sum_cost = new_cost + cur_cost
            if costs[new_destination] > sum_cost:
                costs[new_destination] = sum_cost
                heapq.heappush(queue, [new_destination, sum_cost])
    return costs[end]

print(dijkstra(*map(int,input().split())))