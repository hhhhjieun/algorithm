'''
문제 이해부터 실패...
타자의 순서를 순열을 통해 정해준다
각 베이스 정보 리스트를 만들어 갱신
'''
import sys
from itertools import permutations

N = int(sys.stdin.readline())

ans = 0

# 1번선수 빼고 타자 순열 만들기
hit_results = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for players in permutations((range(1, 9)), 8):
    players = list(players[:3]) + [0] + list(players[3:])

    # 현재 선수
    player = 0
    result = 0

    for i in range(N):
        out = 0
        base = [0, 0, 0, 0]

        while out < 3:
            hit = hit_results[i][players[player]]

            if hit == 0:
                out += 1

            elif hit == 1:
                # 3루 주자 있으면 득점
                result += base[3]
                # base 갱신(한칸씩 미뤄주기)
                base = [0, 1, base[1], base[2]]

            elif hit == 2:
                # 2, 3루자 있으면 득점
                result += base[2] + base[3]
                # base 갱신(두칸씩 미뤄주기)
                base = [0, 0, 1, base[1]]

            elif hit == 3:
                # 1, 2, 3루자 있으면 득점
                result += base[1] + base[2] + base[3]
                # base 갱싱(세칸씩 미뤄주기)
                base = [0, 0, 0, 1]

            elif hit == 4:
                # 그냥 다 득점
                result += base[1] + base[2] + base[3] + 1
                # 초기화
                base = [0, 0, 0, 0]

            # 다음 선수
            player = (player + 1) % 9

    if result > ans:
        ans = result

print(ans)

