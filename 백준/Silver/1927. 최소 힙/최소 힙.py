import sys
import heapq

N = int(sys.stdin.readline())
heap = []
top = 0
for _ in range(N):
    X = int(sys.stdin.readline())
    if X:
        heapq.heappush(heap, X)

    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)