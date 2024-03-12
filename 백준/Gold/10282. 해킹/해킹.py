# 해킹
'''
다익스트라
출발 노드와, 도착 노드를 설정
알고 있는 모든 거리 값을 부여
출발 노드부터 시작하여, 방문하지 않은 인접 노드를 방문, 거리를 계산한 다음, 현재 알고있는 거리보다 짧으면 해당 값으로 갱신
현재 노드에 인접한 모든 미방문 노드까지의 거리를 계산했다면, 현재 노드는 방문한 것이므로, 미방문 집합에서 제거
도착 노드가 미방문 노드 집합에서 벗어나면, 알고리즘을 종료
'''
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


T = int(sys.stdin.readline())

for _ in range(T):
    n, d, c = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(n + 1)]

    distance = [INF] * (n + 1)

    heap = []

    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b].append((a, s))

    dijkstra(c)

    cnt = 0
    ans = 0
    for i in distance:
        if i != INF:
            cnt += 1
            ans = max(ans, i)

    print(cnt, ans)
