# 링크와 스타트
'''
1. 조합만들기
2. start에 해당 숫자 없으면 link임
3. start와 link에 점수 더하기
'''
import sys



def cal_value():
    global min_value

    # 능력치 계산
    start_value = 0
    link_value = 0

    # i, j 가 start 팀에 있을 때
    for i in range(N):
        for j in range(N):
            # if i in start and j in start:
            #     start_value += arr[i][j] + arr[j][i]
            # elif i not in start and j not in start:
            #     link_value += arr[i][j] + arr[j][i]
            if visited[i] and visited[j]:
                start_value += arr[i][j]
            elif not visited[i] and not visited[j]:
                link_value += arr[i][j]

    min_value = min(min_value, abs(start_value - link_value))

# 조합만들기
def comb(cnt):
    # global start

    # 기저조건
    if cnt == N:
        cal_value()
        return

    # 넣어줄때
    # 방문 표시
    visited[cnt] = 1
    # start.append(cnt)
    # 재귀
    comb(cnt+1)

    # 안넣어줄때
    # 방문 초기화
    visited[cnt] = 0
    # start.pop()
    # 재귀
    comb(cnt+1)


N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [0] * N
min_value = 1e9
# start = []

comb(0)

print(min_value)