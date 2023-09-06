import sys

N, M, K = map(int, sys.stdin.readline().split())

arr = [[0] * M for _ in range(N)]

# 숫자채우기
n = 1
for i in range(N):
    for j in range(M):
        arr[i][j] = n
        n += 1

ni = 0
nj = 0

if K != 0:
    flag = False

    for i in range(N):
        for j in range(M):
            if arr[i][j] == K:
                ni = i
                nj = j
                flag = True
                break
        if flag is True:
            break

# 길찾기
ways1 = [[0] * (nj+1) for _ in range(ni+1)]
for i in range(ni+1):
    for j in range(nj+1):
        if i == 0 or j == 0:
            ways1[i][j] = 1
        else:
            ways1[i][j] = ways1[i-1][j] + ways1[i][j-1]
result1 = ways1[-1][-1]
# print(ways1)

ways2 = [[0] * (M-nj) for _ in range(N-ni)]
for i in range(N-ni):
    for j in range(M-nj):
        if i == 0 or j == 0:
            ways2[i][j] = 1
        else:
            ways2[i][j] = ways2[i-1][j] + ways2[i][j-1]
result2 = ways2[-1][-1]
# print(ways2)
cnt = result1 * result2

print(cnt)