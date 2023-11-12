# 램프
'''
1 ; ON  0 : OFF
켜져있는 행의 최댓값
'''
import sys
N, M = map(int, sys.stdin.readline().split())
lamps = list(sys.stdin.readline() for _ in range(N))

K = int(sys.stdin.readline())

max_cnt = 0

for i in range(N):

    zero = 0
    for lamp in lamps[i]:
        if lamp == '0':
            zero += 1

    # 똑같은 값 가진 램프 세기
    ans = 0
    # 모두 킬 수 있으면?
    if zero <= K and zero % 2 == K % 2:
        for j in range(N):
            if lamps[i] == lamps[j]:
                ans += 1

    # 최댓값 갱신
    max_cnt = max(max_cnt, ans)

print(max_cnt)