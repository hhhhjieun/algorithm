import sys

T = int(sys.stdin.readline())

for test_case in range(1, T + 1):
    N = int(sys.stdin.readline())

    p = [0] * 101

    p[1] = 1
    p[2] = 1
    p[3] = 1
    p[4] = 2

    for i in range(5, N+1):
        p[i] = p[i-1] + p[i-5]

    print(p[N])