# 숨바꼭질 4
'''
걷기 : 1초 후 x-1 or x + 1
순간이동: 1초 후 2*x
'''
import sys
from collections import deque

# 최단이동을 어떻게 할지 출력
# 동생이 있는 위치에 도달하기 까지 수빈이가 어떻게 이동했는지 확인
def path(x):
    arr = []
    temp = x
    for _ in range(dist[x]+1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

# 동생을 찾는 가장 빠른 시간 출력
def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            path(x)
            return x
        for i in (x+1, x-1, 2*x):
            if 0<=i<=100000 and dist[i]==0:
                q.append(i)
                dist[i] = dist[x] + 1
                move[i] = x

N, K = map(int, sys.stdin.readline().split())
dist = [0]*100001
move = [0]*100001
bfs()