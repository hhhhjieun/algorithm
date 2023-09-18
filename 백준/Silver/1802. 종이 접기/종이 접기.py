T = int(input())

for tc in range(T):
    arr = list(map(str, input()))
    possible = 1

    while len(arr) > 1:
        mid = len(arr)//2
        front = arr[:mid]
        back = arr[:mid:-1]

        for i in range(mid):
            if front[i] == back[i]:
                possible = 0
                break

        arr = front


    if possible:
        print('YES')
    else:
        print('NO')