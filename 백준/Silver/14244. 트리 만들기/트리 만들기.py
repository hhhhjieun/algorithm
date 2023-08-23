import sys

n, m = map(int, sys.stdin.readline().split())

# 자식 노드 표
children = [[0] * n for _ in range(n)]

# 루트 0에서 m까지 간선 연결
for i in range(1, m+1):
    children[0][i] = 1


cnt = m+1
node = 1
while cnt < n:
    children[node][cnt] = 1
    node += 1
    cnt += 1

for i in range(n):
    for j in range(n):
        if children[i][j] == 1:
            print(i, j)
