# 멀티버스2
'''
M개의 우주
N개의 행성
행성의 크기를 알고 있을 때, 균등한 우주의 쌍이 몇개인가

"좌표압축"
: 주어진 숫자를 압축해서 작은 용량과 작은 숫자 범위로 표현
-> 크기순으로 순서 지정

# planet1 = planets[0]
# sort_planet = list(sorted(set(planet1)))
# cnt = {sort_planet[i]: i for i in range(len(sort_planet))}
# for i in planet1:
#     print(cnt[i], end=' ')
#     # 0 2 1
'''
import sys
from collections import defaultdict

M, N = map(int, sys.stdin.readline().split())
planets = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
universe = defaultdict(int)
same_cnt = 0

for planet in planets:

    # 구성이 같으면 순서가 바껴도 상관없으므로 set
    sort_planet = sorted(list(set(planet)))

    # 순위 지정
    cnt = {sort_planet[i]: i for i in range(len(sort_planet))}

    # 행성에 맞게 순위 저장, 개수 추가
    vector = tuple([cnt[i] for i in planet])
    universe[vector] += 1

for i in universe.values():
    same_cnt += (i * (i - 1)) // 2

print(same_cnt)

# 시간초과...
# def multi(universe1, universe2):
#     for i in range(N-1):
#         for j in range(i+1, N):
#             if universe1[i] < universe1[j]:
#                 if universe2[i] < universe2[j]:
#                     continue
#                 else:
#                     return False
#
#             elif universe1[i] == universe1[j]:
#                 if universe2[i] == universe2[j]:
#                     continue
#                 else:
#                     return False
#             elif universe1[i] > universe1[j]:
#                 if universe2[i] > universe2[j]:
#                     continue
#                 else:
#                     return False
#
#     return True

# for i in range(M-1):
#     for j in range(i+1, M):
#         result = multi(planets[i], planets[j])
#         if result is True:
#             same_cnt += 1