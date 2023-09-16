# 주유소
'''
왼쪽에서 오른쪽 최소비용
다음 저렴한 가격이 나오기전까지
해당 가격으로 가기
'''
import sys

N = int(sys.stdin.readline())
km = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

i = 0
j = 1
cost = 0

while i < N:
    # i 위치의 가격이 i+j의 위치보다 작으면 계속 이동
    if price[i] <= price[i+j]:
        j += 1
        # 마지막 지점까지 도달하면,
        if i + j == N:
            cost += price[i] * sum(km[i:i+j])
            break
    # 더 저렴한 가격이 나오면 i+j 위치까지 가격 계산
    else:
        cost += (price[i] * sum(km[i:i+j]))
        # i 위치 갱신
        i += j
        # j는 다시 1부터
        j = 1

print(cost)