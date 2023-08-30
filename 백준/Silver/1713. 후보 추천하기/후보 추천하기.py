import sys

N = int(sys.stdin.readline())  # 사진틀
M = int(sys.stdin.readline())  # 추천 횟수
arr = list(map(int, sys.stdin.readline().split()))  # 추천번호

# 사진틀 만들기(q)
photos = [[0, 0]]

# 후보 추천
for i in range(M):
    # 사진틀이 비어있을 때
    if len(photos) < N:
        for j in range(len(photos)):
            # 해당 번호가 있으면
            if photos[j][0] == arr[i]:
                photos[j][1] += 1
                break
        else:
            # 해당 번호가 없으면
            if [0, 0] in photos:
                photos[0][0] = arr[i]
                photos[0][1] = 1

            else:
                photos.append([arr[i], 1])

    # 사진틀이 가득 차있을 때,
    else:
        # 추천 받은 횟수가 가장 적은 학생
        min_vote = photos[0][1]
        min_idx = 0
        for j in range(1, N):
            if photos[j][1] < min_vote:
                min_vote = photos[j][1]
                min_idx = j

        for j in range(N):
            # 해당 번호가 있으면
            if photos[j][0] == arr[i]:
                photos[j][1] += 1
                break

        # 해당 번호가 없으면
        else:
            # 추천 횟수 가장 적은 학생 삭제, 해당 자리 삽입
            for k in range(N):
                if photos[k][1] == min_vote:
                    photos.pop(k)
                    photos.append([arr[i], 1])
                    break


result = []
for i in range(len(photos)):
    if photos[i][0] != 0:
        result.append(photos[i][0])

result.sort()
print(*result)