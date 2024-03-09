# 민서의 응급 수술
import sys

N, M = map(int, sys.stdin.readline().split())
parent = list(range(N + 1))


def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

cnt = 0
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())

    if find_parent(parent, u) == find_parent(parent, v):
        cnt += 1

    union_parent(parent, u, v)

ans = 0
for i in range(1, N):
    if find_parent(parent, i) != find_parent(parent, i + 1):
        union_parent(parent, i, i + 1)
        ans += 1

print(cnt + ans)