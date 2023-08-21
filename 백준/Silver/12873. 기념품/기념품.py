import sys

N = int(sys.stdin.readline())  # 캠프 참가자수

# 참가자
players = [int(i) for i in range(1, N+1)]

# 참가자가 1명 남을때 까지
T = 1  # 단계
front = 0

while len(players) != 1:

    front = (front + (T**3) - 1) % len(players)
    players.pop(front)
    T += 1

print(players[0])
