# 에리 - 카드
'''
공유 숫자카드 x 팀 숫자카드
팀 숫자 카드 K 장 견제
'''
import sys

N, K = map(int, sys.stdin.readline().split())
share_card = list(map(int, sys.stdin.readline().strip().split()))
team_card = set(map(int, sys.stdin.readline().strip().split()))

for _ in range(K):
    s = -int(1e9)
    x = 0
    for i in team_card:
        for j in share_card:
            if s <= i * j:
                s = i * j
                x = i

    team_card.remove(x)

ans = -int(1e9)
for team in team_card:
    for share in share_card:
        ans = max(ans, team * share)

print(ans)