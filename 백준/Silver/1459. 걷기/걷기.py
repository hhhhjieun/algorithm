# 걷기
import sys

X, Y, W, S = map(int, sys.stdin.readline().split())

result = 0

# 한 블록씩 두번 간 경우가 대각선보다 작다면
if 2*W <= S:
    print((X+Y) * W)

else:
    # 대각선으로 갈 수 있는만큼 가기
    min_length = min(X, Y)
    result = min_length * S
    # 남은 거리
    rest_length = abs(X - Y)
    if W > S:
        if rest_length % 2 == 0:
            result += rest_length * S
        else:
            result += (rest_length-1) * S + W
    else:
        result += rest_length * W

    print(result)
