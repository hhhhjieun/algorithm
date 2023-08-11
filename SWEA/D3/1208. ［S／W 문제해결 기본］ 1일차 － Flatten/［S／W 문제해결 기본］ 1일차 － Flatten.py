T = 10

for test_case in range(1, T + 1):
    N = int(input())  # dump 횟수
    dumps = list(map(int, input().split()))

    # 높이를 저장할 100개의 리스트
    heights = [0] * 101  # 높이는 항상 100이하

    # 가로 길이는 항상 100

    for height in dumps:
        heights[height] += 1

    # flatten 시작
    start = 1
    end = 100
    n = 0  # dump 횟수

    while n <= N:
        # 높이가 있을때까지 start, end 자리 이동
        while heights[start] == 0:
            start += 1

        while heights[end] == 0:
            end -= 1

        # start와 end의 높이 -1, 그 이후, 이전 높이 +1
        heights[start] -= 1
        heights[end] -= 1
        heights[start + 1] += 1
        heights[end - 1] += 1
        n += 1  # dump 횟수 +1

        if end - start <= 1:
            break

    print(f'#{test_case} {end-start}')