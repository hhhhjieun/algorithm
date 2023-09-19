while True:
    arr = str(input())
    if arr == 'end':
        break

    first = arr.count('X')
    second = arr.count('O')

    if first < second or first-second > 1:
        print('invalid')
        continue

    tick = [[] for _ in range(3)]
    for i in range(9):
        row = i // 3
        tick[row].append(arr[i])

    x_cnt = 0
    o_cnt = 0
    # 행별 검사
    for i in range(3):
        x = 0
        o = 0
        for j in range(3):
            if tick[i][j] == 'X':
                x += 1
            if tick[i][j] == 'O':
                o += 1
        if x == 3:
            x_cnt += 1
        if o == 3:
            o_cnt += 1

    # 열별 검사
    for i in range(3):
        x = 0
        o = 0
        for j in range(3):
            if tick[j][i] == 'X':
                x += 1
            if tick[j][i] == 'O':
                o += 1
        if x == 3:
            x_cnt += 1
        if o == 3:
            o_cnt += 1

    # 대각선 검사
    x = 0
    o = 0
    for i in range(3):
        if tick[i][i] == 'X':
            x += 1
        if tick[i][i] == 'O':
            o += 1
    if x == 3:
        x_cnt += 1
    if o == 3:
        o_cnt += 1

    x = 0
    o = 0
    for i in range(3):
        if tick[2-i][i] == 'X':
            x += 1
        if tick[2-i][i] == 'O':
            o += 1
    if x == 3:
        x_cnt += 1
    if o == 3:
        o_cnt += 1

    if x_cnt and o_cnt:
        print('invalid')
        continue

    if first+second < 9 and x_cnt + o_cnt == 0:
        print('invalid')
        continue

    if first > second and x_cnt < o_cnt:
        print('invalid')
        continue

    if first == second and x_cnt > o_cnt:
        print('invalid')
        continue


    print('valid')