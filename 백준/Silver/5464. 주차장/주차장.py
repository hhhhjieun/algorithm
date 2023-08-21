import sys

N, M = map(int, sys.stdin.readline().split())  # N: 주차 공간의 수, M : 차량의 수

charges = list(int(sys.stdin.readline()) for _ in range(N))  # 주차 공간의 단위 무게당 요금

car = list(int(sys.stdin.readline()) for _ in range(M))  # 차량의 무게
cars = [[idx+1, weigh] for idx, weigh in enumerate(car)]  # 차량의 번호, 무게

total_income = 0  # 총 수입
parking_lot = [[0, 0] for _ in range(N)]  # 주차장 q
waiting = []  # 대기

# 주차
for i in range(2*M):
    car_num = int(sys.stdin.readline())
    # 입차
    if car_num > 0:
        if [0, 0] in parking_lot:  # 주차 공간이 있으면
            for j in range(N):
                if parking_lot[j][0] == 0:
                    parking_lot[j] = cars[car_num-1]
                    break
        else:
            waiting.append(cars[car_num-1])
    # 출차
    else:
        for j in range(N):
            if parking_lot[j][0] == -(car_num):
                # 요금 계산
                income = (charges[j] * parking_lot[j][1])
                total_income += income
                parking_lot[j] = [0, 0]

                if waiting:
                    parking_lot[j] = waiting.pop(0)

                break

print(total_income)