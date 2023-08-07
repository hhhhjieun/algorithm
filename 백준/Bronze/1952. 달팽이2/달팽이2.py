dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, input().split())

# N x N 크기의 값이 0인 2차원 배열 생성
snail = [[0] * N for _ in range(M)]

num = 1  # 입력할 숫자
x, y = 0, 0  # 시작 좌표
dir = 0  # 이동방향
snail[y][x] = num  # 시작 위치에 1 기록
cnt = 0  # 꺾는 횟수


# 달팽이 반복 시작
while num < M * N:
    nx = x + dx[dir]
    ny = y + dy[dir]

    # 다음 조사 위치가 0보다 크거나 같고, N 보다 작다면, 다음 위치가 0이면
    if 0 <= ny < M and 0 <= nx < N and snail[ny][nx] == 0:
        num += 1
        snail[ny][nx] = num
        x, y = nx, ny
    else:
        dir += 1
        cnt += 1
        if dir >= 4:
            dir = 0

print(cnt)