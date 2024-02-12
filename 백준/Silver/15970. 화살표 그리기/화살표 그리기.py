# 화살표 그리기
import sys

N = int(sys.stdin.readline())

positions = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    positions.append([x, y])

positions.sort(key=lambda x:(x[1], x[0]))
# print(positions)

ans = 0

for i in range(N):
    if i == 0:
        if positions[i][1] == positions[i+1][1]:
            ans += (positions[i+1][0] - positions[i][0])

    elif i == N-1:
        if positions[i-1][1] == positions[i][1]:
            ans += (positions[i][0] - positions[i-1][0])

    else:
        flag = False
        min_sum = 999999999999
        if positions[i-1][1] == positions[i][1]:
            flag = True
            min_sum = min(min_sum, (positions[i][0] - positions[i-1][0]))

        if positions[i][1] == positions[i+1][1]:
            flag = True
            min_sum = min(min_sum, (positions[i+1][0] - positions[i][0]))

        if flag is True:
            ans += min_sum

print(ans)
