from sys import stdin  # 입력이 많지는 않지만 그래도 해주는 것이 좋다.

input = stdin.readline

# 4방향으로 움직이므로 아래가 필요하다.
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def move(movetime):  # 매 움직임마다 변하는 보드를 구현할 함수.
    global mincnt, minmove

    pinloc = []
    for i in range(5):
        for j in range(9):
            if matrix[i][j] == 'o':
                pinloc.append((j, i))

    if len(pinloc) < mincnt:
        minmove = movetime
        mincnt = len(pinloc)


    for x, y in pinloc:  # 각 핀의 위치를 가져온다.
        for i in range(4):  # 4방향 이동
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx + dx[i] < 9 and -1 < ny + dy[i] < 5:
                if matrix[ny][nx] == 'o' and matrix[ny + dy[i]][nx + dx[i]] == '.':

                    matrix[ny][nx] = '.'
                    matrix[ny + dy[i]][nx + dx[i]] = 'o'
                    matrix[y][x] = '.'
                    move(movetime + 1)

                    matrix[ny][nx] = 'o'
                    matrix[ny + dy[i]][nx + dx[i]] = '.'
                    matrix[y][x] = 'o'


for tc in range(int(input())):
    mincnt = 10
    minmove = 10
    matrix = [list(input().rstrip()) for i in range(5)]
    input()
    move(0)
    print(mincnt, minmove)