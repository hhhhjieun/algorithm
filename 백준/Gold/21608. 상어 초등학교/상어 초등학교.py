# 상어 초등학교
'''
조건
1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

'''
import sys

n = int(sys.stdin.readline())

# 자리 정보
seat = [[0]*(n+1) for _ in range(n+1)]

# 학생의 번호 별 좋아하는 학생의 번호를 저장할 리스트
student_like = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n**2):

    # 입력 정보 저장
    infos = list(map(int, sys.stdin.readline().split()))

    # 현재 학생의 번호
    now_student = int(infos[0])

    # 현재 학생이 좋아하는 학생의 번호
    like_student = list(map(int, infos[1:]))

    # 학생의 번호 별 좋아하는 학생의 번호를 별도로 저장
    student_like.append(infos)

    # 현재 학생을 앉힐 수 있는 자리 후보
    result = []

    for i in range(1, n+1):
        for j in range(1, n+1):

            # 해당 좌석이 빈 좌석이면
            if (seat[i][j] == 0):
                # 인접한 칸의 좋아하는 학생의 수
                like_student_cnt = 0
                # 인접한 칸의 비어있는 칸 수
                empty_cnt = 0

                # 각 위치에서 상하좌우 찾아봐
                for k in range(4):
                    ni = i + dy[k]
                    nj = j + dx[k]

                    # 교실 내에 있는지
                    if (1 <= ni < n+1 and 1 <= nj < n+1):

                        # 인접한 칸에 좋아하는 학생이 있다면, += 1
                        if (seat[ni][nj] in like_student):
                            like_student_cnt += 1

                        # 인접한 칸이 비어있다면, += 1
                        if (seat[ni][nj] == 0):
                            empty_cnt += 1

                # 현재의 중심 좌석을 현재 학생을 앉힐 수 있는 자리 후보에 추가
                result.append((like_student_cnt, empty_cnt, i, j))

    # 자리 후보를 조건에 따라 정렬
    result = sorted(result, key = lambda x : (-x[0], -x[1], x[2], x[3]))

    # 최적의 자리에 현재 학생 앉히기
    seat[result[0][2]][result[0][3]] = now_student

student_like.sort()

# 학생의 만족도
sum = 0
for i in range(1, n+1):
    for j in range(1, n+1):

        count = 0
        for k in range(4):
            ni = i + dy[k]
            nj = j + dx[k]
            # 교실 내에 있는지
            if (1 <= ni < n+1 and 1 <= nj < n+1):
                if (seat[ni][nj] in student_like[seat[i][j]-1]):
                    count += 1

        # 인접한 칸에 좋아하는 학생이 있을 경우
        if (count != 0):
            sum += 10**(count-1)

print(sum)