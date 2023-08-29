import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()
q.append((N, [N]))
visited = [0] * (N + 1)

while q:
    num, ans = q.popleft()
    if num == 1:
        print(len(ans) - 1)
        for num in ans:
            print(num, end=' ')
        break

    if visited[num] == 0:
        visited[num] = 1
        if num % 3 == 0:
            q.append((num//3, ans + [num // 3]))

        if num % 2 == 0:
            q.append((num//2, ans + [num//2]))

        q.append((num-1, ans + [num - 1]))
