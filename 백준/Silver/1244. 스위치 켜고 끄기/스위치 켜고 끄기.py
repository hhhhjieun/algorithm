import sys

N = int(sys.stdin.readline())  # 스위치 개수
lights = list(map(int, sys.stdin.readline().split()))  # 스위치 상태

M = int(sys.stdin.readline())  # 학생 수
for _ in range(M):
    student = list(map(int, sys.stdin.readline().split()))

    # 성별 확인
    # 남학생
    if student[0] == 1:
        # 배수
        i = student[1]
        while i <= N:
            if i % student[1] == 0:
                if lights[i-1] == 1:
                    lights[i-1] = 0
                else:
                    lights[i-1] = 1
            i += 1

    # 여학생
    else:
        # 양 옆의 대칭
        i = student[1]
        if 0 < i - 1 <= N - 1:
            j = 0
            while 0 <= i - 1 - j < N and 0 <= i - 1 + j < N:
                if lights[i-1-j] == lights[i-1+j]:
                    j += 1
                else:
                    break

            j -= 1

            for k in range(i - j - 1, i + j):
                if lights[k] == 1:
                    lights[k] = 0
                else:
                    lights[k] = 1

        else:
            if lights[i-1] == 1:
                lights[i-1] = 0
            else:
                lights[i-1] = 1

for light in range(0, N, 20):
    print(*lights[light:light + 20])