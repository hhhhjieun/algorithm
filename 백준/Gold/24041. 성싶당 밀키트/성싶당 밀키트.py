# 성싶당 밀키트
'''
N개의 재료
i 번째 유통기한은 Li일까지 부패속도 Si
x일 후에 세균수는 Si * max(1, x-Li)
모든 제료의 세균수 합이 G마리 이하일 경우 섭취
최대 K까지 빼서 G 이하면 그냥 먹음
며칠 후까지 먹을 수 있나
Oi가 1일때 뺄 수 있음
'''
import sys

N, G, K = map(int, sys.stdin.readline().split())
ingredient1 = []
ingredient2 = []
for _ in range(N):
    Si, Li, Oi, = map(int, sys.stdin.readline().split())
    if Oi:
        ingredient1.append([Si, Li])
    else:
        ingredient2.append([Si, Li])


# 날짜를 target
start, end = 0, int(2e9)
result = 0

while start <= end:
    mid = (start + end) // 2
    bacteria_cnt = 0
    if len(ingredient1) > K:
        ingredient1.sort(key=lambda x:(-x[0]*max(1, mid-x[1])))
        for i in range(K, len(ingredient1)):
            bacteria_cnt += ingredient1[i][0] * max(1, mid-ingredient1[i][1])
    for i in range(len(ingredient2)):
        bacteria_cnt += ingredient2[i][0] * max(1, mid - ingredient2[i][1])

    if bacteria_cnt <= G:
        start = mid + 1
        result = max(mid, result)
    else:
        end = mid - 1

print(result)
