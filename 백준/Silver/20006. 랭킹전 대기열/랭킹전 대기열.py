# 랭킹전 대기열
'''
p: 플레이어 수
m : 방의 정원
l : 플레이어 레벨
n : 닉네임
'''
import sys

p, m = map(int, sys.stdin.readline().split())

rooms = []

for i in range(p):
    l, n = sys.stdin.readline().split()

    # 플레이어 입장
    # 첫번째
    if i == 0:
        rooms.append([])
        rooms[0].append([int(l), n])
    else:
        # 비교
        result = True
        for j in range(len(rooms)):
            if abs(rooms[j][0][0] - int(l)) <= 10 and len(rooms[j]) < m:
                rooms[j].append([int(l), n])
                result = True
                break

            else:
                result = False

        if result is False:
            rooms.append([])
            rooms[-1].append([int(l), n])


for i in range(len(rooms)):
    rooms[i].sort(key= lambda x:x[1])
    if len(rooms[i]) % m == 0:
        print('Started!')
    else:
        print('Waiting!')
    for j in range(len(rooms[i])):
        print(rooms[i][j][0], rooms[i][j][1])