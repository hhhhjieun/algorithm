# 친구비
'''
친구의 친구는 친구
적은 비용으로 친구
1 - 3
2 - 4 - 5
'''
import sys
sys.setrecursionlimit(100000)

N, M, k = map(int, sys.stdin.readline().split())

# 인덱스 맞추기
price = [0] + list(map(int, sys.stdin.readline().strip().split()))

friends = [[] for _ in range(N+1)]

for _ in range(M):
    v, w = map(int, sys.stdin.readline().split())
    # 친구 표시
    friends[v].append(w)
    friends[w].append(v)

visited = [False] * (N+1)
results = []  # 친구의 친구의 친구 확인한 리스트 저장

# dfs로 친구만들기
def make_friends(v, arr):
    for i in friends[v]:
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            make_friends(i, arr)


for i in range(1, N+1):
    if not visited[i]:
        arr = [i]
        visited[i] = True
        make_friends(i, arr)
        results.append(arr)

ans = 0
for result in results:
    cost = 100000000
    for j in result:
        if price[j] < cost:
            cost = price[j]
    ans += cost


if ans <= k:
    print(ans)
else:
    print('Oh no')
