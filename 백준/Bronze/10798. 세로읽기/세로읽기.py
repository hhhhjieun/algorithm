# 총 다섯줄의 입력
arr = [list(map(str, input())) for _ in range(5)]


# 열의 최댓값 찾기
max_length = 0
for i in range(5):
    length = len(arr[i])
    if max_length < length:
        max_length = length

# max_length 를 기준으로 빈 행렬 만들기
new_arr = [[0] * max_length for _ in range(5)]

# 새로운 행렬에 기존 행렬 입력
for i in range(5):
    for j in range(len(arr[i])):
        new_arr[i][j] = arr[i][j]


# 2차원 배열로 열 우선
for j in range(max_length):
    for i in range(5):
        if new_arr[i][j] == 0:
            continue
        else:
            print(new_arr[i][j], end='')