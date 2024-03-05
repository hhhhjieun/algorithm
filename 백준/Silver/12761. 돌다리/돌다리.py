# 돌다리
'''
현 위치에서 +1, -1, +A, -A, +B, -B
순간적 힘을 모아 현 위치의 A배나 B배 위치로  좌우 이동
'''
import sys
from collections import deque

def kongkong(N):
    q = deque()
    q.append(N)

    while q:
        now_dong = q.popleft()

        if now_dong == M:
            break

        for next_dong in [now_dong+A, now_dong+B, now_dong*A, now_dong*B, now_dong-A, now_dong-B, now_dong+1, now_dong-1]:
            if 0 <= next_dong <= 100000 and visited[next_dong] == 0:
                cnt[next_dong] = cnt[now_dong] + 1
                visited[next_dong] = 1
                q.append(next_dong)


A, B, N, M = map(int, sys.stdin.readline().split())
visited = [0] * 100001
cnt = [0] * 100001
kongkong(N)
print(cnt[M])

